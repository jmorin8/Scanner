#
# Functions
#

import socket
import sys
import logging
import nmap
from nmap3.exceptions import NmapExecutionError  
from datetime import datetime
import os
import requests
import wget

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
            except KeyboardInterrupt:
                log.info('Keyboard interrupt')
                print('[ERROR] Keyboard interrupt, quiting..')
        
        except KeyboardInterrupt:
            log.info('Keyboard interrupt')
            print('[ERROR] Keyboard interrupt, quiting..')
            sys.exit()
    
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
            host_scan = scanner.scan(hosts=target, arguments='-Pn -sV -sS')
            print(f'\t[>] Executing: {scanner.command_line()}')

            scan_result = host_scan['scan'][f'{target}']['tcp']
            
            for key,value in scan_result.items():
                if isinstance(value, dict):
                    print(f'\t[>] Port:{key}')
                    for k,v in value.items():
                        print(f'\t\t- {k} : {v}')
            
            try:
                log.info('[>] Creating report')
                print('[>] Creating report')

                with open('fulScan_report.txt', 'a') as fs_report:
                    for key,value in scan_result.items():
                        if isinstance(value, dict):
                            fs_report.write(f'\t[>] Port:{key}')
                            for k,v in value.items():
                                fs_report.write(f'\t\t- {k} : {v}')

                    fs_report.close()
                        
            except KeyboardInterrupt:
                log.info('Keyboard interrupt')
                print('[ERROR] Keyboard interrupt, quiting..')       

        except NmapExecutionError as err:
            logging.info(err)
            print('[ERROR]',err)
    
    except KeyboardInterrupt:
        log.info('Keyboard interrupt')
        print('[ERROR] Keyboard interrupt, quiting..')
        sys.exit()



def send_reports():
    option = input('[>] Do you want to send created reports? [y/n]: ')