"""
return word_list and word_nature_list
"""
from pyhanlp import HanLP
from pyhanlp import JClass
import pickle
from setting import entityDictFileName
def segmentList(sentence,nshort_segment):
    # NShortSegment = JClass("com.hankcs.hanlp.seg.NShort.NShortSegment")
    # nshort_segment = NShortSegment().enableCustomDictionary(
    # False).enablePlaceRecognize(True).enableOrganizationRecognize(True)
    # nshort_segment = HanLP.newSegment("crf") #这个效果比上面的NSort效果要好
    # NShortSegment = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
    # nshort_segment = NShortSegment().enableCustomDictionary(
    # False).enablePlaceRecognize(True).enableOrganizationRecognize(True)
    word_list = []
    word_nature_index_list = []
    word_nature_list = []
    word_nature_list1 = []
    

    for word in nshort_segment.seg(sentence):
        word_nature_list1.append([str(word.word),str(word.nature)])
    # print(word_nature_list1)
    # 字典整合(比如一个nt会被识别为多个nt,需要把这几个合起来,一个时间t会被分为多个时间t,也需要合起来)
    for tuple in word_nature_list1:
        if not word_nature_list:
            word_nature_list.append(tuple)
        else:
            if tuple[1] == word_nature_list[-1][1]:
                word_nature_list[-1][0] += tuple[0]
            else:
                word_nature_list.append(tuple)

    for index, item in enumerate(word_nature_list):
        word_list.append(item[0])
        word_nature_index_list.append((item[0],item[1],index))

    # print(word_list)
    # print(word_nature_index_list)
    return word_list, word_nature_index_list