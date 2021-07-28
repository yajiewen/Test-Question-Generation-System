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
entityDictFileName = "entityDict.pkl"

if not os.path.exists(entityDictFileName):
    pickle.dump(entityDict,open(entityDictFileName,'wb'))