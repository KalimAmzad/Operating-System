# Page Replacement Algorithm: LRU
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
page_fault = frame_size

for i in given:
    if i in frame:
        temp = []
        for j in frame:
            if j != i:
                temp.append(j)
        frame = temp
    else:
        slc = frame[1:]
        frame = slc
        page_fault += 1
    frame.append(i)
        
    print(frame)
        
print('Total Page fault: ',page_fault)        

wait = input()