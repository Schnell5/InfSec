import poplib
import getpass
import sys
import mailconfig


mailserver = mailconfig.popservername
mailuser = mailconfig.popusername
mailpasswd = getpass.getpass('Password: ')

print('Connecting...')
server = poplib.POP3_SSL(mailserver)
server.user(mailuser)
server.pass_(mailpasswd)

try:
    print(server.getwelcome())
    msgCount, msgBytes = server.stat()
    print('There are {0} mail messages in {1} bytes'.format(msgCount, msgBytes))
    print(server.list())
    print('-' * 80)
    input('[Press Enter key]')

    for i in range(2):
        hdr, message, octets = server.retr(i+1)
        for line in message:
            print(line.decode())
        print('-' * 80)
        if i < 1:
            input('[Press Enter key]')
finally:
    server.quit()
print('Bye')
