"""
    For循环
"""
for item in [10, 20, 30, 40, 50]:
    print(item, end=' ') # 10 20 30 40 50

for i in "hello":
    print(i, end=' ') # h e l l o

print("\n###########################")
aa = range(1, 10, 2) # start end step
print(aa) # range(0, 10)
for item in aa:
    print(item, end=' ') # 1 3 5 7 9

print("\n##########################")

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} x {i} = {i * j}", end="\t")

    print()

