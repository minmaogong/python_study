"""
    正则表达式
"""
import  re
text = "adbcef123456"
# r: 忽略转义，使用原始字符
print(re.search(r"\w+", text)) # 相当于[a-zA-Z0-9_]+


test = [
    "13812345678", # 合法
    "11456817239", # 非法
    "19912345678", # 合法
    "17138412356", # 合法
    "1234567890", # 非法
    "14752345673", # 合法
    "1800123456" # 非法
]

# 以1开头，第二位为3，4，5，7，8，9，后面是9位数字
pattern = r"^1[345789]\d{9}$" # ^: 以1开始 [345789]: 第二位从这些里匹配一个 \d: 0-9整数 {9}: 出现9次 $: 结束
for i in test:
    print(f"{i:20}{'合法' if re.match(pattern, i) else '非法'}")


test1 = [
    "example@example.com",
    "user.name@subdomain.example.co",
    "username@.com",
    "@missingusername.com",
    "-dasd@qq.com"
]
# 匹配邮箱
pattern = r"[\w]+@[\w]+\.[a-zA-Z]{2,}$" # .: 任意字符 \.: 转义后普通点
for i in test1:
    print(f"{i:20}{'合法' if re.match(pattern, i) else '非法'}")


# 匹配出 0-255 之间的数字
test2 = ["0", "9", "50", "100", "199", "200", "255", "256", "-1", "01", "001"]
# 十位为1-9，?表示可以没有十位，个位是0-9 # [1-9]?\d
# 或 百位是1， 十位是0-9，个位是0-9 # 1\d{2}
# 或 百位是2， 十位是0-4，个位是0-9 # 2[0-4]\d
# 或 百位是2， 十位是5， 个位是0-5 # 25[0-5]
pattern = r"^([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])$"
for i in test2:
    print(f"{i:20}{'合法' if re.match(pattern, i) else '非法'}")



test3 = """<link rel="alternate" hreflang="zh" href="https://zh.wikipedia.org/wiki/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hans" href="https://zh.wikipedia.org/zh-hans/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hans-CN" href="https://zh.wikipedia.org/zh-cn/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hans-MY" href="https://zh.wikipedia.org/zh-my/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hans-SG" href="https://zh.wikipedia.org/zh-sg/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hant" href="https://zh.wikipedia.org/zh-hant/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hant-HK" href="https://zh.wikipedia.org/zh-hk/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hant-MO" href="https://zh.wikipedia.org/zh-mo/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hant-TW" href="https://zh.wikipedia.org/zh-tw/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="x-default" href="https://zh.wikipedia.org/wiki/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">"""

# 获取所有href中网址
pattern = r"href=\"(.+?)\"" # 这里的?表示的是非贪婪匹配
for i in re.findall(pattern, test3):
    print(i)


# 替换文本中的所有数字为对应的词
test4 = "I have 2 apples and 3 oranges."
# 定义数字到词的映射
num_map = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven"}
# re.sub 替换逻辑：
# 1. r"\d"：正则表达式，匹配任意单个数字（0-9）
# 2. lambda x: num_map[x.group(0)]：替换函数，接收匹配对象x，x.group(0)获取匹配到的数字字符串（如"2"），再从num_map取对应值
# 3. test4：要处理的原始字符串
print(re.sub(r"\d", lambda x: num_map[x.group(0)], test4)) # 匹配到一次，就会调用一次lambda表达式。lambda表达式中的x就是每一次匹配到的结果。通过x.group(0)从匹配结果获取匹配到的数字字符串。再从map应用中找到对应的值，作为替换数字的对象
