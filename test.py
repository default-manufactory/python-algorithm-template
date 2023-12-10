import sys
import time
from pathlib import Path

# 주석------------
base_path = Path(__file__).parent
file_path = (base_path / "./python.txt").resolve()
sys.stdin = open(file_path, 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())
count = 0
check = 1
while check ** 2 <= N:
    check += 1
    count += 1

print(count)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
