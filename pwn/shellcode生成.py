from pwn import *

# 设置架构为 x86_64
context(arch='amd64', os='linux')

# 生成 execve("/bin/sh") 的 shellcode
shellcode = asm(shellcraft.sh())

# 输出生成的 shellcode
print(shellcode)