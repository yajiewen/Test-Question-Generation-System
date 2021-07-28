def cleanData(data):
    data = data.strip() 
    deleteWordList = [' ','\n','\t','@','#','&','*','^','_','=','+','-','＃']

    for wordToRplace in deleteWordList:
        data = data.replace(wordToRplace,'')
    return data