from distutils.core import setup

setup(
    name="graphic", # 需要打包的名字
    version="0.1", # 版本
    py_modules=["graphic.circle", "graphic.rectangle"], # 需要打包的模块
)

# python setup.py build   # 生成build目录
# python setup.py sdist   # 压缩build目录，生成压缩文件