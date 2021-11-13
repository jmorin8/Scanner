# Main nombre por definir 

import functions
import argparse
from art import *



if __name__=='__main__':
    print("="*50)
    print( text2art('Scanner') )
    print('Made by: jmorin8 (j0r38)')
    print('repo: https:github.com/jmorin8/Scanner')
    print("="*50)

    parser = argparse.ArgumentParser(usage='main.py [option] [-t|--target] target' )
    parser.add_argument('-t', '--target', help='IP target | url to test', required=True)
    
    parser.add_argument('-p', '--portScan', help='Perform a port scan to target', action="store_true")
    
    parser.add_argument('-tp', '--topPorts', help="Scan well-kwnon ports", action='store_true')
    parser.add_argument('-f', '--fullScan', help="path of wordlist that will be used example: [-w | --wordlist] [/home/wordlist/wordlist.txt | C:/User/wordlist/wordlist.txt)]", action='store_true')


    params = parser.parse_args()

    # OPTIONS 
    op_portScan = params.portScan

    # Complements
    topPorts = params.topPorts
    fullScan = params.fullScan

    # Required
    target_ = params.target

    if op_portScan and topPorts:
        functions.portScan_top(target_)
        functions.send_reports()
    elif op_portScan and fullScan:
        functions.portScan_full(target_)
        functions.send_reports()
    