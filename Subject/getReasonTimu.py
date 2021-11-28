from infogetter import *
import random
from setting import add_reason2dict
def get_all_reason_timu(text,reasonDict):
    title = get_title(text)

    questiondict = {}
    try:
        zhijietimu = get_zhijie_timu(text,reasonDict,title)
        if zhijietimu:
            questiondict['direct'] = zhijietimu
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno)        

    try: 
        jianjietimu = get_jianjie_timu(text,reasonDict,title)
        if jianjietimu:
            questiondict['indirect'] = jianjietimu
    except Exception as e:
        print(repr(e))       
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno)

    try: 
        zhuyaotimu = get_zhuyao_timu(text,reasonDict,title)
        if zhuyaotimu:
            questiondict['main'] = zhuyaotimu
    except Exception as e:
        print(repr(e))       
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno)       

    try: 
        ciyaotimu = get_ciyao_timu(text,reasonDict,title)
        if ciyaotimu:
            questiondict['minor'] = ciyaotimu
    except Exception as e:
        print(repr(e))  
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno)

    try: 
        shiguyuanyintimu = get_shiguyuanyin_timu(text,reasonDict,title)
        if shiguyuanyintimu:
            questiondict['story'] = shiguyuanyintimu
    except Exception as e:
        print(repr(e))  
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno)   

    try: 
        yuanyinfenxitimu = get_yuanyingfenxi_timu(text,reasonDict,title)
        if yuanyinfenxitimu:
            questiondict['analyse'] = yuanyinfenxitimu
    except Exception as e:
        print(repr(e))  
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno)   
    
    return questiondict.copy()

def get_yuanyingfenxi_timu(text,reasonDict,title):
    # 事故原因题目
    random_title = random.sample(reasonDict.keys(),1)[0]
    while random_title == title:
        random_title = random.sample(reasonDict.keys(),1)[0]

    reason_list = get_yuanyingfenxi(text)
    add_reason2dict(reasonDict,title,reason_list)

    dict = {}
    if len(reason_list) <3 and len(reason_list) > 0:
        
        random_index = random.randint(0,1)
        random_index1 = random.randint(0,1)
        if random_index == 0: # 生成错误判断题
            if random_index1 == 0: #生成题型1
                str = random.sample(reasonDict[random_title]['reason'],1)[0]
                dict['subject'] = str + '是造成该事故的原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'
            else:
                str = random.sample(reason_list,1)[0]
                dict['subject'] = str + '不是造成该事故的原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'

        else: # 生成正确判断题
            str = random.sample(reason_list,1)[0]
            dict['subject'] = str + '是造成该事故的原因(   )'
            dict['rightAnswer'] = '对'
            dict['wrongAnswer1'] = '错'

    elif len(reason_list) == 3:
        dict['subject'] = '以下不属于造成该事故的原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]

    elif len(reason_list) >= 4:
        while len(reason_list) >= 4:
            random_index = random.randint(0,len(reason_list)-1)
            del reason_list[random_index]

        dict['subject'] = '以下不属于造成该事故的原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]
    
    return dict.copy()


def get_shiguyuanyin_timu(text,reasonDict,title):
    # 事故原因题目
    random_title = random.sample(reasonDict.keys(),1)[0]
    while random_title == title:
        random_title = random.sample(reasonDict.keys(),1)[0]

    reason_list = get_shiguyuanying(text)
    add_reason2dict(reasonDict,title,reason_list)

    dict = {}
    if len(reason_list) <3 and len(reason_list) > 0:
        
        random_index = random.randint(0,1)
        random_index1 = random.randint(0,1)
        if random_index == 0: # 生成错误判断题
            if random_index1 == 0: #生成题型1
                str = random.sample(reasonDict[random_title]['reason'],1)[0]
                dict['subject'] = str + '是造成该事故的原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'
            else:
                str = random.sample(reason_list,1)[0]
                dict['subject'] = str + '不是造成该事故的原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'

        else: # 生成正确判断题
            str = random.sample(reason_list,1)[0]
            dict['subject'] = str + '是造成该事故的原因(   )'
            dict['rightAnswer'] = '对'
            dict['wrongAnswer1'] = '错'

    elif len(reason_list) == 3:
        dict['subject'] = '以下不属于造成该事故的原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]

    elif len(reason_list) >= 4:
        while len(reason_list) >= 4:
            random_index = random.randint(0,len(reason_list)-1)
            del reason_list[random_index]

        dict['subject'] = '以下不属于造成该事故的原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]
    
    return dict.copy()


def get_ciyao_timu(text,reasonDict,title):
    # 次要原因题目
    random_title = random.sample(reasonDict.keys(),1)[0]
    while random_title == title:
        random_title = random.sample(reasonDict.keys(),1)[0]

    reason_list = get_ciyaoyuanying(text)
    add_reason2dict(reasonDict,title,reason_list)
    
    dict = {}
    if len(reason_list) <3 and len(reason_list) > 0:
        
        random_index = random.randint(0,1)
        random_index1 = random.randint(0,1)
        if random_index == 0: # 生成错误判断题
            if random_index1 == 0: #生成题型1
                str = random.sample(reasonDict[random_title]['reason'],1)[0]
                dict['subject'] = str + '是造成该事故的次要原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'
            else:
                str = random.sample(reason_list,1)[0]
                dict['subject'] = str + '是造成该事故的主要原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'

        else: # 生成正确判断题
            str = random.sample(reason_list,1)[0]
            dict['subject'] = str + '是造成该事故的次要原因(   )'
            dict['rightAnswer'] = '对'
            dict['wrongAnswer1'] = '错'

    elif len(reason_list) == 3:
        dict['subject'] = '以下不属于造成该事故的次要原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]

    elif len(reason_list) >= 4:
        while len(reason_list) >= 4:
            random_index = random.randint(0,len(reason_list)-1)
            del reason_list[random_index]

        dict['subject'] = '以下不属于造成该事故的次要原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]
    return dict.copy()


