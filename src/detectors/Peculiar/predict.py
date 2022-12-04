import sys
import shutil
import json
from detect import main

def backup_old_files():
    shutil.copy('dataset/data.jsonl', 'dataset/data.jsonl.bak')
    shutil.copy('dataset/train.txt', 'dataset/train.txt.bak')
    shutil.copy('dataset/test.txt', 'dataset/test.txt.bak')
    shutil.copy('dataset/valid.txt', 'dataset/valid.txt.bak')
    shutil.copy('saved_models/checkpoint-best-f1/model.bin', 'saved_models/checkpoint-best-f1/model.bin.bak')

def restore_backup():
    shutil.move('dataset/data.jsonl.bak', 'dataset/data.jsonl')
    shutil.move('dataset/train.txt.bak', 'dataset/train.txt')
    shutil.move('dataset/test.txt.bak', 'dataset/test.txt')
    shutil.move('dataset/valid.txt.bak', 'dataset/valid.txt')
    shutil.move('saved_models/checkpoint-best-f1/model.bin.bak', 'saved_models/checkpoint-best-f1/model.bin')

def predict_using_model(filename, modelname):
    with open(filename) as f:
        contract = f.read()
    
    j = {
        'contract':contract, 
        'address': 0x100,
        'idx': 0
    }

    backup_old_files()
    with open('dataset/data.jsonl', 'w') as f:
        f.write(json.dumps(j))
    
    with open('dataset/test.txt', 'w') as f:
        f.write('0\t0')

    shutil.copy2(modelname, 'saved_models/checkpoint-best-f1/model.bin')
    main(False)
    restore_backup()

    with open('saved_models/predictions.txt') as f:
        result = f.readline()[-2]
    print("Result = ", result)
    return result


def predict(filename):
    results = []
    for model in ['saved_models/checkpoint-best-f1/access_control_model.bin',
         'saved_models/checkpoint-best-f1/front_running_model.bin', 
         'saved_models/checkpoint-best-f1/reentrancy_model.bin', 
         'saved_models/checkpoint-best-f1/low_level_model.bin']:
         results.append(predict_using_model(filename, model))
    return results

if __name__=="__main__":
    predict(sys.argv[2])