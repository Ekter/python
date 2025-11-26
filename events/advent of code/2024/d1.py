# get data as text from https://adventofcode.com/2024/day/1/input
import subprocess
from tqdm import tqdm
from collections import Counter
cmd = "wget -qO- https://adventofcode.com/2024/day/1/input --load-cookies=../cookies-adventofcode-com.txt"
print("    Downloading data...", end="")

result = subprocess.check_output(cmd, shell=True).decode("utf-8")

print("✅")



lines = result.split("\n")
lines1 = []
lines2 = []
for line in lines[:-1]:
    lines1.append(int(line.split(" ")[0]))
    lines2.append(int(line.split(" ")[-1]))

lines1.sort()
lines2.sort()

diff = 0

for n1, n2 in zip(lines1, lines2):
    diff += abs(n1 - n2)

print("Part 1\n")

print(diff)

c1 = Counter(lines1)

c2 = Counter(lines2)

simm = 0

for k, _ in c1.items():
    simm += k*c2[k]

print("\nPart 2\n")

print(simm)
