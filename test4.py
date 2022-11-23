#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

e1=(int(lines[0].split(" ")[0]),int(lines[0].split(" ")[1]))
e2=(int(lines[1].split(" ")[0]),int(lines[1].split(" ")[1]))
e3=(int(lines[2].split(" ")[0]),int(lines[2].split(" ")[1]))
d1=(e2[0]-e1[0],e2[1]-e1[1])
d2=(e3[0]-e1[0],e3[1]-e1[1])
l=[]

for line in lines[4:]:
    print(line)
    l.append((int(line.split(" ")[0]),int(line.split(" ")[1])))

found=True

for e in l:
    print(e,(e[0]+d1[0],e[1]+d1[1]))
    if (e[0]+d1[0],e[1]+d1[1]) in l and (e[0]+d2[0],e[1]+d2[1]) in l:
        print(f"{e[0]} {e[1]}")
        print(f"{e[0]+d1[0]} {e[1]+d1[1]}")
        print(f"{e[0]+d2[0]} {e[1]+d2[1]}")
        found=False
        break
if found:
    print("NOT FOUND")