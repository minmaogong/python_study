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
                    self.delete_customer()
                case "3":
                    print("修改客户")
                case "4":
                    self.search_customer()
                case "5":
                    self.display_all_customer()
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
        if not (customer_id := self.add_customer_id()):
            return
        if not (customer_name := self.add_customer_name()):
            return
        customer_age = self.set_customer_age()
        customer_phone = self.set_customer_phone()
        customer_email = self.set_customer_email()

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

    def add_customer_name(self):
        for i in range(3):
            if i < 2:
                customer_name = input("请输入客户的姓名:")
                if Customer.check_name(customer_name):
                    break
                else:
                    print("客户姓名必须是纯字母")
            else:
                customer_name = input("最后一次机会，请珍惜！请输入客户姓名:")
                if Customer.check_name(customer_name):
                    break
                else:
                    print("机会耗尽，终止添加客户")
                    return False
        return customer_name

    def set_customer_age(self):
        age = input("请输入客户年龄:")
        if Customer.check_age(age):
            return age
        else:
            print("年龄不合法，使用默认值")
            return "None"

    def set_customer_phone(self):
        phone = input("请输入客户手机号:")
        if Customer.check_phone(phone):
            return phone
        else:
            print("手机号不合法，使用默认值")
            return "None"

    def set_customer_email(self):
        email = input("请输入客户邮箱:")
        if Customer.check_email(email):
            return email
        else:
            print("邮箱不合法，使用默认值")
            return "None"

    def display_all_customer(self):
        if len(self.customer_id_dict) == 0:
            print("暂时还没有客户")
        else:
            for customer in self.customer_id_dict.values():
                print(customer)

    def search_customer(self):
        self.display_search_menu()


    def display_search_menu(self):
        print(f"{'~~~~~~~~~~4.查询客户~~~~~~~~~~':^{menu_width}}")
        print(f"{'1.通过ID查询':^{menu_width}}")
        print(f"{'2.通过姓名查询':^{menu_width}}")
        print(f"{'3.取消查询':^{menu_width}}")
        print(f"{'~~~~~~~~~~~~~~~~~~~~~~~~~~~~':^{menu_width}}")

        search_menu = input("请输入您要进行的操作")
        match search_menu:
            case "1":
                self.search_customer_by_id()
                pass
            case "2":
                self.search_customer_by_name()
                pass
            case _:
                return

    def search_customer_by_id(self):
        customer_id = input("请输入查询客户的ID:")
        if customer_id not in self.customer_id_dict:
            print(f"未查询到ID为 {customer_id} 的客户")
        else:
            print(self.customer_id_dict[customer_id])

    def search_customer_by_name(self):
        customer_name = input("请输入查询客户的姓名:")
        if customer_name not in self.customer_name_dict:
            print(f"未查询到姓名为 {customer_name} 的客户")
        else:
            customer_dict = self.customer_name_dict.get(customer_name)
            for customer in customer_dict.values():
                print(customer)

    def delete_customer(self):
        customer_id = input("请输入删除客户的ID:")
        if customer_id not in self.customer_id_dict:
            print("系统中不存在该客户")
        else:
            customer = self.customer_id_dict.get(customer_id)
            self.customer_id_dict.pop(customer_id)
            self.customer_name_dict[customer.name].pop(customer_id)
            print("删除成功")


if __name__ == "__main__":
    cms = CMS()
    cms.start()
