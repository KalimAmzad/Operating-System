# Page Replacement Algorithm: Optimal
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
given_index = 0
page_fault = frame_size

for i in given:
    if not (i in frame):
        rest = given[given_index:]
        max_index = -1
        for j in frame:
            try:
                idx = rest.index(j)
                if idx > max_index:
                    max_index = idx
                    frame_index = frame.index(rest[max_index])
            except:
                frame_index = frame.index(j)
                break;
        frame[frame_index] = i
        page_fault = page_fault+1
    
    print(frame)
    given_index = given_index+1
    
print('Total page fault: ',page_fault)

wait = input()
                
        
    
