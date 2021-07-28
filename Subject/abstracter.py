from pyhanlp import HanLP


def getSummary(data):
    summarySentences = HanLP.extractSummary(data,5)
    print(summarySentences)
