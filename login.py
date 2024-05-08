import json
import requests

from getpass import getpass
from pathlib import Path

#this file contains code which allows the user to connect to router1 and router2

def apiLogin1(router1_name, router1_password, router1_url):
    apilogin_file_path = Path(__file__).parent / "login.json"
    try:
        with open(apilogin_file_path) as f:
            login = json.load(f)
            login["apilogin"]["username"] = router1_name
            login["apilogin"]["password"] = router1_password
            apilogin1 = requests.post(f"{router1_url}login",json=login["apilogin"],timeout=5)
            apilogin1.raise_for_status()
            return apilogin1
    except requests.exceptions.HTTPError as error:
        print (error, '\n'); return False
    except requests.exceptions.Timeout as error:
        print (error, '\n'); return False
    except requests.exceptions.ConnectionError as error:
        print (error, '\n'); return False
    except requests.exceptions.InvalidURL as error:
        print (error, '\n'); return False
    except FileNotFoundError as error:
        print (error, '\n'); quit()
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {apilogin_file_path} \n"); quit()

def apiLogin2(router2_name, router2_password, router2_url):
    apilogin_file_path = Path(__file__).parent / "login.json"
    try:
        with open(apilogin_file_path) as f:
            login = json.load(f)
            login["apilogin"]["username"] = router2_name
            login["apilogin"]["password"] = router2_password
            apilogin2 = requests.post(f"{router2_url}login",json=login["apilogin"],timeout=5)
            apilogin2.raise_for_status()
            return apilogin2
    except requests.exceptions.HTTPError as error:
        print (error, '\n'); return False
    except requests.exceptions.Timeout as error:
        print (error, '\n'); return False
    except requests.exceptions.ConnectionError as error:
        print (error, '\n'); return False
    except requests.exceptions.InvalidURL as error:
        print (error, '\n'); return False
    except FileNotFoundError as error:
        print (error, '\n'); quit()
    except json.decoder.JSONDecodeError as error:
        print (error, '\n'); print(f"Incorrect JSON syntax at {apilogin_file_path} \n"); quit()


def auth1(apilogin1):
    if apilogin1 == False:
        quit()
    else:
        json_login=apilogin1.json()
        token=json_login.get("ubus_rpc_session")
        headers1={"Authorization": f"Bearer {token}"}
    return headers1

def auth2(apilogin2):
    if apilogin2 == False:
        quit()
    else:
        json_login=apilogin2.json()
        token=json_login.get("ubus_rpc_session")
        headers2={"Authorization": f"Bearer {token}"}
    return headers2

def router1Login():
    print("Router which will be sending SMS")
    router1_name=input("Username: ")
    router1_password=getpass("Password: ")
    router1_ip=input("IP: ")
    router1_url=f"http://{router1_ip}/api/"
    return router1_name, router1_password, router1_ip, router1_url
def router2Login():
    print("\nRouter which will be receiving SMS")
    router2_name=input("Username: ")
    router2_password=getpass("Password: ")
    router2_ip=input("IP: ")
    router2_url=f"http://{router2_ip}/api/"
    return router2_name, router2_password, router2_url

    
    



    