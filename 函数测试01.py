#coding:gb2312
import os
import glob
# current_file = os.path.realpath(__file__)#��ȡ��ǰ�ļ���·��
# path01 = "D:\Personal_project\Python"
# if os.path.exists(path01):
#     print("·�����ڣ��ļ�����")
#     list01 = glob.glob(f"{path01}/*App*")
# else:
#     print("·�������ڣ��ļ�������")

# print(list01)
# print(f"\n��ǰ�ļ���·���� %s"%current_file)

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

value01 = input("�����������ͣ�")
print(f"��ֵ��{case01(value01)}")