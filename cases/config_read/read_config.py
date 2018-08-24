import os
import codecs
import configparser

config_dir = os.path.split(os.path.abspath(__file__))[0]
config_path = os.path.join(config_dir, 'config.ini')


class ReadConfig:
    def __init__(self):
        with open(config_path, 'r') as f:
            data = f.read()
            if data[:3] == codecs.BOM_UTF8:
                data = data[3:]
                with codecs.open(config_path, 'w') as file:
                    file.write(data)

        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    def get_email(self, name):
        value = self.cf.get('EMAIL', name)
        return value

    def get_http(self, name):
        value = self.cf.get('HTTP', name)
        return value

    def get_headers(self, name):
        value = self.cf.get('HEADERS', name)
        return value

    def get_db(self, name):
        value = self.cf.get('DATABASE', name)
        return value


if __name__ == '__main__':
    config = ReadConfig()
    print("打印出mail_host：", config.get_email('mail_host'))
    print("打印出baseurl：", config.get_http('baseurl'))
    print("打印出token_v：", config.get_headers('token_v'))
    print("打印出database：", config.get_db('database'))