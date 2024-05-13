from collections import deque
from collections import defaultdict
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Frames"]

def fifo(page_reference_string, num_frames):
    page_faults = 0
    frames = []
    hit_miss = []
    for page in page_reference_string:
        table.clear_rows()
        if page not in frames:
            page_faults += 1
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            hit_miss.append('Miss')
        else:
            hit_miss.append('Hit')
        for i in frames:
            table.add_row([str(i)])
        if len(frames) < num_frames:
            for i in range(num_frames - len(frames)):
                table.add_row([" "])
        print(table)
    print(hit_miss)
    return page_faults

def lru(page_reference_string, num_frames):
    page_faults = 0
    frames = deque(maxlen=num_frames)
    hit_miss = []

    for page in page_reference_string:
        table.clear_rows()
        if page not in frames:
            page_faults += 1
            if len(frames) == num_frames:
                frames.popleft()
            frames.append(page)
            hit_miss.append('Miss')
        else:
            frames.remove(page)
            frames.append(page)
            hit_miss.append('Hit')
        frame_list = list(frames)
        for i in frame_list:
            table.add_row([str(i)])
        if len(frame_list) < num_frames:
            for i in range(num_frames - len(frame_list)):
                table.add_row([" "])
        print(table)

    print(hit_miss)
    return page_faults

def lfu(page_reference_string, num_frames):
    page_faults = 0
    frames = []
    hit_miss = []
    page_access_count = defaultdict(int)

    for page in page_reference_string:
        table.clear_rows()
        if page not in frames:
            page_faults += 1
            if len(frames) == num_frames:
                least_used_page = min(frames, key=lambda x: page_access_count[x])
                frames.remove(least_used_page)
            frames.append(page)
            hit_miss.append('Miss')
        else:
            hit_miss.append('Hit')
        page_access_count[page] += 1
        for i in frames:
            table.add_row([str(i)])
        if len(frames) < num_frames:
            for i in range(num_frames - len(frames)):
                table.add_row([" "])
        print(table)
    print(hit_miss)
    return page_faults

with open('prac8/input.txt', 'r') as file:
    page_reference_string = list(map(int, file.readline().strip().split()))
    num_frames = int(file.readline().strip())

print("***FIFO Algorithm***")
fifo_page_faults = fifo(page_reference_string, num_frames)
print("Page faults:", fifo_page_faults)

print("***LRU Algorithm***")
lru_page_faults = lru(page_reference_string, num_frames)
print("Page faults:", lru_page_faults)

print("***LFU Algorithm***")
lfu_page_faults = lfu(page_reference_string, num_frames)
print("Page faults:", lfu_page_faults)
