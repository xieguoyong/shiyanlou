from setuptools import setup

setup(

    name='tickets',

    py_modules=['tickets', 'parse_station'],

    install_requires=['requests', 'docopt', 'prettytable', 'colorama'],

    entry_points={

        'console_scripts': ['tickets=tickets:cli']

    }
)

