valid = "1234567890!@$%^*(){}[];\'\",.<>/?-=_`~ "
 
answer = "phpinfo"
 
tmp1,tmp2 = '',''
for c in answer:
    for i in valid:
        for j in valid:
            if (ord(i)^ord(j) == ord(c)):
                tmp1 += i
                tmp2 += j
                break
        else:
            continue
        break
print(tmp1,tmp2)