import configparser


FILE_PATH = "/Users/liuzhaowei/"
FILE_NAME = "config.ini"
FILE_SECTION = "charge_record"

class SettingFile():
    #初始化配置文件
    def __init__(self):
        fn = FILE_PATH+FILE_NAME
        conf = configparser.ConfigParser()
        conf.read(fn)
        if not conf.has_section(FILE_SECTION):
            conf.add_section(FILE_SECTION)
            conf.set(FILE_SECTION,"emsaddress","http://localhost")
        with open(fn, 'w') as fw:
            conf.write(fw)
    #增加或保存配置文件中key的值
    def update(self, **kargs):
        key = kargs["key"]
        value = kargs["value"]
        fn = FILE_PATH + FILE_NAME
        conf = configparser.ConfigParser()
        conf.read(fn)
        if conf.has_section(FILE_SECTION) :
            conf.set(FILE_SECTION, key, value)
        else:
            conf.add_section(FILE_SECTION)
            conf.set(FILE_SECTION, key, value)
        with open(fn, 'w') as fw:
            conf.write(fw)
    #根据key获取配置文件值
    def getByKey(self, **kargs):
        key = kargs["key"]
        fn = FILE_PATH + FILE_NAME
        conf = configparser.ConfigParser()
        conf.read(fn)
        if conf.has_option(FILE_SECTION, key):
            return conf.get(FILE_SECTION, key)
        else:
            return None

if __name__ == '__main__':
    fileSetting = SettingFile()
    fileSetting.update(key="name", value="woasis")
    print(fileSetting.getByKey(key="name"))