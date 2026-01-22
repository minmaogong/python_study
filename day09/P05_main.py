"""
    带包模块导入
    1.全局导入
        导入包中模块的所有成员
        import 包名.模块名 [as 别名]
    2.局部导入
        局部导入包下的模块 from import
            from 包名 import 模块名 [as 别名]
        局部导入包下模块的成员 from import
            from 包名.模块名 import 成员名 [as 别名]
        局部导入 from import * 从包中导入模块
            from 包名.模块名 import *

"""

# 全局导入
"""
import graphic.circle

print(graphic.circle.PI)
"""
"""
import graphic.circle as c

print(c.PI)
"""
"""
import graphic

print(graphic.circle.PI)
"""



# 局部导入
# 局部导入包下的模块 from import
"""
from graphic import rectangle

print(rectangle.rectangle_width)
"""

# 局部导入包下模块的成员 from import
"""
from graphic.circle import area

print(area(10))
"""

# 局部导入 from import * 从包中导入模块
from graphic import *

print(circle.PI)