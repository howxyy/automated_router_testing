from configrules import *
from otherrules import *
from saveresults import *
from login import *
from colorama import Fore, Style

def runProgram():
        
    """apilogin_file_path = Path(__file__).parent / "login.json"
    with open(apilogin_file_path) as f:
        login = json.load(f)
        router1_name=login["apilogin"]["username"]
        router1_password=login["apilogin"]["password"]
        router1_ip=login["apilogin"]["ip"]
        router1_url=login["apilogin"]["url"]
        router2_name=login["apilogin2"]["username"]
        router2_password=login["apilogin2"]["password"]
        router2_url=login["apilogin2"]["url"]
        headers1=apiLogin1(router1_name, router1_password, router1_url)
        headers2=apiLogin2(router2_name, router2_password, router2_url)""" #easier login for debugging. put credentials in login.json file 
        

    successful_tests = 0
    failed_tests = 0

    router1_name, router1_password, router1_ip, router1_url = router1Login()
    while True:
        if apiLogin1(router1_name, router1_password, router1_url) == False:
            print("Login failed, try again")
            router1_name, router1_password, router1_ip, router1_url = router1Login()
        else:
            headers1=apiLogin1(router1_name, router1_password, router1_url)
            break
    router2_name, router2_password, router2_url = router2Login()
    while True:
        if apiLogin1(router2_name, router2_password,router2_url) == False:
            print("Login failed, try again")
            router2_name, router2_password, router2_url = router2Login()
        else:
            headers2=apiLogin2(router2_name, router2_password,router2_url)
            break
    
    response=requests.get(f"{router1_url}device/info",headers=auth1(headers1))
    product_name=response.json()["data"]["mnfinfo"]["name"]
    print(f"\nProduct name: {product_name}\n")
    while True:
        try:
            user_input=input("Input a command: ")  
            match user_input:
                case "quit":
                    quit()
                case "help":
                    print("\nquit (quit program)\nhelp (print all available commands)\nresults (print test results)\ntests (print all available tests)\nchangenumber (input the numbers your routers are using)\n")
                case "results": 
                    print(Fore.GREEN + f"\nSuccessful tests = {successful_tests}")
                    print(Fore.RED + f"Failed tests = {failed_tests}")
                    print(Style.RESET_ALL)
                case "newtoken":
                        headers1=apiLogin1(router1_name, router1_password, router1_url)
                        headers2=apiLogin2(router2_name, router2_password, router2_url)
                        auth1(headers1)
                        auth2(headers2)
                case "changenumber":
                    router1_number=input("Router's number which will be sending SMS (Format: '+370XXXXXXXX'): ")
                    while True:
                        try:
                            if len(router1_number) != 12:
                                print("Error: Incorrect phone number format")
                                router1_number=input("Enter a phone number (Format: '+370XXXXXXXX'): ")
                            elif type(int(router1_number)) != int:
                                print("Error: Incorrect phone number format")
                                router1_number=input("Enter a phone number (Format: '+370XXXXXXXX'): ")
                            else:
                                rule_file_path = Path(__file__).parent / "rule.json"
                                with open(rule_file_path) as f:
                                    file = json.load(f)
                                    file["expected_number"].pop("telnum")
                                    file["expected_number"]["telnum"] = router1_number
                                    changed_number = json.dumps(file, indent = 4)
                                with open(rule_file_path, 'w') as f:
                                    f.write(changed_number)
                                break
                        except ValueError as error:
                            print(error, '\n')
                            router1_number=input("Enter a phone number (Format: '+370XXXXXXXX'): ")
                    router2_number=input("Router's number which will be receiving SMS (Format: '+370XXXXXXXX'): ")
                    while True:
                        try:
                            if len(router2_number) != 12:
                                print("Error: Incorrect phone number format")
                                router2_number=input("Enter a phone number (Format: '+370XXXXXXXX'): ")
                            elif type(int(router2_number)) != int:
                                print("Error: Incorrect phone number format")
                                router2_number=input("Enter a phone number (Format: '+370XXXXXXXX'): ")
                            else:
                                rule_file_path = Path(__file__).parent / "rule.json"
                                with open(rule_file_path) as f:
                                    file = json.load(f)
                                    file["data"].pop("telnum")
                                    file["data"]["telnum"] = router2_number
                                    changed_number = json.dumps(file, indent = 4)
                                with open(rule_file_path, 'w') as f:
                                    f.write(changed_number)
                                break
                        except ValueError as error:
                            print(error, '\n')
                            router2_number=input("Enter a phone number (Format: '+370XXXXXXXX'): ")
                case "tests":
                    allConfigCommands()        
                case "ConfigAll": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigAllRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1                
                case "ConfigAvl": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigAvlRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigButtons": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigButtonsRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:           
                        failed_tests = failed_tests + 1
                case "ConfigCallUtils": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigCallUtilsRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigChilli": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigChilliRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigCLI": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigCLIRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigDDNS": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigDDNSRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigDHCP": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigDHCPRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigDMVPN": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigDMVPNRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigDropbear": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigDropbearRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigEmailToSMS": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigEmailToSMSRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigEtherwake": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigEtherwakeRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigEventsReporting": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigEventsReportingRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigFirewall": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigFirewallRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigFstab": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigFstabRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigGPS": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigGPSRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigHostblock": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigHostblockRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigIOJuggler": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigIOJugglerRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigIOMan": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigIOManRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigIpBlocked": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigIpBlockedRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigIpSec": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigIpSecRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigModbusServer": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigModbusServerRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigModbusClient": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigModbusClientRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigModbusGateway": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigModbusGatewayRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigMosquittoBroker": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigMosquittoBrokerRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigMosquittoPublisher": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigMosquittoPublisherRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigMultiWifi": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigMultiWifiRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigMWan3": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigMWan3Rule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigNetwork": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigNetworkRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigNTPClient": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigNTPClientRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigNTPServer": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigNTPServerRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigOpenVPN": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigOpenVPNRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigOperctl": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigOperctlRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigOverview": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigOverviewRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigP910ND": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigP910NDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigPackageRestore": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPackageRestoreRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigPeriodicReboot": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPeriodicRebootRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigPingReboot": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPingRebootRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigPostGet": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPostGetRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigPPTPD": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPPTPDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigPrivoxy": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPrivoxyRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigProfiles": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigProfilesRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigQuotaLimit": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigQuotaLimitRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigRMSMQTT": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRMSMQTTRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigRPCD": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRPCDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigFota": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigFotaRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigSamba": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSambaRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigSimSwitch": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSimSwitchRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigSimCard": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSimCardRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigSMSGateway": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSMSGatewayRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigSMSUtils": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSMSUtilsRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigSNMPD": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSNMPDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigSNMPTrap": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSNMPTrapRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigSQM": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSQMRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigSTunnel": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSTunnelRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigSystem": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSystemRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigTelnetD": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigTelnetDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigUHTTPD": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigUHTTPDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigULogd": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigULogdRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigUserGroups": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigUserGroupsRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigVRRPD": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigVRRPDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigWidget": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigWidgetRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigWifiScanner": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigWifiScannerRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigWireless": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigWirelessRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "ConfigXL2TPD": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigXL2TPDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "SSHSuccessful": 
                    if makeTestResultFile(auth2(headers2), product_name, testSSHSuccessfulRule(auth1(headers1), router1_url, loadrule(), router1_password, router1_ip), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "SSHFailed": 
                    if makeTestResultFile(auth2(headers2), product_name, testSSHFailedRule(auth1(headers1), router1_url, loadrule(), router1_ip), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "WebUISuccessful": 
                    if makeTestResultFile(auth2(headers2), product_name, testWebUISuccessfulRule(auth1(headers1), router1_url, loadrule(), router1_name, router1_password), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "WebUIFailed": 
                    if makeTestResultFile(auth2(headers2), product_name, testWebUIFailedRule(auth1(headers1), router1_url, loadrule(), router1_name), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "MobileConnectionConnected": 
                    if makeTestResultFile(auth2(headers2), product_name, testMobileConnectionConnectedRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "MobileConnectionDisconnected": 
                    if makeTestResultFile(auth2(headers2), product_name, testMobileConnectionDisconnectedRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1 
                case "ConfigRSConsole": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRSConsoleRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1    
                case "ConfigRSModbus": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRSModbusRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1    
                case "ConfigRSModem": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRSModemRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1    
                case "ConfigRSOverIP": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRSOverIPRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case "TestAll": 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigAllRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else: 
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigAvlRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1    
                    if makeTestResultFile(auth2(headers2), product_name, testConfigButtonsRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigCallUtilsRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigChilliRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigCLIRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigDDNSRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigDHCPRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigDMVPNRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigDropbearRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigEmailToSMSRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigEtherwakeRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigEventsReportingRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigFirewallRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigFstabRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigGPSRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigHostblockRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigIOJugglerRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigIOManRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigIpBlockedRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigIpSecRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigModbusServerRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigModbusClientRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigModbusGatewayRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigMosquittoBrokerRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigMosquittoPublisherRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigMultiWifiRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigMWan3Rule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigNetworkRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigNTPClientRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigNTPServerRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigOpenVPNRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigOperctlRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigOverviewRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigP910NDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPackageRestoreRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPeriodicRebootRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPingRebootRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPostGetRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPPTPDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigPrivoxyRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigProfilesRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigQuotaLimitRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRMSMQTTRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRPCDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigFotaRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSambaRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSimSwitchRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSimCardRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSMSGatewayRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSMSUtilsRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSNMPDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSNMPTrapRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSQMRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSTunnelRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigSystemRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigTelnetDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigUHTTPDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigULogdRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigUserGroupsRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigVRRPDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigWidgetRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigWifiScannerRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigWirelessRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testConfigXL2TPDRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testSSHSuccessfulRule(auth1(headers1), router1_url, loadrule(), router1_password, router1_ip), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testSSHFailedRule(auth1(headers1), router1_url, loadrule(), router1_ip), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testWebUISuccessfulRule(auth1(headers1), router1_url, loadrule(), router1_name, router1_password), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testWebUIFailedRule(auth1(headers1), router1_url, loadrule(), router1_name), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testMobileConnectionConnectedRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                    if makeTestResultFile(auth2(headers2), product_name, testMobileConnectionDisconnectedRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1 
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRSConsoleRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1    
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRSModbusRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1    
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRSModemRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1    
                    if makeTestResultFile(auth2(headers2), product_name, testConfigRSOverIPRule(auth1(headers1), router1_url, loadrule()), loadrule(), router2_url) != False:
                        successful_tests = successful_tests + 1
                    else:
                        failed_tests = failed_tests + 1
                case other:
                    print(f"'{user_input}' command not found")
        except requests.exceptions.HTTPError:
            print("Bearer token expired. Creating new one..")
            time.sleep(1)
            headers1=apiLogin1(router1_name, router1_password, router1_url)
            headers2=apiLogin2(router2_name, router2_password, router2_url)
            continue