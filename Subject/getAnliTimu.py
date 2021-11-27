from math import e
from getSentenses import sentenseList
from questionGenerator import qusGenrator
from infogetter import get_story,remove_biaodian
def get_anli_timu(data,nshort_segment,entityDict):
    data1= ''
    try:
        data1 = get_story(data)
    except Exception as e:
        print(repr(e))
        
    if data1 != '':
        data = data1
    
    sentences = sentenseList(data)
    sentences = remove_biaodian(sentences)
    questiondict = {}
    
    for index, sentence in enumerate(sentences):
        try:
            questionlist = qusGenrator(sentence,nshort_segment,entityDict)
            if questionlist:
                questiondict[str(index)] = questionlist
        except Exception as e:
            print(repr(e))
            print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
            print("row:",e.__traceback__.tb_lineno)            
    return questiondict.copy()
