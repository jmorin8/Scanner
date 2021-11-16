``` 
================================================== 
 ____
/ ___|   ___   __ _  _ __   _ __    ___  _ __
\___ \  / __| / _` || '_ \ | '_ \  / _ \| '__|
 ___) || (__ | (_| || | | || | | ||  __/| |
|____/  \___| \__,_||_| |_||_| |_| \___||_|                           
================================================== 
Made by: jmorin8
```

![for the badge_made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)
# :desktop_computer::mag: Scanner
Scanner is a python tool to automate tasks while auditing a target, such as port scanning and search hidden files/directories in a website.


# :book: Content 
* [Installation](#Installation)
    * Linux | Unix
    * Wordlists
    * Gobuster
* [How_to_use?](#How-to-use?)
    * Options
      * PortScan
      * Search Hidden
 * [Reports](#Reports)
 * [Logs](#Logs)


# :hammer_and_wrench: Installation
**Important: linux | unix env, python 3.9.1, wordlists, gobuster**
 
### Linux & Unix
```
$ git clone https://github.com/jmorin8/Scanner
$ cd Scanner
$ pip3 install -r requirements.txt
$ chmod +x searcHidden
```

### Wordlists
Wordlist are a file that contains a set of values that the attacker requires to provide to test a mechanism, you can download some from [SecLists](https://github.com/danielmiessler/SecLists) or you can just clone the entire repository
```
$ git clone https://github.com/danielmiessler/SecLists
$ cd SecLists/Discovery/Web-Content # Wordlists for web-content discovery are under this path
```

### Gobuster
You must have got gobuster by default in your linux env, if don´t just run the next command
```
$ sudo apt intall gobuster 
```


# :question: How to use?
A the beggining you can deploy the menu executing the command `python3 scanner.py -h | --help` to see the available options 
```
==================================================
 ____
/ ___|   ___   __ _  _ __   _ __    ___  _ __
\___ \  / __| / _` || '_ \ | '_ \  / _ \| '__|
 ___) || (__ | (_| || | | || | | ||  __/| |
|____/  \___| \__,_||_| |_||_| |_| \___||_|


Made by: jmorin8
Repo: https://github.com/jmorin8/Scanner
================================================== 
usage: main.py [option] [-t|--target] target

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        IP target | url to test        
  -p, --portScan        Perform a port scan to target  
  -tp, --topPorts       Scan well-kwnon ports
  -f, --fullScan        Perform advance port scanning  
  -s, --searchHidden    Search hidden files in a target
```

## Options
### PortScan
* Top ports
<br>This option will call `portScan_top` function which will check for [well-known](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers#Well-known_ports) ports state, all this done by using sockets, for every well-known port will create a connection then closed it if port is open will display the port number on screen, to execute this option:</br>
```
$ python3 scanner.py --portScan --target 127.0.0.1 --topPorts 

==================================================
 ____
/ ___|   ___   __ _  _ __   _ __    ___  _ __
\___ \  / __| / _` || '_ \ | '_ \  / _ \| '__|
 ___) || (__ | (_| || | | || | | ||  __/| |
|____/  \___| \__,_||_| |_||_| |_| \___||_|


Made by: jmorin8
Repo: https://github.com/jmorin8/Scanner
==================================================       
[>] PortScan  |  Top-ports: 0-1024  | Target:127.0.0.1
[>] Scanning: 127.0.0.1
[>] Started at: 2021-11-15 23:01:21.512590
        [>] Port:22 open
        [>] Port:80 open
```


* Full Scan
<br> This options will call `portScan_full` function which use nmap module to perform a andvance scan such as OS detection, service name and status and product and version and more</br>
```
$ python3 scanner.py --portScan --target 127.0.0.1 --fullScan

==================================================
 ____
/ ___|   ___   __ _  _ __   _ __    ___  _ __     
\___ \  / __| / _` || '_ \ | '_ \  / _ \| '__|    
 ___) || (__ | (_| || | | || | | ||  __/| |       
|____/  \___| \__,_||_| |_||_| |_| \___||_|       


Made by: jmorin8
Repo: https://github.com/jmorin8/Scanner
==================================================
[>] PortScan  |  full scan  | Target:127.0.0.1
[>] Started at: 2021-11-15 23:15:10.866612        
        [>] Executing: nmap -oX - -Pn -sV -sS 127.0.0.1
        [>] Port:22
                - state : open
                - reason : syn-ack
                - name : ssh
                - product : OpenSSH
                - version : 8.2p1 Ubuntu 4ubuntu0.2     
                - extrainfo : Ubuntu Linux; protocol 2.0
                - conf : 10
                - cpe : cpe:/o:linux:linux_kernel       
        [>] Port:80
                - state : open
                - reason : syn-ack
                - name : http
                - product : Apache httpd
                - version : 2.4.41
                - extrainfo : (Ubuntu)
                - conf : 10
                - cpe : cpe:/a:apache:http_server:2.4.41
```


### Search Hidden
This options will call `search_hidden` function which use the module subprocess to call a bash script that use gobuster and search for hidden files in a website
```
$ python3 scanner.py --searchHidden --target https://example.com  

==================================================
 ____
/ ___|   ___   __ _  _ __   _ __    ___  _ __     
\___ \  / __| / _` || '_ \ | '_ \  / _ \| '__|    
 ___) || (__ | (_| || | | || | | ||  __/| |       
|____/  \___| \__,_||_| |_||_| |_| \___||_|       


Made by: jmorin8
Repo: https://github.com/jmorin8/Scanner
==================================================
[>] Search Hiddenn  |  searcHidden.sh  | Target: https://example.com
```
<br>The bash script will ask you for a wordlist to use and for the file extensions you want to search on the target </br>
```
[>] Path of the wordlist to use: /home/User/wordlists/wordlists.txt
[>] File extensions to search seppareted by commas, example(txt,hmtl,php): txt,php
[>] Searching, to stop it ctrl+z
```


# :file_folder: Reports
Every option you execute at the end will create a report in a `txt` file which will have all the results of the execution then will ask you if you want to send it, if you accept the program will ask you for a `gmail` account then will ask for your password (at the moment you write it, will be hidden), a destination which could be your friend´s email, email subject and a message you want to send as a body email, otherwise the program will finish
``` 
[>] Creating report
[>] Do you want to send created reports? [y/n]: y
[>] Enter your email: your_email@gmail.com
[>] Enter your password: your_password 
[>] Who do you want to send the report?: destinantion@example.comm
[>] Type email subject: Example
[>] What do you want to send as message: This is just an example
[>] Sendind email..
[>] Succesfully sent
```
:warning: **IMPORTANT** :warning: If you accept to send reports you must create your own apiKey at [hunter](https://hunter.io/) and change line 129 from `functions.py` for your apkikey
```
line 129 api_key= "yourApiKey"
```
if you want to ignore this part of the project remove lines 42 and 45 from `scanner.py`
```
line 42 functions.send_reports()
line 45 functions.send_reports()

```

# :bookmark_tabs: Logs
Logs are a detailed list of an application information, system performance, or user activities, in this project we use them to get a registrer of user activities. Every event and option you use will be saved in a `log` file, at the end of each execution you can check the `log` file to see how the events were registered and if the project fail will show you in what it fails, the file may look like this
```
2021-11-16 00:47:34,837 Initializing port scan (full scan)
2021-11-16 00:47:56,854 [>] Creating report
2021-11-16 00:47:56,856 [>] Report succesfully created
2021-11-16 00:47:58,807 User accepted to send emails
2021-11-16 00:48:01,414 Starting new HTTPS connection (1): api.hunter.io:443
2021-11-16 00:48:01,896 https://api.hunter.io:443 "GET /v2/email-verifier?email=testttpec4%40gmail.com&api_key=yourApiKey HTTP/1.1" 200 None
2021-11-16 00:48:15,507 Starting new HTTPS connection (1): api.hunter.io:443
2021-11-16 00:48:15,984 https://api.hunter.io:443 "GET /v2/email-verifier?email=javier.morin_ortiz%40hotmail.com&api_key=yourApiKey HTTP/1.1" 200 None
2021-11-16 00:48:23,368 Sendind email..
2021-11-16 00:48:24,845 Succesfully sent
```
