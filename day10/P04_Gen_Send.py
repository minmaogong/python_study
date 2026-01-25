"""
    send向生成器发送数据
    使用send() 发送任务id，使用生成器交替执行两个任务
"""
def gen():
    task_id = 0
    int_value = 0
    char_value = 'A'

    while True:
        match task_id:
            case 0:
                task_id = yield int_value
                int_value += 1
            case 1:
                task_id = yield  char_value
                ord(char_value) + 1
                char_value = chr(ord(char_value) + 1)
            case _:
                task_id =  yield None


f = gen()
print(next(f))
print(f.send(1))
print(f.send(1))
print(f.send(1))
print(f.send(1))
print(f.send(0))
print(f.send(0))
print(f.send(2))
print(f.send(0))
