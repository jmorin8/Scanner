<br>![image](https://user-images.githubusercontent.com/54748637/141711816-1cccdb05-a104-458d-b1c0-34f96f9f0df9.png)</br>
![for the badge_made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)
# Scanner

Scanner is a python tool to automate tasks while doing audits to a target 

# Content
* [Installation](#Installation)
* [Usage](#Usage)
  * [Menu](#Scanner-menu)
  * [Options](#Options)
    * PortSan
    * Search hiddem


# Installation
**Important: python 3.9.1, wordlists, linux | unix env**

## Linux & Unix
```
$ git clone https://github.com/jmorin8/Scanner
$ cd Scanner
$ pip3 -r requirements.txt
$ chmod +x searcHidden
```
## Wordlists
Wordlist are a file that contains a set of values that the attacker requires to provide to test a mechanism, you can download some from [SecLists](https://github.com/danielmiessler/SecLists)


# Usage
## Scanner menu
```
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
```
$ python3 scanner.py --portScan --target 127.0.0.1 --fullScan 
```
or 
```
$ python3 scanner.py --portScan --target 127.0.0.1 --topPorts 

```

### Search Hidden
```
$ python3 scanner.py --searchHidden --target https://example.com  
```
