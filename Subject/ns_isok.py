def ns_is_ok(word_nature_index_list,ns_index):

    condition1 = ns_index - 1 != -1
    condition2 = True
    if ns_index + 1 < len(word_nature_index_list) and ns_index - 1 != -1:
        if word_nature_index_list[ns_index-1][1] == 'w' and word_nature_index_list[ns_index+1][1] == 'w':
            condition1 = False
    
    condition3 = ns_index + 1 < len(word_nature_index_list) and word_nature_index_list[ns_index+1][1] != 'v'

    return condition1 and condition2 and condition3

