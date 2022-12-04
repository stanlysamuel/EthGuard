import sys
from Peculiar.predict import predict

# Code to take as input a solidity program and print it's contents
f = open(sys.argv[2])
predict(f.name)
# print(f.read())
