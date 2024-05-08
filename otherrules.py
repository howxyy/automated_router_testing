import requests
import json
import time
import paramiko
import socket

#this file contains the code with other miscellaneous rules that are being triggered during the test

from pathlib import Path
from paramiko.ssh_exception import NoValidConnectionsError

def testSSHSuccessfulRule(headers, url, rule , router1_password, router1_ip):
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        host=router1_ip; port="22"; user="root"; pwd=router1_password
        event="SSH"
        eventMark="succeeded"
        rule["data"]["event"] = event
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        print("Testing rule")
        time.sleep(2)
        time.sleep(1)
        ssh.connect(host,port,user,pwd,timeout=5)
        ssh.close()
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except paramiko.AuthenticationException as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except NoValidConnectionsError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except socket.gaierror as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except TimeoutError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testSSHFailedRule(headers, url, rule, router1_ip):
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        host=router1_ip; port="22"; user="root"; pwd="1234"
        event="SSH"
        eventMark="bad"
        rule["data"]["event"] = event
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        print("Testing rule")
        time.sleep(2)
        time.sleep(1)
        ssh.connect(host,port,user,pwd,timeout=5)
        ssh.close()
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except paramiko.AuthenticationException:
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return True, event_info
    except NoValidConnectionsError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except socket.gaierror as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except TimeoutError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
        
def testWebUISuccessfulRule(headers, url, rule, router1_name, router1_password):
    try:
        login_file_path = Path(__file__).parent / "login.json"
        with open(login_file_path) as f:
            login = json.load(f)
        login["apilogin"]["username"] = router1_name
        login["apilogin"]["password"] = router1_password
        event="Web UI"
        eventMark="Password auth succeeded"
        rule["data"]["event"] = event
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        print("Testing rule")
        time.sleep(2)
        requests.post(f"{url}login",json=login["apilogin"],timeout=5).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testWebUIFailedRule(headers, url, rule, router1_name):
    try:
        login_file_path = Path(__file__).parent / "login.json"
        with open(login_file_path) as f:
            login = json.load(f)
        login["apilogin"]["username"] = router1_name
        login["apilogin"]["password"] = "1234"
        event="Web UI"
        eventMark="Bad password attempt"
        rule["data"]["event"] = event
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        print("Testing rule")
        time.sleep(2)
        requests.post(f"{url}login",json=login["apilogin"],timeout=5)
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info

def testMobileConnectionConnectedRule(headers, url, rule):
    try:
        event="Mobile Data"
        eventMark="data connected"
        rule["data"]["event"] = event
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        print("Testing rule")
        time.sleep(2)
        config = rule[f"{event}"]; requests.post(f"{url}mobile/modems/actions/restart_connection",json=config, headers=headers).raise_for_status()
        print("Rebooting modem(This may take up to 10-15 seconds)")
        time.sleep(15)
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testMobileConnectionDisconnectedRule(headers, url, rule):
    try:
        event="Mobile Data"
        eventMark="data disconnected"
        rule["data"]["event"] = event
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        print("Testing rule")
        time.sleep(2)
        config = rule[f"{event}"]; requests.post(f"{url}mobile/modems/actions/restart_connection",json=config, headers=headers).raise_for_status()
        print("Rebooting modem(This may take up to 10-15 seconds)")
        time.sleep(15)
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info