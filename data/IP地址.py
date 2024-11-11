import re

# 提取正确的 IP 地址
def get_valid_ip(sign):
    res = []
    ip_list = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', sign)
    if len(ip_list) <= 0:
        return res
    for ip in ip_list:
        ip = ip.strip()  # 去除前后的空格
        parts = ip.split(".")
        if len(parts) != 4:
            continue
        ipsign = 1
        for part in parts:
            num = int(part)
            if num < 0 or num > 255:
                ipsign = 0
                break
        if ipsign:
            res.append(f'ip_{ip}')
    return res

source = '''Alway 172.57.54.89 s have, always  31.275.210.167 will. 
227.6.242.88 Honesty is the b 261.323.330.116 est policy.Better to 
light one candle than to c 94.293.48.182 urse the darkness.'''
res = get_valid_ip(source)
print(res)  # 应输出：['ip_172.57.54.89', 'ip_227.6.242.88']