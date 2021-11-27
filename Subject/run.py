#coding:utf-8
from flask import Flask,request,json,jsonify
from pyhanlp import *
from dataClean import cleanData
from pyhanlp import HanLP
from pyhanlp import JClass
from getAnliTimu import get_anli_timu
from getReasonTimu import get_all_reason_timu
from getMeasureTimu import get_all_measure_timu
import pickle
from infogetter import get_title
from setting import close_write, entityDictFileName
from setting import reasonDictFileName

NShortSegment = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
nshort_segment = NShortSegment().enableCustomDictionary(
False).enablePlaceRecognize(True).enableOrganizationRecognize(True)
print("载入模型完毕")

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/quesgetter',methods = ['POST'])
def getquestion():
    if request.method == 'POST':
        data = request.form['text']
        data = cleanData(data)

        entityDict = pickle.load(open(entityDictFileName,'rb'))
        reasonDict = pickle.load(open(reasonDictFileName,'rb'))
        questiondict = {}

        # 获取案例题目
        anlitimu = get_anli_timu(data,nshort_segment,entityDict)
        if anlitimu:
            questiondict['case'] = anlitimu
        # 获取原因题目
        yuanyingtimu = get_all_reason_timu(data,reasonDict)
        if yuanyingtimu:
            questiondict['reason'] = yuanyingtimu
        # 获取措施题目
        cuoshitimu = get_all_measure_timu(data,reasonDict)
        if cuoshitimu:
            questiondict['measure'] = cuoshitimu

        # 关闭可写
        title = get_title(data)
        close_write(reasonDict,title)
        print(reasonDict)
        pickle.dump(entityDict,open(entityDictFileName,'wb'))
        pickle.dump(reasonDict,open(reasonDictFileName,'wb'))

        return jsonify(questiondict)
    else:
        return 'bad request'

if __name__ == '__main__':
   app.run(port=26666)