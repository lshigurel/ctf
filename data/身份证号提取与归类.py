import re

# 提取正确的身份证
def get_valid_idcard(sign):
    res = []
    idcard_list = re.findall(r'([0-9]{17})([0-9X])', sign)
    if len(idcard_list) <= 0:
        return res
    for i in idcard_list:
        idcard = ''.join(i)
        id_num = idcard[:17]
        wf = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        sum = 0
        for j in range(len(id_num)):
            sum += int(id_num[j]) * wf[j]
        eighteen_num = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'][sum % 11]
        if idcard[17] != eighteen_num:
            continue
        res.append(f'idcard_{idcard}')
    return res

source = '''If i could rearra 950274201511273362 nge 960913201204307387 the alphabet.I 
954847198410251461 magin 91876320000130051X ation is more important than knowledge.Every man is a p 
912142197912261827 oet wh 982068199610077126 en he is in love.'''
res = get_valid_idcard(source)
print(res)  # ['idcard_954847198410251461', 'idcard_982068199610077126']