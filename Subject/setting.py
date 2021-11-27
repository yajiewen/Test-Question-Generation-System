#coding:utf-8
"""
config file
"""
import pickle
import os
#Part_of_speech = ['nr', 'ns', 'nt', 'ntc', 'ntcf', 'nmc', 't', 'm']
Part_of_speech = [ 'ns', 't', 'm']
# nr 人名
# ns 地名
# nt 机构团体名
# ntc 公司名
# ntcf 工厂
# nmc 化学品
# t 时间词
# m 数词

entityDict ={
    'nr':['刘志军', '丁书苗', '张志明','李梅红','王子青',],
    'ns':['青岛', '厦门', '广州', '福建', '山东', '天津'],
    'nt':['青岛食品有限公司', '天津燃气公司', '紫荆矿业公司'],
    'ntc':['华为公司', 'Apple公司', '中兴', '腾讯', '网易'],
    'ntcf':['广州雅东制服厂', '温州皮革厂', '山东煤气批发厂'],
    'nmc':['乙烯', '丙烯', '氢气'],
    't':['2021年5月', '2013年7月3日', '2006年9月26日','17时24分','16时40分','17时20分','16时8分','13时36分'],
}

reasonDict={
    'base1':{
        'reason':['炎热的天气,外加上车间内部不通风,导致火灾','机房长期潮湿,导致线路短路'],
        'measure':['不需要措施,相关人员加强安全意识即可']
    }
}
entityDictFileName = "entityDict.pkl"
reasonDictFileName = "reasonDict.pkl"

if not os.path.exists(entityDictFileName):
    pickle.dump(entityDict,open(entityDictFileName,'wb'))

if not os.path.exists(reasonDictFileName):
    pickle.dump(reasonDict,open(reasonDictFileName,'wb'))

def add_reason2dict(reasonDict,title,list):
    if title!='':
        if title not in reasonDict.keys() and list: #list 不能为空否则可能会创建空字典
            reasonDict[title] = {
                'reason':[],
                'measure':[],
                'write':True
            }
            reasonDict[title]['reason'].extend(list)
        else:
            if reasonDict[title]['write']:
                reasonDict[title]['reason'].extend(list)

def add_measure2dict(reasonDict,title,list):
    if title!='':
        if title not in reasonDict.keys() and list:
            reasonDict[title] = {
                'reason':[],
                'measure':[],
                'write':True
            }
            reasonDict[title]['measure'].extend(list)
        else:
            if reasonDict[title]['write']:
                reasonDict[title]['measure'].extend(list)

def close_write(reasonDict,title):
    if title!='' and title in reasonDict.keys():
        reasonDict[title]['write'] = False