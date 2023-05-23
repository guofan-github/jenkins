import pytest
import yaml


# 读取yaml文件，返回整个yaml中的数据
def yamlload(filename):
    files = open(filename, 'r', encoding='utf8')
    # 读取yaml
    data = yaml.load(files, Loader=yaml.FullLoader)
    return data


# 读取yaml文件，返回需要的数据

# 获取接口信息yaml数据
def loadyaml():
    files = open('../data/接口信息.yaml', 'r', encoding='utf8')
    # 读取yaml
    data = yaml.load(files, Loader=yaml.FullLoader)
    return data




if __name__ == '__main__':

    a = loadyaml()
    print(a['login'])