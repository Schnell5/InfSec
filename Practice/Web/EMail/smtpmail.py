import smtplib
import email.utils
import sys
import mailconfig
import getpass


mailserver = mailconfig.smtpservername

From = input('From: ').strip()
To = input('To: ').strip()
Tos = To.split(';')
Subj = input('Subject: ').strip()
Date = email.utils.formatdate()

text = 'From: {0}\nTo: {1}\nDate: {2}\nSubject: {3}\n\n'.format(From, To, Date, Subj)

"""
Uncomment the string below and comment the previous one. Then type "To: fakeaddr" followed by an empty string in the 
message body. As result: fakeaddr will be in the "To:" field, but the message will be sent to the real recipient
"""
# text = 'From: {0}\nDate: {1}\nSubject: {2}\n'.format(From, Date, Subj)

print('Type message text, end with line=[Ctrl+d (Unix), Ctrl+z (Windows)]')
while True:
    line = sys.stdin.readline()
    if not line:
        break       # Exit (Ctrl+d/z)
    text += line

print('Connecting...')
server = smtplib.SMTP(mailserver)
#server.login(mailconfig.smtpusername, getpass.getpass('Password:'))    # If authentication required
failed = server.sendmail(From, Tos, text)
server.quit()

if failed:
    print('Failed recipients:', failed)
else:
    print('No errors')
print('Bye.')
