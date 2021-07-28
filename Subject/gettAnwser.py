import random

# def getThreeTimeWeongAnwser(tirad,entityDict):
#     wrongAnswers = []
#     #获取相似时间
#     timeAnwsers = entityDict[tirad[1]]
#     timeAnwsers.remove(tirad[0])
#     similarTimeAnwser = []
#     for timeAnwser in timeAnwsers:
#         if len(timeAnwser) - len(tirad[0]) <1: # 两个time字符串长度差小于等于2
#             similarTimeAnwser.append(timeAnwser)
    
#     for count in range(3):
#         randnum = random.randint(0,len(similarTimeAnwser)-1)

#         while similarTimeAnwser[randnum] == tirad[0] or similarTimeAnwser[randnum]  in wrongAnswers:
#             randnum = random.randint(0,len(similarTimeAnwser)-1)
#         wrongAnswers.append(similarTimeAnwser[randnum])
#     #print(wrongAnswers)
#     return wrongAnswers

def getThreeTimeWeongAnwser(tirad,entityDict):
    numblock = ''
    notnumblock = ''
    block_list = []
    for char in tirad[0]:
        if char >='0' and char <= '9':
            block_list.append(notnumblock)
            notnumblock = ''
            numblock += char
        else:
            block_list.append(numblock)
            numblock = ''
            notnumblock +=char
    block_list.append(notnumblock)
    block_list.append(numblock)
        
    print(block_list)

    # 找到最后一个时间index
    last_num_block_index = 0
    for index,item in enumerate(block_list):
        if item.isdigit():
            last_num_block_index = index

    # 生成答案
    wrongAnswers = []
    three_wrong_last_num_block = []
    #更具最后一个可能是什么时间生成wrongAnwser
    last_num_block = block_list[last_num_block_index] #time 中的last number
    if int(last_num_block) >=1 and int(last_num_block)<= 12: # month
        for count in range(3):
            randnum = random.randint(1,12)

            while randnum == int(last_num_block) or last_num_block  in three_wrong_last_num_block:
                randnum = random.randint(1,12)
            three_wrong_last_num_block.append(str(randnum))

    elif int(last_num_block) >=1 and int(last_num_block)<= 28: #day
        for count in range(3):
            randnum = random.randint(1,28)

            while randnum == int(last_num_block) or last_num_block  in three_wrong_last_num_block:
                randnum = random.randint(1,28)
            three_wrong_last_num_block.append(str(randnum))
    elif int(last_num_block) >=0 and int(last_num_block)<= 23: #hour
        for count in range(3):
            randnum = random.randint(1,23)

            while randnum == int(last_num_block) or last_num_block  in three_wrong_last_num_block:
                randnum = random.randint(1,23)
            three_wrong_last_num_block.append(str(randnum))
    elif int(last_num_block) >=0 and int(last_num_block)<= 59: #minit,seconds
        for count in range(3):
            randnum = random.randint(1,59)

            while randnum == int(last_num_block) or last_num_block  in three_wrong_last_num_block:
                randnum = random.randint(1,59)
            three_wrong_last_num_block.append(str(randnum))
    else:
        for count in range(3):
            three_wrong_last_num_block.append(str( int(last_num_block) - count - 1 ) )
    # generate wrongAnwser
    for count in range(3):
        block_list[last_num_block_index] = three_wrong_last_num_block[count] #替换假的数字
        wrongAnswers.append(
            ''.join(block_list)
        )

    return wrongAnswers