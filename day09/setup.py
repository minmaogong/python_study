from distutils.core import setup

setup(
    name="graphic", # 需要打包的名字
    version="0.1", # 版本
    py_modules=["graphic.circle", "graphic.rectangle"], # 需要打包的模块
)