from pwn import *

# ���üܹ�Ϊ x86_64
context(arch='amd64', os='linux')

# ���� execve("/bin/sh") �� shellcode
shellcode = asm(shellcraft.sh())

# ������ɵ� shellcode
print(shellcode)