import json

from pathlib import Path

#this file contains code, which loads the rule triggers from rule.json

def loadrule():
    try:
        file_path = Path(__file__).parent / "rule.json"
        with open(file_path ,'r') as f:
            rule = json.load(f)
            return rule
    except json.decoder.JSONDecodeError as a:
        print (a, '\n')
        print(f"Incorrect JSON syntax at {file_path} \n")
        print("Error: config failed to load")
        quit()
    except FileNotFoundError as a:
        print (a, '\n')
        print("Error: config failed to load")
        quit()
