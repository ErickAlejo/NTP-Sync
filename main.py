from netmiko import ConnectHandler
import re

# Read IPs Files
with open("hosts.txt", "r") as hosts:
    host = []
    for a in hosts:
        a = a.strip() # Remover /n
        host.append(a)
host = host

# Create Object to connect with Netmiko
devices =[{
    'device_type': 'mikrotik_routeros',
    'host': ips,
    'username': 'admin',
    'password': 'admin'
    }
    for ips in host
]

# Commands to Execute in routers depend it V6 & V7
templates = {
    "check" : ['system routerboard print'
               ],
     'V6':{
        "post_config" :["/system ntp client set primary-ntp=X.X.X.X secondary-ntp=X.X.X.X ", #  <-- Change by your Server IP Adress
                        "/system clock set time-zone-name=America/Bogota"
                        ],
    },    
    'V7':{
        "clean_config" :["/system/ntp/client/servers remove [find]",
                        "/system clock set time-zone-name=America/Bogota"
                        ],
        "post_config" : [
                        "/system ntp client set enabled=yes",
                        "/system ntp client servers add address=X.X.X.X", # <-- Change by your Server IP Adress
                        "/system ntp client servers add address=X.X.X.X." # <-- Change by your Server IP Adress
                        ]
    }

}


# Connect and Execute Command
for device in devices:
    try:
        net_connect = ConnectHandler(**device)
        print('\n')
        print(f'Host {device['host']}')
        for commands in templates['check']:
            output = net_connect.send_command(commands)
            regex_ver7 = r'upgrade-firmware: (7\..+)'
            regex_ver6 = r'upgrade-firmware: (6\..+)'
            if  re.findall(regex_ver7,output):
                print('Version 7')
                for commands in templates['V7']['clean_config']:
                    print(f"X  Deleting Config: '{commands}'")
                    output = net_connect.send_command(commands,read_timeout=40)
                for commands in templates['V7']['post_config']:
                    print(f"✓  Reconfig: '{commands}'")
                    output = net_connect.send_command(commands,read_timeout=40)   
            elif re.findall(regex_ver6,output):
                    print('Version 6')
                    for commands in templates['V6']['post_config']:
                        print(f"✓  Reconfig: '{commands}'")
                        output = net_connect.send_command(commands,read_timeout=40) 
            else:
                print(output)
    except ConnectionRefusedError as err:
        print(f"Connection Refused: {err}")
    except TimeoutError as err:
        print(f"Connection Refused: {err}")
    except Exception as err:
        exception_type = type(err).__name__
        print(exception_type)
        

    # Close All connections to Routers
    net_connect.disconnect()

