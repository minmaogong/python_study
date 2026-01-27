"""
    闭包
"""

def outer():
    a = 10
    b = 20
    def inner():
        return a + b

    return inner

inn = outer()
# print(inn())
cell_tup = inn.__closure__
print(cell_tup[0].cell_contents) # 10
print(cell_tup[1].cell_contents) # 20
print(inn.__closure__) # (<cell at 0x1007cad70: int object at 0x101ae2518>, <cell at 0x1007ca620: int object at 0x101ae2658>)