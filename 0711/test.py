cnt=0
for i in range(1,101):
    if i % 6 == 0:
        cnt += 1
        print(i, end="\t")
    if cnt % 4 == 0:
        print()
        
for i in range(1,101):
    if i % 6 == 0:
        print(i, end="\t")
    if i % 24 == 0:
        print()