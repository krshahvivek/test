rows = 5
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
a = 1
'''1
    3 3
    5 5 5
    7 7 7 7
    9 9 9 9 9'''
'''while a <= rows:
    j = 1
    while j <= a:
        print((a*2-1), end=" ")
        j += 1
    a += 1 
    print(' ')'''

'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1'''
'''for i in range(rows, 0 , -1):
    for j in range(i):
        print(i, end=' ')
    print(' ')'''

'''
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1'''
'''for i in range(rows):
    for j in range(i,0,-1):
        print(j, end=' ')
    print(' ')'''

'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1'''
'''for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print(' ')'''
'''
1
3 2
6 5 4
10 9 8 7'''
'''start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    print(':::::',start,stop)
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop'''
