frames=[]
page_faults = 0
page_table={}

def page_replacement(page_num, num_frames):
    global page_faults
    
    if page_num not in frames:
        page_faults += 1
        if len(frames) < num_frames:
            frames.append(page_num)
            page_table[page_num] = len(frames) - 1
        else:
            print("Replacing using FIFO algorithm")
            first = frames[0]
            frames.pop(0)
            frames.append(page_num)
            page_table.pop(first)
            page_table[page_num] = 0
        print('Miss')
           
    else:
        print('Page already in Main Memory')
        print('Hit')

    return page_table

logical_address = 64  # input logical address size
physical_address = 16  # input physical address size

possible_values=[]
for i in range(1, physical_address):
    if physical_address % i == 0 and logical_address % i == 0:
        possible_values.append(i)

print("Possible page sizes:", possible_values)
page_size = 4  # input page size
if page_size in possible_values:
    num_pages = logical_address // page_size
    num_frames = physical_address // page_size
    while True:
        print('Enter page number in range 0 to', num_pages - 1)
        page_num = int(input())
        if page_num < 0 or page_num >= num_pages:
            print('Invalid page number')
        else:
            page_table = page_replacement(page_num, num_frames)
        print("Page Table:", page_table)
else:
    print('Not a valid page size')