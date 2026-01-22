__all__ = ["num", "add"]

num = 100
num1 = 200
_str1 = "abc"

def add(a, b):
    """求两个数的和"""
    return a + b

# print(__name__)

if __name__ == "__main__":
    print(add(50,60))