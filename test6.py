#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

# lines = []
# for line in sys.stdin:
# 	lines.append(line.rstrip('\n'))

lines="""10
.XXX.XX.X.
....XXXXXX
XXXXXX.XX.
X...XXXXXX
XXX...XXX.
X.X.XXX.XX
.X.X..XX.X
X..X...XX.
XXO..XXXXX
..X.X...X.""".split("\n")
#find the way to the key("O") with the minimum number of traps("X") 
# #lines = 
# 6
# ..X...
# XXXXX.
# .XXX.X
# XXXO..
# .XXX.X
# ..X...

lines.pop(0)

coord_key=[0,0]
for i in range(1,len(lines)):
    if lines[i].find("O")!=-1:
        coord_key=[i,lines[i].find("O")]
list_fitness=[99]
list_movement=[[0,1],[0,-1],[1,0],[-1,0]]
def goto(coord, actual, list_already_gone, Xs=0):
    if Xs>10:
        return
    for possibility in list_movement:
        ci=[actual[0]+possibility[0],actual[1]+possibility[1]]
        # print(ci,list_already_gone)
        if ci[0]<0 or ci[1]<0 or ci[0]>=len(lines) or ci[1]>=len(lines[0]):
            continue
        if ci not in list_already_gone:
            # print(ci)
            if lines[ci[0]][ci[1]]=="O":
                list_fitness.append(Xs)
                print("AHAHAHAHHAHAHA")
            else:
                list_already_gone.append(ci)
                X=goto(coord, ci, list_already_gone,Xs+1 if lines[ci[0]][ci[1]]=="X" else Xs)
                list_already_gone.pop()
                # print(list_already_gone)
                return X

goto(coord_key, [0,0], [[0,0]])

etp1=min(list_fitness)

list_fitness=[99]
goto(coord_key, [len(lines),len(lines)], [[0,0]])
print(min(list_fitness)+etp1)