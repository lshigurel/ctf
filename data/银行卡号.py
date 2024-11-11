import re

# 提取正确的银行卡号
def get_valid_bankcard(sign):
    res = []
    bankcard_list = re.findall(r'(970|971|972|973|974|975|976|977|978|979)(\d{10,16})', sign)
    if len(bankcard_list) <= 0:
        return res
    for i in bankcard_list:
        bankcard = ''.join(i)
        s = 0
        card_num_length = len(bankcard)
        for _ in range(1, card_num_length + 1):
            t = int(bankcard[card_num_length - _])
            if _ % 2 == 0:
                t *= 2
                s += t if t < 10 else t % 10 + t // 10
            else:
                s += t
        if s % 10 == 0:
            res.append(f'bankcard_{bankcard}')
    return res

source = '''From small beginnings comes gr 9715404432844352 eat things.The fi 9731072579662911574 nest diamond 
mu 9752777675570430531 st be cut.Forgettin 97541981212800125 g someone doesn't mean never think of him.'''
res = get_valid_bankcard(source)
print(res)  # 应输出：['bankcard_9731072579662911574', 'bankcard_97541981212800125']
