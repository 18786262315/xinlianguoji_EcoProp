import os
import codecs
import configparser
import random
import string
import json




# 读取配置文件
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")
print(proDir)

class ReadConfig:
    def __init__(self):
        fd = open(configPath,encoding='utf-8')
        data = fd.read()

        #  remove BOM         
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,encoding='utf-8-sig')

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value
    def get_user(self,name):
        value = self.cf.get('USER',name)
        return value
    def set_user(self,key,vl):
        value = self.cf.set('USER',key,vl)
        self.cf.write(open(configPath, "w",encoding='utf-8')) 
        return value
    def suiji(self):
        '''
          随机生成3位数
        '''
        li = [chr(i) for i in range(ord("A"),ord("Z")+1)]
        li1 = [chr(i) for i in range(ord("a"),ord("z")+1)]
        li2 = [str(i) for i in range(0,10)]
        vlaues = ''.join(random.sample(li+li1+li2, 3))
        return vlaues
    def Box_File(self,pwd):     
        """
            路径合成
        """
        s = proDir+pwd
        return s
    def rd_json(self,pwd):
        """
            读取json
        """
        ts = open(pwd,'r',encoding='utf-8')
        ds = json.load(ts)
        return ds


