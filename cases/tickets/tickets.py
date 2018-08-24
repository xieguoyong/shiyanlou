# -*- coding:utf-8 -*-

"""命令行火车票查看器
Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help       显示帮助菜单
    -g              高铁
    -d              动车
    -t              特快
    -k              快车
    -z              直达

Example:
    tickets 北京 上海 2018-07-14
    tickets -dg 北京 上海 2018-07-14
"""

from docopt import docopt   # Python3 命令行参数解析工具
import requests
from parse_station import stations
from prettytable import PrettyTable     # 格式化信息打印工具，能像 MySQL 那样打印数据
from colorama import init, Fore     # 命令行着色工具

init(autoreset=True)  # init()自动初始化着色设置，autoreset=True 即恢复为默认颜色


# 封装类来解析返回的数据
class TrainsCollection:
    # header = '车次 车站 时间 历时 一等 二等 高级软卧 软卧 硬卧 硬座 无座'.split()
    header = '车次 车站 时间 历时 一等 二等 高级软卧 软卧 硬卧 硬座'.split()

    def __init__(self, available_trains, available_place, options):
        self.available_trains = available_trains
        self.available_place = available_place
        self.options = options

    @property
    def trains(self):
        for raw_train in self.available_trains:
            raw_train_list = raw_train.split('|')
            train_no = raw_train_list[3]
            initial = train_no[0].lower()
            duration = raw_train_list[10]
            if not self.options or initial in self.options:
                train = [
                    train_no,
                    '\n'.join([Fore.LIGHTGREEN_EX + self.available_place[raw_train_list[6]] + Fore.RESET, Fore.LIGHTRED_EX + self.available_place[raw_train_list[7]] + Fore.RESET]),
                    '\n'.join([Fore.LIGHTGREEN_EX + raw_train_list[8] + Fore.RESET, Fore.LIGHTRED_EX + raw_train_list[9] + Fore.RESET]),
                    duration,
                    raw_train_list[-6] if raw_train_list[-6] else '--',
                    raw_train_list[-7] if raw_train_list[-7] else '--',
                    raw_train_list[-15] if raw_train_list[-15] else '--',
                    raw_train_list[-8] if raw_train_list[-8] else '--',
                    raw_train_list[-14] if raw_train_list[-14] else '--',
                    raw_train_list[-11] if raw_train_list[-11] else '--',
                    # raw_train_list[-9] if raw_train_list[-9] else '--',
                ]
                yield train

    def pretty_print(self):
        pt = PrettyTable(self.header)
        # pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)


def cli():
    """
    docopt 会根据我们在命令行中的定义的格式自动解析出参数并返回一个字典，也就是 arguments
    """
    arguments = docopt(__doc__)
    """
    print(arguments)
    
    {'-d': True,
    '-g': True,
     '-k': False,
    '-t': False,
     '-z': False,
     '<date>': '2018-
     '<from>': '上海'
     '<to>': '瑞金'}
    """
    # 获取出发地、到达地、时间
    from_station = arguments['<from>']
    to_station = arguments['<to>']
    date = arguments['<date>']
    # print(from_station, to_station, date)

    # 将出发地、到达地转化为对应的字母代码
    from_station_code = stations.get(from_station)
    to_station_code = stations.get(to_station)
    # print(from_station_code, to_station_code)

    # 请求参数设置成dict；添加verify=False参数不验证证书
    params = {'leftTicketDTO.train_date': date, 'leftTicketDTO.from_station': from_station_code, 'leftTicketDTO.to_station': to_station_code, 'purpose_codes': 'ADULT'}
    url = 'https://kyfw.12306.cn/otn/leftTicket/query'
    re = requests.get(url, params=params)
    # print(re.json())
    available_trains = re.json()['data']['result']
    available_place = re.json()['data']['map']
    options = ''.join([key for key, value in arguments.items() if value is True])
    TrainsCollection(available_trains, available_place, options).pretty_print()


if __name__ == '__main__':
    cli()

