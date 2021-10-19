"""
Generate question
"""
from json import encoder
from getSegment import segmentList
from setting import Part_of_speech
from setting import entityDictFileName
from gettAnwser import getThreeTimeWeongAnwser
from m_isok import m_is_ok
from t_isok import t_is_ok
from ns_isok import ns_is_ok
import pickle
import random
import math
import json

def stringToNumber(stringnum):
    if '.' in stringnum:
        return float(stringnum)
    else:
        return int(stringnum)

def getThreeWrongAnswer(tirad,entityDict):
    wrongAnswers = []
    for count in range(3):
        randnum = random.randint(0,len(entityDict[tirad[1]])-1)

        while entityDict[tirad[1]][randnum] == tirad[0] or entityDict[tirad[1]][randnum] in wrongAnswers:
            randnum = random.randint(0,len(entityDict[tirad[1]])-1)
        wrongAnswers.append(entityDict[tirad[1]][randnum])
    return wrongAnswers

def dictPrint(dictData):
    print('{')
    for key,value in dictData.items():
        print("   '{0}' : '{1}'".format(key,value))
    print('}')


def qusGenrator(sentence,nshort_segment,entityDict):

    word_list, word_nature_index_list = segmentList(sentence,nshort_segment)

    questionList = []
    questionDict = {
        'subject':'',
        'rightAnswer':'',
        'wrongAnswer1':'',
        'wrongAnswer2':'',
        'wrongAnswer3':'',
    }

    anwserToken = '(   )'
    for index,triad in enumerate(word_nature_index_list): # triad :[word,nature,index]
        if triad[1] in Part_of_speech:
            word_list_copy = word_list[:]
            
            if triad[1] == 'm': 
                if m_is_ok(word_nature_index_list,index): # 进一步判断m 是否合适
                    # 生成subject
                    word_list_copy[triad[2]] = anwserToken
                    questionDict['subject'] =''.join(word_list_copy)
                    # 生成 anwser
                    questionDict['rightAnswer'] = triad[0]

                    # 生成 wrong anwser
                    origin_num = stringToNumber(triad[0])

                    threeWrongNumList = []
                    index_n = 1
                    wrongNum = ''
                    while len(threeWrongNumList) < 3:
                        randomNum = random.randint(0,100)
                        #浮点数处理
                        if '.' in triad[0]:
                            if randomNum % 2 == 0:
                                wrongNum = str( round(origin_num * (index_n + 3),2) )
                            else:
                                wrongNum = str( round(origin_num / (index_n + 2),2) )
                        else:
                            if randomNum % 2 == 0:
                                wrongNum = str( math.ceil(origin_num * ( (index_n + 3) * 2)) )
                            else:
                                wrongNum = str( math.ceil(origin_num / ( (index_n + 1) * 2)) )
                        index_n += 0.5
                        if wrongNum not in threeWrongNumList:
                            threeWrongNumList.append(wrongNum)


                    for key,wrongNum in zip(['wrongAnswer1','wrongAnswer2','wrongAnswer3'], threeWrongNumList):
                        questionDict[key] = wrongNum

                    # 插入题目list
                    questionList.append(questionDict.copy())   #字典是引用类型
            elif triad[1] == 't':
                    if t_is_ok(word_nature_index_list,index):
                        # 生成 subject
                        word_list_copy[triad[2]] = anwserToken
                        questionDict['subject'] =''.join(word_list_copy)
                        # 生成 anwser
                        questionDict['rightAnswer'] = triad[0]
                        # 生成 wrong anwser
                        wrongAnswers = getThreeTimeWeongAnwser(triad, entityDict)
                        questionDict['wrongAnswer1'] = wrongAnswers[0]
                        questionDict['wrongAnswer2'] = wrongAnswers[1] 
                        questionDict['wrongAnswer3'] = wrongAnswers[2]
                        # 插入题目list
                        questionList.append(questionDict.copy())   #字典是引用类型
            
            elif triad[1] == 'ns':
                if ns_is_ok(word_nature_index_list,index):
                    # 生成 subject
                    word_list_copy[triad[2]] = anwserToken
                    questionDict['subject'] =''.join(word_list_copy)
                    # 生成 anwser
                    questionDict['rightAnswer'] = triad[0]
                    #扩充answer library
                    if triad[0] not in entityDict[triad[1]]:
                        entityDict[triad[1]].append(triad[0])
                    # 生成 wrong anwser
                    wrongAnswers = getThreeWrongAnswer(triad, entityDict)
                    questionDict['wrongAnswer1'] = wrongAnswers[0]
                    questionDict['wrongAnswer2'] = wrongAnswers[1] 
                    questionDict['wrongAnswer3'] = wrongAnswers[2]
                    # 插入题目list
                    questionList.append(questionDict.copy())   #字典是引用类型
                    
     
    # for dictData in questionList:
    #     dictPrint(dictData)
    return questionList
