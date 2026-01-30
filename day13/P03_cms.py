"""
    客户管理系统 CMS
"""
import sys

from P02_customer import Customer

menu_width = 30
class CMS:
    def __init__(self):
        # 定义存储客户的容器
        self.customer_id_dict = {}
        self.customer_name_dict = {}

    def start(self):
        while True:
            self.display_menu()

            menu= input("请输入您要进行的操作：")
            match menu:
                case "1":
                    self.add_customer()
                case "2":
                    print("删除客户")
                case "3":
                    print("修改客户")
                case "4":
                    print("查询客户")
                case "5":
                    print("显示所有客户")
                case "6":
                    sys.exit()
                case _:
                    print("输入不合理，请重新输入")

    def display_menu(self):
        print(f"{'~~~~~~~~~~客户管理系统~~~~~~~~~~':^{menu_width}}")
        print(f"{'1.添加客户':^{menu_width}}")
        print(f"{'2.删除客户':^{menu_width}}")
        print(f"{'3.修改客户':^{menu_width}}")
        print(f"{'4.查询客户':^{menu_width}}")
        print(f"{'5.显示所有客户':^{menu_width}}")
        print(f"{'6.退出系统':^{menu_width}}")
        print(f"{'~~~~~~~~~~~~~~~~~~~~~~~~~~~~':^{menu_width}}")

    def add_customer(self):
        customer_id = self.add_customer_id()
        customer_name = ""
        customer_age = 0
        customer_phone = ""
        customer_email = ""

        customer = Customer(customer_id, customer_name, customer_age, customer_phone, customer_email)

        self.customer_id_dict[customer_id] = customer
        customer_name_inner_dict = self.customer_name_dict.get(customer_name)
        if customer_name_inner_dict:
            customer_name_inner_dict[customer_id] = customer
        else:
            self.customer_name_dict[customer_name] = {customer_id: customer}

        print(f"{'添加成功！':^{menu_width}}")

    def add_customer_id(self):
        for i in range(3):
            if i < 2:
                customer_id = input("请输入客户的ID:")
                if Customer.check_id(customer_id):
                    break
                else:
                    print("客户的ID必须为纯数字")
            else:
                customer_id = input("最后一次机会，请输入正确的客户ID:")
                if Customer.check_id(customer_id):
                    break
                else:
                    print("机会耗尽，放弃添加客户")
                    return False

        if customer_id in self.customer_id_dict:
            print("当前客户ID已经存在，放弃添加客户")
            return False
        return customer_id



if __name__ == "__main__":
    cms = CMS()
    cms.start()
