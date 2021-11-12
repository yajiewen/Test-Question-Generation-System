def t_is_ok(word_nature_index_list,t_index):

    condition1 = len(word_nature_index_list[t_index][0]) >=4 # 过滤长度太短的时间
    condition2 = False

    # 判断命名实体识别出来的时间是不是全部是中文
    for char in word_nature_index_list[t_index][0]: 
        if char >='0' and char <= '9':
            condition2 = True
            break
    return condition1 and condition2
