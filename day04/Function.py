"""
    函数的定义
"""

# rows columns 形参
def print_stars(rows = 2, columns = 3):
    """打印两行三列*"""
    while rows > 0:
        print("*" * columns)
        rows -= 1

print_stars()
print("-" * 50)
print_stars(rows=3, columns=4) # 3， 4 实参
