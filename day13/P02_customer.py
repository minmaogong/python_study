"""
    客户类
"""
import re

class Customer:
    def __init__(self, id, name, age="None", phone="None", email="None"):
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    def __str__(self):
        # :<15 格式化 < 表示左对齐；^表示居中; > 表示右对齐  15表示 宽度限制，指定格式化后的内容占据15个字符的宽度
        return f"ID:{self.id:<15} name:{self.name:<15} age:{self.age:<15} phone:{self.phone:<15} email:{self.email:<15}"

    @staticmethod
    def check_id(id):
        return id.isdigit()

    @staticmethod
    def check_name(name):
        return name.isalpha()

    @staticmethod
    def check_age(age):
        return age.isdigit()

    @staticmethod
    def check_phone(phone):
        pattern = r"^1[345789]\d{9}$"
        return True if re.match(pattern, phone) else False

    @staticmethod
    def check_email(email):
        pattern = r"[\w]+@[\w]+\.[a-zA-Z]{2,}$"
        return True if re.match(pattern, email) else False


