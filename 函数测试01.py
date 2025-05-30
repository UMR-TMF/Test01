#coding:gb2312
import os
import glob
# current_file = os.path.realpath(__file__)#获取当前文件的路径
# path01 = "D:\Personal_project\Python"
# if os.path.exists(path01):
#     print("路径存在，文件存在")
#     list01 = glob.glob(f"{path01}/*App*")
# else:
#     print("路径不存在，文件不存在")

# print(list01)
# print(f"\n当前文件的路径是 %s"%current_file)

def func_1():
    a =10
    b = 11
    return a+b

def func_2():
    a =11
    b = 12
    return a+b

def case01(s):
    map = {"app01":func_1,"app02":func_2}
    return map[s]()

value01 = input("输入数据类型：")
print(f"数值是{case01(value01)}")