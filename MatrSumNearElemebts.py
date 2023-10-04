# put your python code here
a = []
inp = input()
while inp != 'end':
    a.append([int(j) for j in inp.split()])
    inp = input()
b = 0
for i in range(len(a)):
    print()
    for j in range(len(a[i])):
        b = a[i-1][j] + a[i+1-len(a)][j] + a[i][j-1] + a[i][j+1-len(a[i])]
        print(b, end = " ")