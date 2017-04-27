f = open("data.csv","r").readlines()
g = []
for i in range(1,len(f)):
    split_f = f[i].split(",")
    el = []
    if split_f[1] == '"MPI_Waitall"':
        elem = ''
        tmp = False
        for i in f[i]:
            if tmp == False and i == '"':
                tmp = True
            elif tmp == True and i =='"':
                tmp = False
                el.append(elem)
                elem = ''
            elif tmp == True:
                elem += i
        g.append(el)
    else:
        g.append(split_f)

print len(f)
# Creating the blocks
blocks = []
block = []

for i in range(0,len(g)):
    if g[i][0] == "MPI_Waitall":
        block.append(g[i])
        blocks.append(block)
        block = []
    else:
        block.append(g[i])

def shrink(str):
    tmp = []
    sat = False
    for i in str:
        if i == "[":
            sat = True
        elif sat == True and i == "]":
            sat = False
        elif sat == True and i != ",":
            tmp.append(i)
    return tmp

h = file("parsed_data.csv", "w")
for i in range(0, len(blocks)):
    print str(blocks[i]) +"\n" 
    h.write(str(blocks[i]) + "\n")
   
#parsing the blocks
for i in range(0, len(blocks)):
    t_call = []
    for j in range(0, len(blocks[i])):
       if blocks[i][j][1] == '"MPI_Irecv"' or  blocks[i][j][1] == '"MPI_Isend"' :
           t_call.append(blocks[i][j][11])
#       if blocks[i][j][0] == "MPI_Waitall":
           #print shrink(blocks[i][j][1])
    #print map(int, t_call)
