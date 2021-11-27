def cleanData(data):
    data = data.strip() 
    deleteWordList = [' ','@','#','&','*','^','_','=','+','-','＃']

    for wordToRplace in deleteWordList:
        data = data.replace(wordToRplace,'')
    return data