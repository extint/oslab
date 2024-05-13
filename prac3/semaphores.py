import time

def current_permits(available_permits):
    print("num of available permits:", available_permits)

def enter_critical_section(available_permits, waiting_processes, processes_in_critical_section):
    global process_number
    if available_permits==0:
        print(f"Process {process_number} Blocked")
        waiting_processes.append(process_number)
    else:
        print(f"Proccess {process_number} entered the critical section")
        processes_in_critical_section.append(process_number)
        available_permits-=1
    process_number+=1
    return available_permits

def leave_critical_section(available_permits, waiting_processes, processes_in_critical_section):
    global process_number
    if not processes_in_critical_section:
        print("Critical Section Free")
        return available_permits

    completed_process =processes_in_critical_section.pop(0)
    print(f"Process {completed_process} finished and left the critical section.")
    available_permits +=1
        # if not processes_in_critical_section:
    #     print("Critical Section Free")
    #     return available_permits
    if waiting_processes:
        next_process =waiting_processes.pop(0)
        processes_in_critical_section.append(next_process)
        print(f"Process {next_process} is entering the critical section")
    return available_permits

process_number=1

# Hardcoded input values
initial_permits=4
process_count=2

available_permits =initial_permits
current_permits(available_permits)

waiting_processes =[]
processes_in_critical_section =[]

# initial execution and pushing extra tasks in waiting_processes queue
for _ in range(process_count):
    available_permits =enter_critical_section(available_permits, waiting_processes, processes_in_critical_section)

current_permits(available_permits)
time.sleep(2)

for _ in range(process_count):
    available_permits=leave_critical_section(available_permits, waiting_processes, processes_in_critical_section)
    current_permits(available_permits)
    time.sleep(2)

print("all proccess executed")
