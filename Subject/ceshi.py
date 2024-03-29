#coding:utf-8
from math import trunc
import random
import regex as re
from infogetter import *
pattern = re.compile(r'((.*)事故经过(\n)*)(.*\n)*?\n')

str = u'''《杭金衢高速公路“11·29”户外广告牌吊装坠落重大事故》
2004年11月29日14时30分许，杭金衢与金丽温高速公路枢纽处（金东区下潘村段），浙江省二建钢结构有限公司在吊装广告牌施工过程中，因钢丝绳断裂，引起高6米、长1 8米、重约8吨三面体广告牌从离基础高12米处坠落，造成2人当场死亡、2人因抢救无效死亡，4人受伤的重大事故，直接经济损失约150万元。
一、工程项目概况
浙江杭金衢高速公路金华段、金丽高速公路全路段内广告牌工程造价约500万元。发包单位为浙江运通广告有限公司(以下简称发包单位），广告牌设计单位为浙江省建工建筑设计院（建筑设计甲级），施工单位为浙江省二建钢结构有限公司，项目负责人为王新华。该工程由发包单位与省二建签订施工合同，再由省二建与施工单位签订施工合同；后由施工单位与二建钢结构公司杭金衢高速公路金华段、金丽高速公路广告牌项目部(以下简称项目部)签订内部工程施工协议。项目部项目负责人为王新华，施工员为杨建忠，技术员为张志伦，安全员为朱建华(无安全员证)。项目部签约后，在杭金衢高速公路金华段、金丽高速公路全路段陆续完成二十余个广告牌的施工建设，完成合同金额300余万元，发包单位预付工程费128万元。杭金衢与金丽温高速公路枢纽处（金东区下潘村段）广告牌曾于2004年4月安装，5月13日，因钢板薄和焊接位置不对等原因坠落，根据合同由项目部重新安装。
该处的三面体广告牌经杭州市迎宾金属装饰结构厂制作完成后，定于11月29日重新吊装。广告牌采用手拉葫芦进行吊装作业，即将三只5吨手拉葫芦分别安装在直径为1.2米高20余米立柱顶上的三角架（由三根角钢焊接成）上，安装方式是用钢丝绳（17.5mm）缠绕广告牌的钢丝栓在直径为1.46米的广告牌下端园箍上吊装。
二、事故经过
该广告牌的现场安装作业由朱建华负责，张志伦负责技术，现场分吊装和牌面两个组。牌面组由杭州迎宾金属装饰结构厂负责广告牌的安装焊接，其有张接鹏、李兆峰、李荣升、孙晓文、周铁柱；吊装作业承包给牛美华（无起重机械作业上岗证），具体由牛美华提供吊装的作业工具，再聘用（50元/人*天）当地村民沈国元、沈国良、钱钢华、方建明、王海峰一同组成吊装组。
11月29日上午近9时，牌面组现场完成广告牌装配后，牛美华在现场安装作业负责人和技术员没有到场的情况下，便指挥吊装组进行吊装作业，事前又没有对广告牌立柱校正（立柱事前已朝东南偏斜）。在广告牌下负责吊装的有吊装组牛美华等六人和以及牌面组李荣升等3人（吊装组人手不足，三人被叫去帮忙），他们每3人负责一个葫芦，由牛美华指挥同时拉三只葫芦；牌面组的张接鹏、李兆峰两人用安全绳系在广告牌上到柱顶完成最后的焊接安装。至下午1 4时许，广告牌上端已吊装接近柱顶，朱建华、张志伦方至现场，张志伦检查构件的焊接质量后，继续吊装。约1 4时30分，广告牌下端吊装至离基础12米的高度时，因钢丝绳断裂，整个广告牌坠落，导致李荣升、沈国元2人当场被压死，牛美华、方建民在医院救治无效，分别于11月30日凌晨2时5分、中午11时30分死亡，沈国良、钱钢华受伤；李兆峰、张接鹏两人也随广告牌坠落受伤。

三、事故原因分析
 (三)事故原因
1. 吊装索具固定方式不规范，钢丝绳缠挂在角钢上未加垫片，钢丝绳头编结未达到国家技术标准
2. 加之立柱偏斜磨擦阻力加大，使钢丝绳吊装强度不够，钢丝绳断开后广告牌坠落，致使事故发生。
（一）直接原因
1.经事故现场勘察，柱顶三角架上的二根挂葫芦的钢丝绳（3号位为旧钢丝）已坠落在地，当中一根有抽丝现象；
2.三只葫芦均坠落，其中二只已解体损坏，一只基本完好。
（二）间接原因
1、浙江省二建钢结构有限公司承揽相关业务组建项目部后，对项目部失于管理
2.安全生产制度落实不到位。
3、项目部雇佣无证人员为安全员，
主要原因
1.将广告牌吊装业务承包给无资质的牛美华，由未经专业培训的当地村民从事吊装作业
2、现场管理不力，吊装作业前未及时校正立柱，防范措施不到位。
3、在设计图（2004年2月20日出图）未出之前，就编制了施工组织设计（2003年11月25日编制）
次要原因
1.施工过程又未按施工组织设计要求实施作业。
四、事故性质
这是一起重大责任事故。
五、事故处理结果（略）
六、整改措施
1．责令施工单位对该项目部进行整顿，落实安全生产责任制，严格施工现场安全管理，加强业务指导和现场安全生产检查。
2．省二建公司要加强对施工单位安全生产管理，落实对合作项目安全管理职责，防范类似事故的发生。
3．省建设投资集团公司要在下属单位通报“11·29”事故情况，督促各有关单位加强施工现场安全检查，消除安全隐患，落实安全整改措施，确保生产安全。    
4．建议明确有关行政主管部门户外广告设施施工的行政监管职责，加强对高速公路户外广告设施施工的安全监管，依法查处违章、违规作业等行为。

'''
# print(str)

# str = pattern.search(str).group()
# print(str)
# str = re.sub(r'(.*)事故经过(\n)*','',str)
# print(str)
# str2  = str.strip().split('\n')
# print(str2)
# print('====')
# pattern2 = re.compile(r'(([1-9][.．])(.*)(\n)+)+')
# str2 = pattern2.search(str).group()
# print(str2)
# # str2 = str2.replace(r'[1-9][.．]','')
# str2 = re.sub(r'[1-9][.．]','',str2)
# list = str2.strip().split('\n')
# print(list)

# for value in str:
#     print(value)
# pattern2 = re.compile(r'((.*)([1-9][.．])(.*)(\n)+)*')
# print(pattern2.findall(str))

# print('----------------------------------')
# print('title:',get_title(str))
# print('story',get_story(str))
# print('事故原因',get_shiguyuanying(str))

# print('直接原因',get_zhijieyuanying(str))
# print('间接原因',get_jianjieyuanying(str))
# print('主要原因',get_zhuyaoyuanying(str))
# print('次要原因',get_ciyaoyuanying(str))
# print('措施',get_zhenggaicuoshi(str))
# print('防御',get_fangfancuoshi(str))
