from infogetter import *
import random
from setting import add_measure2dict
def get_all_measure_timu(text,reasonDict,id):
    title = get_title(text)

    questiondict = {}
    try:
        zhenggai = get_zhenggai_timu(text,reasonDict,title,id)
        if zhenggai:
            questiondict['corrective'] = zhenggai
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno)

    try:
        fangfan = get_fangfan_timu(text,reasonDict,title,id)
        if fangfan:
            questiondict['precautions'] = fangfan
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno)
    return questiondict.copy()

def get_fangfan_timu(text,reasonDict,title,id):
    # 防范措施题目
    random_title = random.sample(reasonDict.keys(),1)[0]
    while random_title == title:
        random_title = random.sample(reasonDict.keys(),1)[0]

    measure_list = get_fangfancuoshi(text)
    if id == "":
        add_measure2dict(reasonDict,title,measure_list)
    
    dict = {}
    if len(measure_list) <3 and len(measure_list) > 0:
        
        random_index = random.randint(0,1)
        random_index1 = random.randint(0,1)
        if random_index == 0: # 生成错误判断题
            if random_index1 == 0: #生成题型1
                str = random.sample(reasonDict[random_title]['measure'],1)[0]
                dict['subject'] = str + '是该起事故的防范措施(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'
            else:
                str = random.sample(measure_list,1)[0]
                dict['subject'] = str + '不是该起事故的防范措施(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'

        else: # 生成正确判断题
            str = random.sample(measure_list,1)[0]
            dict['subject'] = str + '是该起事故的防范措施(   )'
            dict['rightAnswer'] = '对'
            dict['wrongAnswer1'] = '错'

    elif len(measure_list) == 3:
        dict['subject'] = '以下不属于该起事故的防范措施的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['measure'],1)[0]
        dict['wrongAnswer1'] = measure_list[0]
        dict['wrongAnswer2'] = measure_list[1]
        dict['wrongAnswer3'] = measure_list[2]

    elif len(measure_list) >= 4:
        while len(measure_list) >=4:
            random_index = random.randint(0,len(measure_list)-1)
            del measure_list[random_index]

        dict['subject'] = '以下不属于该起事故的防范措施的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['measure'],1)[0]
        dict['wrongAnswer1'] = measure_list[0]
        dict['wrongAnswer2'] = measure_list[1]
        dict['wrongAnswer3'] = measure_list[2]
    return dict.copy()

def get_zhenggai_timu(text,reasonDict,title,id):
    # 整改措施题目
    random_title = random.sample(reasonDict.keys(),1)[0]
    while random_title == title:
        random_title = random.sample(reasonDict.keys(),1)[0]

    measure_list = get_zhenggaicuoshi(text)
    if id == "":
        add_measure2dict(reasonDict,title,measure_list)
    
    dict = {}
    if len(measure_list) <3 and len(measure_list) > 0:
        
        random_index = random.randint(0,1)
        random_index1 = random.randint(0,1)
        if random_index == 0: # 生成错误判断题
            if random_index1 == 0: #生成题型1
                str = random.sample(reasonDict[random_title]['measure'],1)[0]
                dict['subject'] = str + '是该起事故的整改措施(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'
            else:
                str = random.sample(measure_list,1)[0]
                dict['subject'] = str + '不是该起事故的整改措施(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'

        else: # 生成正确判断题
            str = random.sample(measure_list,1)[0]
            dict['subject'] = str + '是该起事故的整改措施(   )'
            dict['rightAnswer'] = '对'
            dict['wrongAnswer1'] = '错'

    elif len(measure_list) == 3:
        dict['subject'] = '以下不属于该起事故的整改措施的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['measure'],1)[0]
        dict['wrongAnswer1'] = measure_list[0]
        dict['wrongAnswer2'] = measure_list[1]
        dict['wrongAnswer3'] = measure_list[2]

    elif len(measure_list) >= 4:
        while len(measure_list) >=4:
            random_index = random.randint(0,len(measure_list)-1)
            del measure_list[random_index]

        dict['subject'] = '以下不属于该起事故的整改措施的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['measure'],1)[0]
        dict['wrongAnswer1'] = measure_list[0]
        dict['wrongAnswer2'] = measure_list[1]
        dict['wrongAnswer3'] = measure_list[2]
    return dict.copy()