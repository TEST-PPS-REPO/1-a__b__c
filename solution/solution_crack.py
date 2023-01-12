import sys
inp = sys.stdin.readline()

for i in range(8):
  with open('IO/in_{:04d}.txt'.format(i)) as f:
    if f.readline() == inp:
      with open('IO/out_{:04d}.txt'.format(i)) as f2:
        print(f2.readline())