import nmap


print('-----------------#-------------------')
scanner=nmap.PortScanner()
print('Waiting For IP... ')
ip_address=input('Enter the IP: ')
x=False
while x==False:
    print('Checking the IP... '+ip_address)
    x1=input('Y/N: ')
    if x1== 'Y':
        x=True
    elif x1=='N':
        ip_address=input('Enter the IP again: ')
    else:
        print('Something went wrong..!')

user_input=input(""" \n ScanType :
                     a)TCP SCAN ( SYN )
                     b)UDP Scan
                     c)TCP Comprehensive Scan\n""")


print("You have chose: ", user_input)
ports=input('How many PORTS do you wanna scan: ')
if user_input == 'a':  
    scanner.scan(ip_address, '1-{}'.format(ports), '-v -sS')
    print(scanner.scaninfo())
    print('Status: ', scanner[ip_address].state)
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ",scanner[ip_address]['tcp'].keys())
elif user_input=='b':
    scanner.scan(ip_address,'1-{}'.format(ports),'-v -sU')
    print(scanner.scaninfo())
    print('Status: ', scanner[ip_address].state)
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ",scanner[ip_address]['udp'].keys())
elif user_input=='c':
    scanner.scan(ip_address,'1-{}'.format(ports),'-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print('Status: ', scanner[ip_address].state)
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ",scanner[ip_address]['tcp'].keys())
else:
    print('Something went wrong... ')


    






