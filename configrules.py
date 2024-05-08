import requests
import json
import time

#This file contains code with all the configuration rules that are being triggered during the test

def testConfigAllRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "all"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        time.sleep(2)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info


def testConfigAvlRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "avl"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule["enabled1"]; requests.put(f"{url}gps/avl/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule["enabled0"]; requests.put(f"{url}gps/avl/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info  

def testConfigButtonsRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "buttons"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}administration/buttons/config/cfg035d81",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}administration/buttons/config/cfg035d81",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info   
            
def testConfigCallUtilsRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "call_utils"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}"]; requests.post(f"{url}mobile_utilities/call_utilities/rules/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}mobile_utilities/call_utilities/rules/config/cfg0292bd",headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info 

def testConfigChilliRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "chilli"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}"]; requests.post(f"{url}hotspot/groups/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}hotspot/groups/config/cfg0246f2",headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); 
        return False, event_info 

def testConfigCLIRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "cli"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule["enable0"]; requests.put(f"{url}access_control/cli/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule["enable1"]; requests.put(f"{url}access_control/cli/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info 

def testConfigDDNSRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "ddns"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule["enabled1"]; requests.put(f"{url}ddns/config/myddns",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule["enabled0"]; requests.put(f"{url}ddns/config/myddns",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigDHCPRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "dhcp"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}"]; requests.post(f"{url}dhcp/static_leases/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}dhcp/static_leases/config/cfg04fe63",headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info

def testConfigDMVPNRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "dmvpn"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"new_id"]; requests.post(f"{url}dmvpn/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}dmvpn/config/test",headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigDropbearRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "dropbear"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}access_control/ssh/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}access_control/ssh/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigEmailToSMSRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "email_to_sms"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}mobile_utilities/sms_gateway/email_to_sms/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}mobile_utilities/sms_gateway/email_to_sms/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigEtherwakeRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "etherwake"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}wol_setup/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}wol_setup/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigEventsReportingRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "events_reporting"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        time.sleep(2)
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigFirewallRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "firewall"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}firewall/general_settings/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}firewall/general_settings/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigFstabRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "fstab"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}usb_tools/general/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}usb_tools/general/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigGPSRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "gps"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}gps/general/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}gps/general/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigHostblockRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "hostblock"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}webfilter/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}webfilter/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigIOJugglerRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "iojuggler"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}io/juggler/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}io/juggler/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigIOManRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "ioman"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}io/scheduler/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}io/scheduler/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigIpBlockedRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "ip_blockd"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}access_control/security/general/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}access_control/security/general/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigIpSecRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "ipsec"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"new_id"]; requests.post(f"{url}ipsec/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}ipsec/config/test",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigLandingPageRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "landingpage"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"landingpage"]; requests.put(f"{url}hotspot/landing/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        #requests.delete(f"{url}ipsec/config/test",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info

def testConfigModbusServerRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "modbus_server"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}modbus/tcp_server/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}modbus/tcp_server/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigModbusClientRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "modbus_client"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}modbus/main/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}modbus/main/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigModbusGatewayRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "modbusgateway"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}modbus/gateway/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}modbus/gateway/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigMosquittoBrokerRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "mosquitto"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}mqtt_broker/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}mqtt_broker/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info

def testConfigMosquittoPublisherRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "mqtt_pub"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}mqtt_pub/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}mqtt_pub/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigMultiWifiRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "multi_wifi"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}wireless/devices/config/radio0/interfaces/default_radio0",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule["enabled0"];requests.put(f"{url}wireless/devices/config/radio0/interfaces/default_radio0",json=config, headers=headers).raise_for_status()
        config=rule["enabled1"];requests.put(f"{url}wireless/devices/config/radio0/interfaces/default_radio0",json=config, headers=headers).raise_for_status()
        config=rule[f"{eventMark}0"]; requests.put(f"{url}wireless/devices/config/radio0/interfaces/default_radio0",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigMWan3Rule(headers, url, rule):
    try:
        event = "config"
        eventMark = "mwan3"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}mwan3/interfaces/config/wan",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}mwan3/interfaces/config/wan",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigNetworkRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "network"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled0"]; requests.put(f"{url}interfaces/config/wan6",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled1"]; requests.put(f"{url}interfaces/config/wan6",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigNTPClientRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "ntpclient"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled0"]; requests.put(f"{url}administration/ntp/client/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled1"]; requests.put(f"{url}administration/ntp/client/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigNTPServerRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "ntpserver"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}administration/ntp/server/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}administration/ntp/server/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigOpenVPNRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "openvpn"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}"]; requests.post(f"{url}openvpn/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}openvpn/config/test",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigOperctlRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "operctl"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"new_name"]; requests.post(f"{url}mobile/operator_lists/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}mobile/operator_lists/config/cfg0223d7",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigOverviewRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "overview"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled0"]; requests.put(f"{url}overview/config/cfg010a5c",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled1"]; requests.put(f"{url}overview/config/cfg010a5c",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigP910NDRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "p910nd"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}usb_tools/p910nd/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}usb_tools/p910nd/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigPackageRestoreRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "package_restore"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled0"]; requests.put(f"{url}package_restore/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled1"]; requests.put(f"{url}package_restore/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigPeriodicRebootRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "periodic_reboot"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}"]; requests.post(f"{url}auto_reboot/periodic/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}auto_reboot/periodic/config/cfg0210a4",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigPeriodicRebootRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "periodic_reboot"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}"]; requests.post(f"{url}auto_reboot/periodic/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}auto_reboot/periodic/config/cfg0210a4",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigPingRebootRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "ping_reboot"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enable1"]; requests.put(f"{url}auto_reboot/ping/config/cfg01c21d",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enable0"]; requests.put(f"{url}auto_reboot/ping/config/cfg01c21d",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info

def testConfigPostGetRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "post_get"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}io/post_get/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}io/post_get/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigPPTPDRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "pptpd"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"new_id"]; requests.post(f"{url}pptp/server/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}pptp/server/config/test",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigPrivoxyRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "privoxy"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}privoxy/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}privoxy/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigProfilesRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "profiles"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"new_id"]; requests.post(f"{url}profiles/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}profiles/config/test",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigQuotaLimitRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "quota_limit"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}interfaces/config/mob1s1a1",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}interfaces/config/mob1s1a1",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigRMSMQTTRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "rms_mqtt"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enable0"]; requests.put(f"{url}cloud_solutions/rms/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enable1"]; requests.put(f"{url}cloud_solutions/rms/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigRPCDRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "rpcd"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}"]; requests.post(f"{url}users/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}users/config/cfg07f8be",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
#//////////////////////Requires serial router////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def testConfigRSConsoleRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "rs_console"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"rs"]; requests.post(f"{url}console/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}console/config/1",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); print("If 422 Client Error, then router may not have serial I/O"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigRSModbusRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "rs_modbus"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}"]; requests.post(f"{url}modbus/tcp_over_serial/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}modbus/tcp_over_serial/config/1",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); print("If 422 Client Error, then router may not have serial I/O"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigRSModemRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "rs_modem"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"rs"]; requests.post(f"{url}rs_modem/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}rs_modem/config/1",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); print("If 422 Client Error, then router may not have serial I/O"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigRSOverIPRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "rs_overip"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"rs"]; requests.post(f"{url}overip/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}overip/config/1",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); print("If 422 Client Error, then router may not have serial I/O"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def testConfigFotaRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "rut_fota"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled0"]; requests.put(f"{url}fota/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled1"]; requests.put(f"{url}fota/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigSambaRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "samba"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}samba/general/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}samba/general/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigSimSwitchRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "sim_switch"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}mobile/sim_switch/config/cfg01aa0e",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}mobile/sim_switch/config/cfg01aa0e",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigSimCardRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "simcard"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}mobile/simcards/config/cfg01aa0e",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}mobile/simcards/config/cfg01aa0e",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigSMSGatewayRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "sms_gateway"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}mobile_utilities/sms_gateway/auto_reply/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}mobile_utilities/sms_gateway/auto_reply/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigSMSUtilsRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "sms_utils"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled0"]; requests.put(f"{url}mobile_utilities/sms_rules/config/cfg0192bd",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled1"]; requests.put(f"{url}mobile_utilities/sms_rules/config/cfg0192bd",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigSNMPDRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "snmpd"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}snmp/settings/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}snmp/settings/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigSNMPTrapRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "snmptrap"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}snmp/trap_settings/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}snmp/trap_settings/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigSQMRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "sqm"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"new_id"]; requests.post(f"{url}sqm/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}sqm/config/test",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigSTunnelRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "stunnel"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled1"]; requests.put(f"{url}stunnel/global/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled0"]; requests.put(f"{url}stunnel/global/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigSystemRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "system"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled0"]; requests.put(f"{url}administration/led/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled1"]; requests.put(f"{url}administration/led/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigTelnetDRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "telnetd"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enable1"]; requests.put(f"{url}access_control/telnet/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enable0"]; requests.put(f"{url}access_control/telnet/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigUHTTPDRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "uhttpd"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}access_control/webui/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}access_control/webui/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigULogdRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "ulogd"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}ulog/ftp/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}ulog/ftp/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigUserGroupsRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "user_groups"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"new_name"]; requests.post(f"{url}recipients/phone_groups/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}recipients/phone_groups/config/cfg01a6bf",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigVRRPDRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "vrrpd"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"new_id"]; requests.post(f"{url}vrrp/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}vrrp/config/test",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigWidgetRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "widget"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}widget/config/3",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}widget/config/3",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigWifiScannerRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "wifi_scanner"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}1"]; requests.put(f"{url}wireless/wifi_scanner/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"{eventMark}0"]; requests.put(f"{url}wireless/wifi_scanner/config/general",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigWirelessRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "wireless"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"enabled0"]; requests.put(f"{url}wireless/devices/config/radio0/interfaces/default_radio0",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        config=rule[f"enabled1"]; requests.put(f"{url}wireless/devices/config/radio0/interfaces/default_radio0",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def testConfigXL2TPDRule(headers, url, rule):
    try:
        event = "config"
        eventMark = "xl2tpd"
        rule["data"]["eventMark"] = eventMark
        rule["data"]["id"] =  "null"
        print("//////////////\nCreating rule\n")
        event_info=f"Event type = '{event}' | Event subtype = '{eventMark}'\n"; print(event_info)
        try:
            requests.post(f"{url}events_reporting/config",json=rule, headers=headers).raise_for_status()
        except requests.exceptions.HTTPError as error:
            print (error, '\n'); print("Error: No such event found"); return False, event_info
        print("Testing rule")
        config=rule[f"{eventMark}"]; requests.post(f"{url}l2tp/server/config",json=config, headers=headers).raise_for_status()
        time.sleep(2)
        requests.delete(f"{url}l2tp/server/config/test",json=config, headers=headers).raise_for_status()
        time.sleep(1)
        requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status()
        return True, event_info
    except FileNotFoundError as error:
        print (error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {rule} \n"); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    except requests.exceptions.HTTPError as error:
        print(error, '\n'); requests.delete(f"{url}events_reporting/config/cfg0192bd",headers=headers).raise_for_status(); return False, event_info
    
def allConfigCommands():
    total=76
    print(f"\nConfigAll\nConfigAvl\nConfigButtons\nConfigCallUtils\nConfigChilli\nConfigCLI\nConfigDDNS\nConfigDHCP\nConfigDMVPN\nConfigDropbear\nConfigEmailToSMS\nConfigEtherwake\nConfigEventsReporting\nConfigFirewall\nConfigFstab\nConfigGPS\nConfigHostblock\nConfigIOJuggler\nConfigIOMan\nConfigIpBlocked\nConfigIpSec\nConfigModbusServer\nConfigModbusClient\nConfigModbusGateway\nConfigMosquittoBroker\nConfigMosquittoPublisher\nConfigMultiWifi\nConfigMWan3\nConfigNetwork\nConfigNTPClient\nConfigNTPServer\nConfigOpenVPN\nConfigOperctl\nConfigOverview\nConfigP910ND\nConfigPackageRestore\nConfigPeriodicReboot\nConfigPingReboot\nConfigPostGet\nConfigPPTPD\nConfigPrivoxy\nConfigProfiles\nConfigQuotaLimit\nConfigRMSMQTT\nConfigRPCD\nConfigFota\nConfigSamba\nConfigSimSwitch\nConfigSimCard\nConfigSMSGateway\nConfigSMSUtilsRule\nConfigSNMPD\nConfigSNMPTrap\nConfigSQM\nConfigSTunnel\nConfigSystem\nConfigTelnet\nConfigUHTTPD\nConfigULogd\nConfigUserGroups\nConfigVRRPD\nConfigWidget\nConfigWifiScanner\nConfigWireless\nConfigXL2TPD\nSSHSuccessful\nSSHFailed\nWebUISuccessful\nWebUIFailed\nMobileConnectionConnected\nMobileConnectionDisconnected\nTestAll\n\nOnly for routers with serial I/O:\nConfigRSConsole\nConfigRSModbus\nConfigRSModem\nConfigRSOverIP\n\n{total} tests in total\n")