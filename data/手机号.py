import re


# 提取正确的手机号
# 将手机号的前 3 位号段范围设计为虚假号段，并限定在指定的集合中，譬如：990, 991, 992, 993, 994, 995, 996, 997, 998, 999。
def get_valid_phone(sign):
    res = []
    phone_list = re.findall(r'(990|991|992|993|994|995|996|997|998|999)(\d{8})', sign)
    if len(phone_list) <= 0:
        return res
    for i in phone_list:
        phone = ''.join(i)
        res.append(f'phone_{phone}')
    return res

source = '''I know that my 68021715851 future is not just a dream.Beaut 29641856693 y is found 
within.Learn to walk before 99851499842 you run.Opportunity knocks at the door but o 99508951519 
nce.Don't let the past 99461738984 steal your pre 99839614379 sent.'''
res = get_valid_phone(source)
print(res)  # ['phone_99851499842', 'phone_99508951519', 'phone_99461738984', 'phone_99839614379']
