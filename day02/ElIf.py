"""
    多分支
"""
age = int(input("请输入你的年龄："))
print(f"当前用户输入的年龄为：{age}")

if age < 2:
    print("婴儿")
elif age < 4:
    print("幼儿")
elif age < 13:
    print("儿童")
elif age < 20:
    print("青少年")
elif age < 65:
    print("成年人")
else:
    print("老年人")