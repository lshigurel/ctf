#!/usr/bin/env python

import sys  # 引入sys模块，用于处理命令行参数
import os  # 引入os模块，用于执行系统命令

# 定义输出数据的文件名
DataFileName = "usb.dat"

# 用于存储从pcap文件中提取的键盘按键数据
presses = []

# 定义普通按键的映射字典，键是按键的16进制编码，值是对应的字符
normalKeys = {
    "04":"a", "05":"b", "06":"c", "07":"d", "08":"e", "09":"f", 
    "0a":"g", "0b":"h", "0c":"i", "0d":"j", "0e":"k", "0f":"l", 
    "10":"m", "11":"n", "12":"o", "13":"p", "14":"q", "15":"r", 
    "16":"s", "17":"t", "18":"u", "19":"v", "1a":"w", "1b":"x", 
    "1c":"y", "1d":"z", "1e":"1", "1f":"2", "20":"3", "21":"4", 
    "22":"5", "23":"6","24":"7","25":"8","26":"9","27":"0",
    "28":"<RET>", "29":"<ESC>", "2a":"<DEL>", "2b":"\t", "2c":"<SPACE>", 
    "2d":"-","2e":"=", "2f":"[", "30":"]", "31":"\\", "32":"<NON>", 
    "33":";", "34":"'", "35":"<GA>", "36":",", "37":".", "38":"/", 
    "39":"<CAP>", "3a":"<F1>", "3b":"<F2>", "3c":"<F3>", "3d":"<F4>", 
    "3e":"<F5>", "3f":"<F6>", "40":"<F7>", "41":"<F8>", "42":"<F9>", 
    "43":"<F10>", "44":"<F11>", "45":"<F12>"
}

# 定义按住Shift键时的按键映射字典，键是按键的16进制编码，值是对应的字符
shiftKeys = {
    "04":"A", "05":"B", "06":"C", "07":"D", "08":"E", "09":"F", 
    "0a":"G", "0b":"H", "0c":"I", "0d":"J", "0e":"K", "0f":"L", 
    "10":"M", "11":"N", "12":"O", "13":"P", "14":"Q", "15":"R", 
    "16":"S", "17":"T", "18":"U", "19":"V", "1a":"W", "1b":"X", 
    "1c":"Y", "1d":"Z", "1e":"!", "1f":"@", "20":"#", "21":"$", 
    "22":"%", "23":"^","24":"&","25":"*","26":"(","27":")",
    "28":"<RET>", "29":"<ESC>", "2a":"<DEL>", "2b":"\t", "2c":"<SPACE>", 
    "2d":"_", "2e":"+", "2f":"{", "30":"}", "31":"|", "32":"<NON>", 
    "33":"\"", "34":":", "35":"<GA>", "36":"<", "37":">", "38":"?", 
    "39":"<CAP>", "3a":"<F1>", "3b":"<F2>", "3c":"<F3>", "3d":"<F4>", 
    "3e":"<F5>", "3f":"<F6>", "40":"<F7>", "41":"<F8>", "42":"<F9>", 
    "43":"<F10>", "44":"<F11>", "45":"<F12>"
}

# 主函数
def main():
    # 检查命令行参数数量
    if len(sys.argv) != 2:
        print("Usage : ")
        print("        python UsbKeyboardHacker.py data.pcap")
        print("Tips : ")
        print("        To use this python script , you must install the tshark first.")
        print("        You can use `sudo apt-get install tshark` to install it")
        print("Author : ")
        print("        WangYihang <wangyihanger@gmail.com>")
        print("        If you have any questions , please contact me by email.")
        print("        Thank you for using.")
        exit(1)  # 如果参数数量不正确，输出使用方法并退出

    # 获取pcap文件的路径
    pcapFilePath = sys.argv[1]
    
    # 使用tshark命令提取pcap文件中的USB数据，并将结果保存到DataFileName中
    os.system("tshark -r %s -T fields -e usb.capdata 'usb.data_len == 8' > %s" % (pcapFilePath, DataFileName))

    # 读取提取的数据
    with open(DataFileName, "r") as f:
        for line in f:
            presses.append(line[0:-1])  # 去掉每行末尾的换行符，并将其存入presses列表中

    # 处理提取的数据
    result = ""  # 初始化存储结果的字符串
    for press in presses:
        if press == '':  # 如果该行是空的，跳过
            continue
        if ':' in press:  # 如果按键数据包含冒号
            Bytes = press.split(":")  # 将其分割成字节列表
        else:  # 否则
            Bytes = [press[i:i+2] for i in range(0, len(press), 2)]  # 每两个字符一组，分割成字节列表
        
        # 检查是否按下普通按键
        if Bytes[0] == "00":
            if Bytes[2] != "00" and normalKeys.get(Bytes[2]):
                result += normalKeys[Bytes[2]]  # 如果找到匹配的普通按键，将其添加到结果字符串中
        
        # 检查是否按下了Shift键
        elif int(Bytes[0],16) & 0b10 or int(Bytes[0],16) & 0b100000:
            if Bytes[2] != "00" and normalKeys.get(Bytes[2]):
                result += shiftKeys[Bytes[2]]  # 如果找到匹配的Shift按键，将其添加到结果字符串中
        
        else:
            print("[-] Unknow Key : %s" % (Bytes[0]))  # 如果按键不匹配已知的按键类型，输出提示信息
    
    print("[+] Found : %s" % (result))  # 输出最终的结果字符串

    # 删除临时生成的文件
    os.system("rm ./%s" % (DataFileName))


# 检查是否作为主程序运行
if __name__ == "__main__":
    main()  # 调用主函数
