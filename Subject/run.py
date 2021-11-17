from flask import Flask,request,json,jsonify
from abstracter import getSummary
from pyhanlp import *
from dataClean import cleanData
from getSentenses import sentenseList
from questionGenerator import qusGenrator
from abstracter import getSummary
from pyhanlp import HanLP
from pyhanlp import JClass
import pickle
from setting import entityDictFileName


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

        sentences = sentenseList(data)
        questiondict = {}
            # read dict 
        entityDict = pickle.load(open(entityDictFileName,'rb'))
        for index, sentence in enumerate(sentences):
            questionlist = qusGenrator(sentence,nshort_segment,entityDict)
            if questionlist:
                questiondict[str(index)] = questionlist
            # close dict
        pickle.dump(entityDict,open(entityDictFileName,'wb')) 
        return jsonify(questiondict)
    else:
        return 'bad request'
