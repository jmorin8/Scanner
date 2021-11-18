#
# Functions
#

import socket
import sys
import logging
import nmap
from datetime import datetime
import glob
from pyhunter import PyHunter
import getpass
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import subprocess



logging.basicConfig(filename='logs.log',format='%(asctime)s %(message)s' )
log = logging.getLogger()
log.setLevel(logging.DEBUG)

topPorts_report = list()

def portScan_top(target_ : str):
    log.info('Initializing port scan (top-ports)')
    top = 10
    ports= 1024

    print(f'[>] PortScan  |  Top-ports: {top}-{ports}  | Target:{target_}')

    try:
        host = socket.gethostbyname(target_)

        try:
            print(f'[>] Scanning: {host}')
            print(f'[>] Started at: {datetime.now()}')
            for ports in range(top,ports+1):
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

                connection = s.connect_ex((host,ports))
                s.settimeout(1)

                if connection==0:
                    openPort = f'\t[>] Port:{ports} open'
                    topPorts_report.append(openPort)
                    print(openPort)

                s.close()

            try:
                log.info('[>] Creating report')
                print('[>] Creating report')

                with open('topPorts_report.txt', 'a') as tp_report:
                    for element in topPorts_report:
                        tp_report.write(element)
                    tp_report.close()

                log.info('[>] Report Succesfully created')
            except KeyboardInterrupt:
                log.info('Keyboard interrupt')
                print('[ERROR] Keyboard interrupt, quiting..')

        except KeyboardInterrupt:
            log.info('Keyboard interrupt')
            print('[ERROR] Keyboard interrupt, quiting..')
            sys.exit()

        log.info('Succesfully scanned (top-ports)')
    except socket.gaierror as err:
        log.info(err)
        print('[ERROR]',err)


def portScan_full(target : str):
    log.info('Initializing port scan (full scan)')
    print(f'[>] PortScan  |  full scan  | Target:{target}')
    print(f'[>] Started at: {datetime.now()}')

    try:
        scanner = nmap.PortScanner()
        try:
            host_scan = scanner.scan(hosts=target, arguments='-Pn -sV -sS', sudo=True)
            print(f'\t[>] Executing: {scanner.command_line()}')

            scan_result = host_scan['scan'][f'{target}']['tcp']

            for key,value in scan_result.items():
                if isinstance(value, dict):
                    print(f'\t[>] Port:{key}')
                    for k,v in value.items():
                        print(f'\t\t- {k} : {v}')

            log.info('[>] Creating report')
            try:
                print('[>] Creating report')

                with open('fulScan_report.txt', 'a') as fs_report:
                    for key,value in scan_result.items():
                        if isinstance(value, dict):
                            fs_report.write(f'[>] Port:{key}\n')
                            for k,v in value.items():
                                fs_report.write(f'\t- {k} : {v}\n')

                    fs_report.close()
            except KeyboardInterrupt:
                log.info('Keyboard interrupt')
                print('[ERROR] Keyboard interrupt, quiting..')

            log.info('[>] Report succesfully created')

        except NmapExecutionError as err:
            logging.info(err)
            print('[ERROR]',err)

    except KeyboardInterrupt:
        log.info('Keyboard interrupt')
        print('[ERROR] Keyboard interrupt, quiting..')
        sys.exit()


def verify_email(email: str):
    try:
        api_key= "209d36b4c56d9be448c264aa19ebf3dea5052740"
        hunter = PyHunter(api_key=api_key)

        result = hunter.email_verifier(email, raw=False)

        if result['result'] != 'undeliverable':
            return True
        else:
            print('[>] Not a valid email\n')
            return False

    except KeyboardInterrupt:
        log.info('Keyboard interrupt')
        print('[ERROR] Keyboard interrupt, quiting..')
        sys.exit()


def send_reports():
    try:
        option = input('[>] Do you want to send created reports? [y/n]: ')

        while not option in ('y', 'Y', 'n', 'N'):
            print('[>] Enter a valid option!!\n')
            option = input('[>] Do you want to send created reports? [y/n]: ')

        if option in ('y', 'Y'):
            log.info('User accepted to send emails')
            try:
                usr = input('[>] Enter your email: ')

                while verify_email(usr) == False:
                    usr = input('[>] Enter your email: ')
                    verify_email(usr)

                password = getpass.getpass('[>] Enter your password: ')
                to = input('[>] Who do you want to send the report?: ')

                while verify_email(to) == False:
                    usr = input('[>] Enter your email: ')
                    verify_email(usr)

                subject= input('[>] Type email subject: ')
                message_ = input('[>] What do you want to send as message: ')

                log.info('Sendind email..')
                print('[>] Sendind email..')
                try:
                    msg = MIMEMultipart('alternative')
                    msg['From'] = usr
                    msg['To'] = to
                    msg['Subject'] = subject

                    html = f"""
                    <html>
                    <body>{message_}</body>
                    <html>
                    """
                    body = MIMEText(html, 'html')
                    msg.attach(body)

                    files = glob.glob('*.txt')
                    file = files[0]

                    with open(file, 'rb') as fl:
                        img_obj = MIMEBase('application', 'octet-stream')
                        img_obj.set_payload(fl.read())

                    encoders.encode_base64(img_obj)
                    img_obj.add_header('Content-Disposition', 'attachment; filename= %s' %file)
                    msg.attach(img_obj)

                    fullmessage = msg.as_string()

                    context = ssl.create_default_context() # Create a secure SSL context
                    port = 465
                    server = "smtp.gmail.com"

                    try:
                        with smtplib.SMTP_SSL(server,port, context=context) as server:
                            server.login(usr,password)
                            server.sendmail(usr, to, fullmessage)

                        server.close()
                        log.info('Succesfully sent')
                        print('[>] Succesfully sent')
                    except:
                        print('[ERROR] Something went wrong')

                except:
                    log.info('Something went wrong while sending email')
                    print('[>] Something went wrong while sending email')

            except KeyboardInterrupt:
                print('[ERROR] Keyboard interrupt, quiting..')

        elif option in ('n', 'N'):
            log.info('User does not accepted to send emails, quiting..')
            print('[>] Quiting..')
            sys.exit()

    except KeyboardInterrupt:
        print('[ERROR] Keyboard interrupt, quiting..')


def search_hidden(target: str):
    log.info('Searching hidden files')
    print(f'[>] Search Hiddenn  |  searcHidden.sh  | Target:{target}')

    try:
        try:
            subprocess.check_call( ["./searcHidden %s" %target], shell=True)

        except subprocess.CalledProcessError as err:
            log.info(err)
            print(err)
    except KeyboardInterrupt:
        print('[>] Keyboard interrupt')
