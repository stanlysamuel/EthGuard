from pandas import DataFrame
import os
import json
from pathlib import Path


if __name__ == '__main__':
    reentrant_contracts = []
    acceess_control_contracts = []
    front_running_contracts = []
    unchecked_low_calls_contracts = []

    reentrant_annotation = {}
    acceess_control_annotations = {}
    front_running_annotations = {}
    unchecked_low_calls_annotations = {}

    base_path = Path("/home/ajinkya/Workspace/smartbugs-results/results/mythril/icse20")
    for a in os.listdir(base_path):
        print("processing ", a)
        current_path = base_path/a/"result.json"
        if(current_path.exists()):
            with open(current_path) as f:
                j = json.load(f)
                if(j['analysis'] is not None):
                    for i in j['analysis']["issues"]:
                        if i["title"].find("State change after external call") != -1:
                            reentrant_contracts.append(a)
                        if i["title"].find("DELEGATECALL to a user-supplied address") != -1:
                            acceess_control_contracts.append(a)
                        if i["title"].find("Unchecked SUICIDE") != -1:
                            acceess_control_contracts.append(a)
                        if i["title"].find("Use of tx.origin") != -1:
                            acceess_control_contracts.append(a)
                        if i["title"].find("Call data forwarded with delegatecall()") != -1:
                            acceess_control_contracts.append(a)
                        if i["title"].find("Transaction order dependence") != -1:
                            front_running_contracts.append(a)
                        if i["title"].find("Unchecked CALL return value") != -1:
                            unchecked_low_calls_contracts.append(a)
    print("building annotations")
    with open('dataset/data.jsonl') as f:
        for l in f.readlines():
            j = json.loads(l)
            addr = j['address']
            idx = j['idx']
            print(addr)
            if addr in reentrant_contracts:
                reentrant_annotation[idx] = 1
            else:
                reentrant_annotation[idx] = 0
            
            if addr in acceess_control_contracts:
                acceess_control_annotations[idx] = 1
            else:
                acceess_control_annotations[idx] = 0

            if addr in front_running_contracts:
                front_running_annotations[idx] = 1
            else:
                front_running_annotations[idx] = 0
            
            if addr in unchecked_low_calls_contracts:
                unchecked_low_calls_annotations[idx] = 1
            else:
                unchecked_low_calls_annotations[idx] = 0
    
    print("dumping")
    with open('reentrant-data.txt', "w") as f:
        for k, v in reentrant_annotation.items():
            f.write(str(k)+'\t'+str(v)+"\n")
    
    with open('access-control-data.txt', "w") as f:
        for k, v in acceess_control_annotations.items():
            f.write(str(k)+'\t'+str(v)+"\n")
    
    with open('front-running-data.txt', "w") as f:
        for k, v in front_running_annotations.items():
            f.write(str(k)+'\t'+str(v)+"\n")
        
    with open('unchecked_low_calls-data.txt', "w") as f:
        for k, v in unchecked_low_calls_annotations.items():
            f.write(str(k)+'\t'+str(v)+"\n")


