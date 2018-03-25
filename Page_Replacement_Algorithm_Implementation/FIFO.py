# Page Replacement Algorithm: FIFO
# AUTHOR: Kalim Amzad
frame_size = int(input('Enter Frame Size: '))
page = int(input('Enter Total no of page: '))
given = []
print('Enter page no')
for i in range(page):
    x = int(input())
    given.append(x)

# manually assigning 1st frame_size page in frame
frame = given[:frame_size]
given = given[frame_size:]
index = 0
page_fault = frame_size

for i in given:
    if not (i in frame):
        frame[index] = i
        index += 1
        if index == frame_size:
            index = 0
        page_fault = page_fault+1
    
    print(frame)
    
print('Total page fault: ',page_fault)

wait = input()
