import sys
import random

if __name__ == "__main__":
    
    with open(sys.argv[1]) as f:
        neg = []
        pos = []
        for l in f.readlines():
            if(l[-2] == '0'):
                neg.append(l)
            else:
                pos.append(l)
        random.shuffle(neg)
        print(len(pos), len(neg))
        alldata = pos + neg[:len(pos)]

    pick = min(4000, len(alldata))
    small_data= random.sample(alldata, pick)
    small_data_train = small_data[:3*pick//5]
    testidx = 3*pick//5
    small_data_test = small_data[testidx:4*pick//5]
    validx = (4*pick//5)
    small_data_valid = small_data[validx:]

    with open('dataset/train.txt','w') as f:
        f.writelines(small_data_train)
    
    with open('dataset/test.txt','w') as f:
        f.writelines(small_data_test)

    with open('dataset/valid.txt','w') as f:
        f.writelines(small_data_valid)

