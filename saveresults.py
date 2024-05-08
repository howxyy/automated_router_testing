import time
import json
import requests
from load_rules import *

from pathlib import Path

#this file contains code which extracts the information from router2's SMSs and puts it in a file

def SMSInfo(headers2, rule, router2_url):
    try:
        res=requests.get(f"{router2_url}interfaces/config/mob1s1a1",headers=headers2)
        modem=res.json()["data"]["modem"]
        rep=requests.get(f"{router2_url}mobile_utilities/sms_messages/read/config/{modem}/0",headers=headers2)
        respmsg=rep.json()["data"]["message"]
        respnumb=rep.json()["data"]["sender"]
        config=rule["delete_sms"]; requests.delete(f"{router2_url}mobile_utilities/sms_messages/read/config/{modem}/0",json=config, headers=headers2); requests.delete(f"{router2_url}mobile_utilities/sms_messages/read/config/{modem}/1",json=config, headers=headers2); requests.delete(f"{router2_url}mobile_utilities/sms_messages/read/config/{modem}/2",json=config, headers=headers2)
        requests.delete(f"{router2_url}mobile_utilities/sms_messages/read/config/{modem}/3",json=config, headers=headers2); requests.delete(f"{router2_url}mobile_utilities/sms_messages/read/config/{modem}/4",json=config, headers=headers2); requests.delete(f"{router2_url}mobile_utilities/sms_messages/read/config/{modem}/5",json=config, headers=headers2)
        return respmsg, respnumb
    except requests.exceptions.HTTPError as error:
        print (error, '\n'); requests.delete(f"{router2_url}mobile_utilities/sms_messages/read/config/{modem}/0",json=config, headers=headers2); quit()
    except requests.exceptions.Timeout as error:
        print (error, '\n'); requests.delete(f"{router2_url}mobile_utilities/sms_messages/read/config/{modem}/0",json=config, headers=headers2); quit()
    except requests.exceptions.ConnectionError as error:
        print (error, '\n'); requests.delete(f"{router2_url}mobile_utilities/sms_messages/read/config/{modem}/0",json=config, headers=headers2); quit()
    except FileNotFoundError as error:
        print (error, '\n'); quit()
    except requests.exceptions.InvalidURL as error:
        print (error, '\n'); quit()
    except KeyError as error:
        print (error, '\n'); print("Could not get SMS information: No message detected")

def makeTestResultFile(headers2, product_name, function, rule, router2_url):
    try:
        curr_dir=Path(__file__).parent
        new_file_path = Path(curr_dir / 'testresults')
        if not Path.exists(new_file_path):
            Path.mkdir(new_file_path)
        current_date=time.strftime("%Y-%m-%d_%H:%M:%S")
        time.sleep(1)
        path = Path(curr_dir / "testresults" / f"{product_name}_{current_date}.csv")
        exp_msg_payload=rule["data"]["message"]
        rule_file_path = Path(__file__).parent / "rule.json"
        with open(rule_file_path) as f:
            file = json.load(f)
            exp_number = file["expected_number"]["telnum"]
        true_or_false, event_info = function
        with open(path, 'w') as f:
            if true_or_false == False:
                f.write("Test status, Failed\n")
                f.write(f"Event information, {event_info}")
                f.write(f"Received message payload, -\n")
                f.write(f"Received number, -\n")
                f.write(f"Expected message payload, {exp_msg_payload}\n")
                f.write(f"Expected number, {exp_number}\n")
                return False
            elif true_or_false == True:
                resp_msg, resp_numb = SMSInfo(headers2, loadrule(), router2_url)
                f.write("Test status, Successful\n")
                f.write(f"Event information, {event_info}")
                f.write(f"Received message payload, {resp_msg}\n")
                f.write(f"Received number, {resp_numb}\n")
                f.write(f"Expected message payload, {exp_msg_payload}\n")
                f.write(f"Expected number, {exp_number}\n")
                return True
    except FileNotFoundError as error:
        print (error, '\n'); quit()
    except TypeError:
        return False


            