def is_safe_state(available, max_claim, allocated):
    num_processes=len(allocated)
    num_resources=len(available)

    # Initialize work and finish arrays
    work=available[:]
    finish =[False] * num_processes

    safe_sequence=[]

    #loop through processes until all are finished or no safe sequence exists
    while True:
        #finding an index i such that prcess i is not finished and needs <= available
        found= False
        for i in range(num_processes):
            # print(i,"global")
            if not finish[i] and all(need + work[j] >= max_claim[i][j] for j, need in enumerate(allocated[i])):
                # print(i)
                #proess i can complete, update work and mark process i finished
                for j in range(num_resources):
                    work[j]+= allocated[i][j]
                finish[i]=True
                safe_sequence.append(i)
                found=True
                break
        # print("found",found)
        # print(work)
        if not found:
            #if no such process found, break the loop
            break

    #check if all processes are finished, return safe sequence
    if all(finish):
        return safe_sequence
    else:
        return None
    
available_resources = [0,0,0]
max_needed_resources = [
    [3, 2, 2],
    [6, 1, 3],
    [3, 1, 4],
    [4, 2, 2]
]
allocated_resources = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1]
]

# deadlock input
# available_resources = [1, 1, 1] 
# max_needed_resources = [
#     [3, 3, 20],
#     [1, 1, 10]
# ]
# allocated_resources = [
#     [1, 0, 1],
#     [1, 1, 1]
# ]


safe_sequence = is_safe_state(available_resources, max_needed_resources, allocated_resources)

if safe_sequence:
    print("Safe sequence:", safe_sequence)
else:
    print("No safe sequence found -> DEADLOCK")









# def Traverse(e):
#     # pprint.pprint(e[0])
#     # pprint.pprint(e[1])
#     count=0
#     for i in range (len(e[0])):
#         # print(e[0][i])
#         # print(e[1][i])
#         if(e[0][i]>e[1][i]):
#             count+=1
#     if(count>len(e)/2):
#         temp=e[0]
#         e[0]=e[1]
#         e[1]=temp

# def mySort(e):
#     for j in range (len(e)):
#         for i in range(len(e)-j-1):
#                 o=[e[i],e[i+1]]
#                 # print(o)
#                 x1=threading.Thread(target=Traverse,args=(o,)).start()
#                 x1.join()
#                 # print(e[i])
#                 # print(e[i+1]) 
            

# # pprint.pprint(max_needed_resources)
# mySort(max_needed_resources)
# import time
# time.sleep(4)
# pprint.pprint(max_needed_resources)
# # pprint.pprint(sorted)