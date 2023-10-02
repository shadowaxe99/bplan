```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.config import config

def send_email(to_address, subject, body):
    msg = MIMEMultipart()
    msg['From'] = config['EMAIL_ADDRESS']
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config['EMAIL_ADDRESS'], config['EMAIL_PASSWORD'])
    text = msg.as_string()
    server.sendmail(config['EMAIL_ADDRESS'], to_address, text)
    server.quit()
```