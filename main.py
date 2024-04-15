import os
import re
import json
from pprint import pprint
from netmiko import ConnectHandler
from dotenv import dotenv_values
from colorama import init, Fore, Back, Style


# Get File .env
config = dotenv_values(".env")
var_env = dict(config)


class ValidatorOfFilesJSON():
    global valid_keys
    valid_keys = ['router','description','execution_commands']

    def validate_keys(file):
        try:
            keys_in_json = dict(file).keys()
            for a in keys_in_json:
                if a in valid_keys:
                    continue
                else:
                    print('Only allowed this keys in json file', valid_keys)
                    return False    
            return file
        except Exception as e:
            print('Error')

    def validate_value_of_keys(file):
        for a in file:
            pointer_value = file.get(a)
            if isinstance(pointer_value,str) or isinstance(pointer_value,dict) :
                continue
            elif len(pointer_value) > 0:
                continue
            else:
                print('Data Invalid')

class HandleFiles:
    """
    Open, edit or create new Files JSON
    EX : HandleFiles('./templates/template.json').AnyMethod()
    """
    def open_json_files(fileJson):
        #Open A File JSON -> EX: HandleFiles(PATH-TO-FILE.json).open_json_files()

        try:
            # Validate Exist File and PATH
            if len(fileJson) > 0 and os.path.exists(fileJson):
                with open(fileJson, "r") as datas:
                    data  = json.load(datas)
                    #pprint(data)
                return data
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print('Require PATH and file json')

    def open_txt_files(fileTxt):
        try:
            # Validate Exist File and PATH
            if len(fileTxt) > 0 and os.path.exists(fileTxt):
                with open(fileTxt, "r") as datas:
                    hosts = []
                    for a in datas:
                        host = a.strip("\n")
                        hosts.append(host)
                return hosts
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print('Require PATH and file json')

class RouterMikrotik():
    def __init__(self,host,template,user,passwd):
        self.host = host
        self.template = template
        self.user = user
        self.passwd = passwd
    
    def connectSsh(self):
        try:        
            version7_regexp = r'^7\.\d+\.\d+$'
            version6_regexp = r'^6\.\d+\.\d+$'

            hosts = HandleFiles.open_txt_files(self.host)
            devices = [{
            'device_type': 'mikrotik_routeros',
            'host': ips,
            'username':self.user,
            'password':self.passwd,
            }
                for ips in hosts
            ]

            for device in devices:
                version = self.template['execution_commands']['first-check-version']
                net_connect = ConnectHandler(**device)
                output = net_connect.send_command(version,use_textfsm=True,read_timeout=20.5)
                
                # Get Current Firmware
                current_firmware = output[0]['current_firmware']
                
                # IF V7
                if re.match(version6_regexp,current_firmware):
                    for x in self.template['execution_commands']['then-if-router-v6']:
                        output = net_connect.send_command(str(x),read_timeout=20.5)
                    print(Fore.GREEN + Style.BRIGHT + f"Completed 💚 - IP: {device['host']}  Version: {current_firmware}")
                    Style.RESET_ALL

                #IF V6
                elif re.match(version7_regexp,current_firmware):
                    for x in self.template['execution_commands']['then-if-router-v7']:
                        output = net_connect.send_command(str(x),read_timeout=20.5)
                    print(Fore.GREEN + Style.BRIGHT + f"Completed 💚 - IP: {device['host']}  Version: {current_firmware}")
                else:
                    print(Fore.RED + Style.BRIGHT + f"Version Unknown: {current_firmware}  IP: {device['host']}")

        except Exception as e:
            print(Fore.RED + Style.BRIGHT + f"Error on IP: {device['host']}  Version:{current_firmware}")


jsonfile = HandleFiles.open_json_files('./templates/ntp-reconfig.template.json')
ValidatorOfFilesJSON.validate_keys(jsonfile)
ValidatorOfFilesJSON.validate_value_of_keys(jsonfile)
RouterMikrotik('./hosts.txt',jsonfile,var_env['USER_MK'],var_env['PASS_MK']).connectSsh()