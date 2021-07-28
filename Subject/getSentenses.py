"""
Return the sentences list
"""
import re
def sentenseList(data):

    data = re.sub('([。；！？\?])([^”’])', r"\1\n\2", data)  # 单字符断句符
    data = re.sub('(\.{6})([^”’])', r"\1\n\2", data)  # 英文省略号
    data = re.sub('(\…{2})([^”’])', r"\1\n\2", data)  # 中文省略号
    data = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', data)
    data = data.rstrip() 

    return data.split("\n")