def get_zhuyao_timu(text,reasonDict,title):
    # 主要原因题目
    random_title = random.sample(reasonDict.keys(),1)[0]
    while random_title == title:
        random_title = random.sample(reasonDict.keys(),1)[0]

    reason_list = get_zhuyaoyuanying(text)
    add_reason2dict(reasonDict,title,reason_list)

    dict = {}
    if len(reason_list) <3 and len(reason_list) > 0:
        
        random_index = random.randint(0,1)
        random_index1 = random.randint(0,1)
        if random_index == 0: # 生成错误判断题
            if random_index1 == 0: #生成题型1
                str = random.sample(reasonDict[random_title]['reason'],1)[0]
                dict['subject'] = str + '是造成该事故的主要原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'
            else:
                str = random.sample(reason_list,1)[0]
                dict['subject'] = str + '是造成该事故的次要原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'

        else: # 生成正确判断题
            str = random.sample(reason_list,1)[0]
            dict['subject'] = str + '是造成该事故的主要原因(   )'
            dict['rightAnswer'] = '对'
            dict['wrongAnswer1'] = '错'

    elif len(reason_list) == 3:
        dict['subject'] = '以下不属于造成该事故的主要原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]

    elif len(reason_list) >= 4:
        while len(reason_list) >= 4:
            random_index = random.randint(0,len(reason_list)-1)
            del reason_list[random_index]

        dict['subject'] = '以下不属于造成该事故的主要原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]
    return dict.copy()


def get_jianjie_timu(text,reasonDict,title):
    # 间接原因题目
    random_title = random.sample(reasonDict.keys(),1)[0]
    while random_title == title:
        random_title = random.sample(reasonDict.keys(),1)[0]

    reason_list = get_jianjieyuanying(text)
    add_reason2dict(reasonDict,title,reason_list)

    dict = {}
    if len(reason_list) <3 and len(reason_list) > 0:
        
        random_index = random.randint(0,1)
        random_index1 = random.randint(0,1)
        if random_index == 0: # 生成错误判断题
            if random_index1 == 0: #生成题型1
                str = random.sample(reasonDict[random_title]['reason'],1)[0]
                dict['subject'] = str + '是造成该事故的间接原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'
            else:
                str = random.sample(reason_list,1)[0]
                dict['subject'] = str + '是造成该事故的直接原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'

        else: # 生成正确判断题
            str = random.sample(reason_list,1)[0]
            dict['subject'] = str + '是造成该事故的间接原因(   )'
            dict['rightAnswer'] = '对'
            dict['wrongAnswer1'] = '错'

    elif len(reason_list) == 3:
        dict['subject'] = '以下不属于造成该事故的间接原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]

    elif len(reason_list) >= 4:
        while len(reason_list) >= 4:
            random_index = random.randint(0,len(reason_list)-1)
            del reason_list[random_index]

        dict['subject'] = '以下不属于造成该事故的间接原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]
    return dict.copy()



def get_zhijie_timu(text,reasonDict,title):
    # 直接原因题目
    random_title = random.sample(reasonDict.keys(),1)[0]
    while random_title == title:
        random_title = random.sample(reasonDict.keys(),1)[0]

    reason_list = get_zhijieyuanying(text)
    add_reason2dict(reasonDict,title,reason_list)
    
    dict = {}
    if len(reason_list) <3 and len(reason_list) > 0:
        
        random_index = random.randint(0,1)
        random_index1 = random.randint(0,1)
        if random_index == 0: # 生成错误判断题
            if random_index1 == 0: #生成题型1
                str = random.sample(reasonDict[random_title]['reason'],1)[0]
                dict['subject'] = str + '是造成该事故的直接原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'
            else:
                str = random.sample(reason_list,1)[0]
                dict['subject'] = str + '是造成该事故的间接原因(   )'
                dict['rightAnswer'] = '错'
                dict['wrongAnswer1'] = '对'

        else: # 生成正确判断题
            str = random.sample(reason_list,1)[0]
            dict['subject'] = str + '是造成该事故的直接原因(   )'
            dict['rightAnswer'] = '对'
            dict['wrongAnswer1'] = '错'

    elif len(reason_list) == 3:
        dict['subject'] = '以下不属于造成该事故的直接原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]

    elif len(reason_list) >= 4:
        while len(reason_list) >= 4:
            random_index = random.randint(0,len(reason_list)-1)
            del reason_list[random_index]

        dict['subject'] = '以下不属于造成该事故的直接原因的是(   )'
        dict['rightAnswer'] = random.sample(reasonDict[random_title]['reason'],1)[0]
        dict['wrongAnswer1'] = reason_list[0]
        dict['wrongAnswer2'] = reason_list[1]
        dict['wrongAnswer3'] = reason_list[2]
    return dict.copy()
