import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
config = config_ini['DEFAULT']
