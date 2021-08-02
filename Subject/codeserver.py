from flask import Flask,request,json,jsonify
from abstracter import getSummary
from pyhanlp import *
from dataClean import cleanData
from getSentenses import sentenseList
from questionGenerator import qusGenrator
from abstracter import getSummary

app = Flask(__name__)

@app.route('/quesgetter',methods = ['POST'])
def getquestion():
    if request.method == 'POST':
        data = request.form['text']
        data = cleanData(data)

        sentences = sentenseList(data)
        questiondict = {}
        for index, sentence in enumerate(sentences):
            questionlist = qusGenrator(sentence)
            if questionlist:
                questiondict[str(index)] = questionlist

        return jsonify(questiondict)
    else:
        return 'bad request'

if __name__ == '__main__':
    app.config["JSON_AS_ASCII"] = False
    app.run(host='0.0.0.0',port='26666',debug=True)