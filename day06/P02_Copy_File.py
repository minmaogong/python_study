"""
    文件拷贝
"""

"""
# source_file_path  源文件路径
# dest_file_path    目标文件路径
def copy_file(source_file_path, dest_file_path):
    # 1.从源读取数据
    # 打开源文件
    source_file = open(source_file_path, "rb")
    # 打开目标文件
    dest_file = open(dest_file_path, "wb")

    # 2.将读取书写入到文件
    content = source_file.read()
    dest_file.write(content)

    # 3.关闭
    source_file.close()
    dest_file.close()


copy_file("F:\\11.heic", "G:\\22.heic")
# copy_file(r"F:\11.heic", r"G:\22.heic")
"""

"""
# 优化1：读取指定的字节，然后将读取额字节写到目标文件
def copy_file(source_file_path, dest_file_path):
    source_file = open(source_file_path, "rb")
    dest_file = open(dest_file_path, "wb")

    content = source_file.read(1024)
    while content:
        dest_file.write(content)
        content = source_file.read(1024)

    source_file.close()
    dest_file.close()
"""


# 优化2：海象运算符
def copy_file(source_file_path, dest_file_path):
    source_file = open(source_file_path, "rb")
    dest_file = open(dest_file_path, "wb")

    while content := source_file.read(1024):
        dest_file.write(content)

    source_file.close()
    dest_file.close()

