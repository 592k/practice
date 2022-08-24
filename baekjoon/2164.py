import sys

input = int(sys.stdin.readline())
if input>1:
    if input%2==0:
        print(4)
    else:
        print(2)
else:
    print(1)
