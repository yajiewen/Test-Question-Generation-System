import re

def remove_biaodian(list):
    try:
        for i in range(0,len(list)):
            list[i] = re.sub(r"[.,;。. 、?！!；？ ，：:']$",'',list[i].strip())
        return list
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno)    
        return list        
# story_pattern = re.compile(r'((.*)事故经过(\n)*)(.*\n)*?\n')

# shiguyuanying_pattern = re.compile(r'(((.*)事故原因(\s)*))((.*)([1-9][.．])(.*)(\n)+)+')
# zhijieyuanying_pattern = re.compile(r'(((.*)直接原因(\s)*))((.*)([1-9][.．])(.*)(\n)+)+')
# jianjieyuanying_pattern = re.compile(r'(((.*)间接原因(\s)*))((.*)([1-9][.．])(.*)(\n)+)+')
# zhuyaoyuanying_pattern = re.compile(r'(((.*)主要原因(\s)*))((.*)([1-9][.．])(.*)(\n)+)+')
# ciyaoyuanying_pattern = re.compile(r'(((.*)次要原因(\s)*))((.*)([1-9][.．])(.*)(\n)+)+')

# zhenggaicuoshi_pattern = re.compile(r'(((.*)整改措施(\s)*))((.*)([1-9][.．])(.*)(\n)+)+')
# fangfancuoshi_pattern = re.compile(r'(((.*)防范措施(\s)*))((.*)([1-9][.．])(.*)(\n)+)+')

def get_title(text):
    try:
        titile_pattern = re.compile(r'^(\s*)《.*?》\s')
        value = titile_pattern.search(text).group()
        return value.strip()
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno) 
        return ''

def get_story(text):
    try:
        pattern = re.compile(r'((.*)事故经过(\n)*)(.*\n)*?\n')
        value = pattern.search(text).group()
        
        true_value = re.sub(r'(.*)事故经过(\n)*','',value)
        return true_value.strip()
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno) 
        return ''

def get_yuanyingfenxi(text):
    try:
        pattern = re.compile(r'(((.*)原因分析(\s)*))((.*)([1-9][.．、])(.*)(\n)+)+')
        value = pattern.search(text).group()

        value_pattern = re.compile(r'((.*)([1-9][.．、])(.*)(\n)+)+')
        true_value = value_pattern.search(value).group()

        true_value = re.sub(r'[1-9][.．、]','',true_value)

        list = true_value.strip().split('\n')

        list = remove_biaodian(list)
        return list[:]
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno) 
        return []


def get_shiguyuanying(text):
    try:
        pattern = re.compile(r'(((.*)事故原因(\s)*))((.*)([1-9][.．、])(.*)(\n)+)+')
        value = pattern.search(text).group()

        value_pattern = re.compile(r'((.*)([1-9][.．、])(.*)(\n)+)+')
        true_value = value_pattern.search(value).group()

        true_value = re.sub(r'[1-9][.．、]','',true_value)

        list = true_value.strip().split('\n')

        list = remove_biaodian(list)
        return list[:]
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno) 
        return []

def get_zhijieyuanying(text):
    try:
        pattern = re.compile(r'(((.*)直接原因(\s)*))((.*)([1-9][.．、])(.*)(\n)+)+')
        value = pattern.search(text).group()

        value_pattern = re.compile(r'((.*)([1-9][.．、])(.*)(\n)+)+')
        true_value = value_pattern.search(value).group()

        true_value = re.sub(r'[1-9][.．、]','',true_value)

        list = true_value.strip().split('\n')
        list = remove_biaodian(list)

        return list[:]
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno) 
        return []


def get_jianjieyuanying(text):
    try:
        pattern = re.compile(r'(((.*)间接原因(\s)*))((.*)([1-9][.．、])(.*)(\n)+)+')
        value = pattern.search(text).group()

        value_pattern = re.compile(r'((.*)([1-9][.．、])(.*)(\n)+)+')
        true_value = value_pattern.search(value).group()

        true_value = re.sub(r'[1-9][.．、]','',true_value)

        list = true_value.strip().split('\n')
        list = remove_biaodian(list)

        return list[:]
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno) 
        return []

def get_zhuyaoyuanying(text):
    try:
        pattern = re.compile(r'(((.*)主要原因(\s)*))((.*)([1-9][.．、])(.*)(\n)+)+')
        value = pattern.search(text).group()

        value_pattern = re.compile(r'((.*)([1-9][.．、])(.*)(\n)+)+')
        true_value = value_pattern.search(value).group()

        true_value = re.sub(r'[1-9][.．、]','',true_value)

        list = true_value.strip().split('\n')
        list = remove_biaodian(list)

        return list[:]
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno) 
        return []


def get_ciyaoyuanying(text):
    try:
        pattern = re.compile(r'(((.*)次要原因(\s)*))((.*)([1-9][.．、])(.*)(\n)+)+')
        value = pattern.search(text).group()

        value_pattern = re.compile(r'((.*)([1-9][.．、])(.*)(\n)+)+')
        true_value = value_pattern.search(value).group()

        true_value = re.sub(r'[1-9][.．、]','',true_value)

        list = true_value.strip().split('\n')
        list = remove_biaodian(list)

        return list[:]
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno) 
        return []


def get_zhenggaicuoshi(text):
    try:
        pattern = re.compile(r'(((.*)整改措施(\s)*))((.*)([1-9][.．、])(.*)(\n)+)+')
        value = pattern.search(text).group()

        value_pattern = re.compile(r'((.*)([1-9][.．、])(.*)(\n)+)+')
        true_value = value_pattern.search(value).group()

        true_value = re.sub(r'[1-9][.．、]','',true_value)

        list = true_value.strip().split('\n')
        list = remove_biaodian(list)

        return list[:]
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno) 
        return []

        
def get_fangfancuoshi(text):
    try:
        pattern = re.compile(r'(((.*)防范措施(\s)*))((.*)([1-9][.．、])(.*)(\n)+)+')
        value = pattern.search(text).group()

        value_pattern = re.compile(r'((.*)([1-9][.．、])(.*)(\n)+)+')
        true_value = value_pattern.search(value).group()
        
        true_value = re.sub(r'[1-9][.．、]','',true_value)

        list = true_value.strip().split('\n')
        list = remove_biaodian(list)

        return list[:]
    except Exception as e:
        print(repr(e))
        print("file:",e.__traceback__.tb_frame.f_globals['__file__'])
        print("row:",e.__traceback__.tb_lineno) 
        return []