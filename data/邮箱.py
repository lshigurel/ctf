import re

# 提取正确的邮箱
def get_valid_email(sign):
    res = []
    email_list = re.findall(r'[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-z]{2,6}', sign)
    if len(email_list) <= 0:
        return res
    for email in email_list:
        email = email.strip()
        res.append(f'email_{email}')
    return res

source = '''To re |ecoL@126.com ad without reflecting.Whatever i 5_+)?k.Cu*,N@qq.com s 
worth doing.By reading we enrich 99727110298@soho.com the mind.Diligenceis 
99760710828@sina.cn themotherofsuccess.The best preparation for tomorrow is doi 
kIhd.LNjwIrk@sina.com ng your best today.'''
res = get_valid_email(source)
print(res)  # ['email_ecoL@126.com', 'email_N@qq.com', 'email_99727110298@soho.com', 'email_99760710828@sina.cn', 'email_kIhd.LNjwIrk@sina.com']
