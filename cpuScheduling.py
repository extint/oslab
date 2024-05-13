import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def round_robin(tasks, quantum):
    tasks.sort(key= lambda x: x[0])
    n =len(tasks)
    remaining_time =[task[1] for task in tasks]
    process_name=[task[3] for task in tasks]
    timeline=[]
    waiting_time=[0] * n
    turnaround_time =[0] * n
    completion_time=[0] * n
    current_time=0

    while any(remaining_time):
        for i in range(n):
            if remaining_time[i] > 0:
                execute_time =min(remaining_time[i], quantum)
                # execute_time =min(remaining_time, quantum)
                current_time +=execute_time
                remaining_time[i] -=execute_time
                # remaining_time[i] -=execute_time-i
                turnaround_time[i] =current_time
                waiting_time[i] =turnaround_time[i] - tasks[i][1]
                completion_time[i] =current_time
                timeline.append((current_time - execute_time, current_time, process_name[i]))

    avg_waiting_time=sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    print("Round Robin Scheduling")
    print("Process\t\tArrival Time\t\tBurst Time\t\tWaiting Time\t\tTurnaround Time\t\tCompletion Time")
    for i in range(n):
        print(f"{tasks[i][3]}\t\t{tasks[i][0]}\t\t\t{tasks[i][1]}\t\t\t{waiting_time[i]}\t\t\t{turnaround_time[i]}\t\t\t{completion_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

    return timeline

def fcfs(tasks):
    # waiting_time[0] =0
    # turnaround_time[0]= tasks[0][1]
    # completion_time
    tasks.sort(key=lambda x: x[0])
    n =len(tasks)
    timeline =[]
    current_time =0
    for task in tasks:
        timeline.append((current_time, current_time + task[1], task[3]))
        current_time+= task[1]

    waiting_time =[0] *n
    turnaround_time =[0]* n
    waiting_time[0] =0
    turnaround_time[0]= tasks[0][1]
    completion_time =[0]* n
    
    
    for i in range(1, n):
        waiting_time[i] =turnaround_time[i - 1]
        turnaround_time[i] = waiting_time[i] + tasks[i][1]
    completion_time =turnaround_time[:]

    avg_turnaround_time= sum(turnaround_time)/n
    avg_waiting_time =sum(waiting_time) /n

    print("FCFS Scheduling")
    print("Process\t\tArrival Time\t\tBurst Time\t\tWaiting Time\t\tTurnaround Time\t\tCompletion Time")
    for i in range(n):
        print(f"{tasks[i][3]}\t\t{tasks[i][0]}\t\t\t{tasks[i][1]}\t\t\t{waiting_time[i]}\t\t\t{turnaround_time[i]}\t\t\t{completion_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    return timeline

def sjf(tasks):
    tasks.sort(key=lambda x: (x[0], x[1]))
    n =len(tasks)
    timeline =[]
    current_time =0
    for process in tasks:
        timeline.append((current_time, current_time + process[1], process[3]))
        current_time +=process[1]

    waiting_time =[0] * n
    turnaround_time =[0] * n
    waiting_time[0] =0
    turnaround_time[0] =tasks[0][1]
    completion_time =[0] * n
    for i in range(1, n):
        waiting_time[i] =turnaround_time[i - 1]
        turnaround_time[i] =waiting_time[i] + tasks[i][1]
    completion_time =turnaround_time[:]
# waiting_time[i] =turnaround_time[i - 1]
#         turnaround_time[i] =waiting_time[i] + tasks[i][1]
#     completion_time =turnaround_time[:]

    avg_waiting_time =sum(waiting_time) / n
    avg_turnaround_time =sum(turnaround_time) / n

    print("SJF Scheduling:")
    print("Process\t\tArrival Time\t\tBurst Time\t\tWaiting Time\t\tTurnaround Time\t\tCompletion Time")
    for i in range(n):
        print(f"{tasks[i][3]}\t\t{tasks[i][0]}\t\t\t{tasks[i][1]}\t\t\t{waiting_time[i]}\t\t\t{turnaround_time[i]}\t\t\t{completion_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    return timeline

def priority_scheduling(tasks):
    tasks.sort(key=lambda x: (x[0], x[2]))
    n =len(tasks)
    timeline =[]
    current_time =0
    for process in tasks:
        timeline.append((current_time, current_time + process[1], process[3]))
        current_time +=process[1]

    waiting_time =[0] * n
    turnaround_time =[0] * n
    waiting_time[0] =0
    turnaround_time[0] =tasks[0][1]
    completion_time =[0] * n
    for i in range(1, n):
        waiting_time[i] =turnaround_time[i - 1]
        turnaround_time[i] =waiting_time[i] + tasks[i][1]
    completion_time =turnaround_time[:]

    avg_waiting_time =sum(waiting_time) / n
    avg_turnaround_time =sum(turnaround_time) / n

    print("Priority Scheduling:")
    # Process\t\tPriority\t\tBurst Time\t\tWaiting Time\t\tTurnaround Time\t\tCompletion Time")
    # for i in range(n):
    #     print(f"
    print("Process\t\tPriority\t\tBurst Time\t\tWaiting Time\t\tTurnaround Time\t\tCompletion Time")
    for i in range(n):
        print(f"{tasks[i][3]}\t\t{tasks[i][2]}\t\t\t{tasks[i][1]}\t\t\t{waiting_time[i]}\t\t\t{turnaround_time[i]}\t\t\t{completion_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}\n")
    return timeline

def gantt_chart(timeline, title):
    fig, ax =plt.subplots(figsize=(10, 1))

    colors ={} # Dictionary to store colors for each process
    # colors=[[]]  
    color_index =0

    for i, item in enumerate(timeline):
        process_name =item[2]
        if process_name not in colors:
            colors[process_name] =f'C{color_index}'
            color_index +=1
        # process_name not in colors:
        #     colors[process_name] =f'C{i}'
        #     color
        rect =Rectangle((item[0], 0), item[1] - item[0], 1, edgecolor='black', facecolor=colors[process_name])
        ax.add_patch(rect)

    # Create legend for process numbers
    legend_handles =[Rectangle((0, 0), 1, 1, color=colors[process_name], edgecolor='black') for process_name in colors]
    legend_labels =list(colors.keys())
    ax.legend(legend_handles, legend_labels, loc='upper left', title='Process Numbers')

    ax.set_xlim(0, max(entry[1] for entry in timeline) + 2)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    plt.title(title)
    plt.xlabel('Time')
    plt.show()


tasks =[
    (0, 8, 3, 'access'),
    (1, 6, 2, 'destroy'),
    (5, 9, 1, 'load'),
    (3, 4, 4, 'ADD'),
]

while True:
    algo =int(input("Enter which algorithm to do the tasks: \n1. First Come First Serve \n2. Shortest Job First \n3. Round Robin \n4. Priority Queue \n5. Exit\n"))
    if algo ==1:
        timeline =fcfs(tasks)
        gantt_chart(timeline, 'FCFS GANTT CHART')
    if algo ==2:
        timeline =sjf(tasks)
        gantt_chart(timeline, 'SJF GANTT CHART')
    if algo ==3:
        quantum =int(input("Enter size of time quantum: "))
        timeline =round_robin(tasks, quantum)
        gantt_chart(timeline, 'Round Robin GANTT CHART')
    if algo ==4:
        timeline =priority_scheduling(tasks)
        gantt_chart(timeline, 'PRIORITY GANTT CHART')
    if algo ==5:
        break
