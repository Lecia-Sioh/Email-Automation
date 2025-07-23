import smtplib
from email.message import EmailMessage

# Email content
msg = EmailMessage()
msg['Subject'] = 'Test Email from Python'
msg['From'] = 'siohlecia@gmail.com'
msg['To'] = 'leciasioh@gmail.com'
msg.set_content('Hello! This email was sent using Python 😄')

file_path = "C:\\Users\\Lecia\\Desktop\\Lecia's team\\pge.py" # 🔁 Change this to your filename
with open(file_path, 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)


# Gmail server setup
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('siohlecia@gmail.com', 'hvfrkwvohaetldml')
server.send_message(msg)
server.quit()
