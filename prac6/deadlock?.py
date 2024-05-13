num_of_processes=4
num_of_resources=3
release=[[1,0,1],[1,1,0],[0,1,0],[0,1,0]]
need=[[0,1,1],[1,0,0],[0,0,2],[0,2,0]]
available=[0,0,1]
pending=[0]*num_of_processes
finish=[0]*num_of_processes
while True:
    found=False
    for i in range(num_of_processes):
        # if all()
        if not finish[i] and all(available[j] >= need for j, need in enumerate(need[i])):
            found=True
            finish[i]=1
            for j in range(num_of_resources):
                available[j]+=release[i][j]
            break
        else: pending[i]=1
    if all(pending):
        print("deadlock")
        break
    if all(finish):
        print("done")
        break