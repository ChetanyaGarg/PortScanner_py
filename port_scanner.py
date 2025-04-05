import socket
import termcolor

def scanning(ipaddress,port):
    print(termcolor.colored("/n" + "Starting Scan For IP : " + str(ipaddress),'blue'))
    for i in range(1,port+1):
        scan_port(ipaddress,i)

def scan_port(ipaddress,port):
    try:
        sock=socket.socket()
        sock.settimeout(2)
        sock.connect((ipaddress,port))
        print(termcolor.colored("[+] Port Open " + str(port),'green'))
        sock.close()
    except:
        print(termcolor.colored("[-] Port Closed " + str(port),'red'))

target = input("[*] Enter The Targets To Scan (seprate the range of ip with { , } ): ")
Port=int(input("[*] Enter Till Which Port Do You Want To Scan : "))
if ',' in target:
    print(termcolor.colored("[*] Scanning Multiple Targets ->",'blue'))
    for addr in target.split(','):
        scanning(addr.strip(" "), Port)
else:
    scanning(target,Port)
