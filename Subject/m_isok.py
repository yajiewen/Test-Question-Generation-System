def isDigit(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def m_is_ok(word_nature_index_list,m_index):
    # m is num
    condition1 = isDigit(word_nature_index_list[m_index][0]) # 解决m 不是阿拉伯数字

    condition2 = m_index != 0 #解决m 是句首第一个字

    condition3 = False
    if m_index + 1 < len(word_nature_index_list):
        if word_nature_index_list[m_index + 1][1] != 'v' : # 解决120赶来的问题
            condition3 = True

    condition4 = False
    if m_index -1 != 0 :
        if word_nature_index_list[m_index-1][1] !='w': #解决如(m) 数字作为标号的问题 数字前有标点符号的不用
            condition4 = True
    
    condition5 = False
    if m_index + 1 < len(word_nature_index_list):
        if word_nature_index_list[m_index + 1][1] == 'q' or word_nature_index_list[m_index + 1][1] == 'n' : # 看m 后跟的是不是单位词,名词
            condition5 = True
    
    condition6 = False
    if m_index + 1 < len(word_nature_index_list):
        if word_nature_index_list[m_index + 1][1] != 'w' : # 解决m后面是标点符号
            condition6 = True

    return condition1 and condition2 and condition3 and condition4 and condition5 and condition6