"""
    send向生成器发送数据
    把send发送的值作为整个yield表达式结果
    使用send() 发送任务id，使用生成器交替执行两个任务
"""
def gen():
    task_id = 0
    int_value = 0
    char_value = 'A'

    while True:
        match task_id:
            case 0:
                # 把send发送的值作为整个yield表达式的结果
                task_id = yield int_value
                int_value += 1
            case 1:
                task_id = yield char_value
                ord(char_value) + 1
                char_value = chr(ord(char_value) + 1)
            case _:
                task_id =  yield None


# f = gen()
# print(next(f)) # 1️⃣ yield int_value 取出数据‘0’后在yield int_value处暂停
# print(f.send(1)) # 2️⃣ 发送1作为 yield int_value表达式的结果，恢复执行，task_id被赋值为1，继续走while循环，匹配case 1 代码块，取出‘A’后在yield char_value处暂停
# print(f.send(1)) # 3️⃣ 发送1作为 yield char_value表达式的结果，恢复执行，task_id被赋值为1，继续走while循环，匹配case 1 代码块，取出‘B’后在yield char_value处暂停
# print(f.send(1)) # 4️⃣ 发送1作为 yield char_value表达式的结果，恢复执行，task_id被赋值为1，继续走while循环，匹配case 1 代码块，取出‘C’后在yield char_value处暂停
# print(f.send(1)) # 5️⃣ 发送1作为 yield char_value表达式的结果，恢复执行，task_id被赋值为1，继续走while循环，匹配case 1 代码块，取出‘D’后在yield char_value处暂停
# print(f.send(0)) # 6️⃣ 发送0作为 yield char_value表达式的结果，恢复执行，task_id被赋值为0，继续走while循环，匹配case 0 代码块，取出‘1’后在yield int_value处暂停
# print(f.send(0)) # 7️⃣ 发送0作为 yield int_value表达式的结果，恢复执行，task_id被赋值为0，继续走while循环，匹配case 0 代码块，取出‘2’后在yield int_value处暂停
# print(f.send(2)) # 8️⃣ 发送2作为 yield int_value表达式的结果，恢复执行，task_id被赋值为2，继续走while循环，匹配case _ 代码块，取出‘None’后在yield None处暂停
# print(f.send(0)) # 9️⃣ 发送0作为 yield None表达式的结果，恢复执行，task_id被赋值为0，继续走while循环，匹配case 0 代码块，取出‘3’后在yield int_value处暂停


f = gen()
# 启动生成器，从生成器中获取数据
# print(next(f))

# send 也可以启动生成器，启动时必须发送None，否则会报错
# print(f.send(None)) # 相当于没有发送值，所以不需要找yield表达式，代码会默认执行case 0代码块，取出0后在yield int_value处暂停
# print(f.send(None)) # 这次发送None后，由于代码暂停在yield int_value处，所以None会作为yield int_value的结果，赋值给task_id，继续走while循环，匹配case _代码块，取出‘None’后在yield None处暂停

print(f.send(1)) # 如果生成器没有被启动，发送1 找不到yield 表达式进行赋值，所以会报错

