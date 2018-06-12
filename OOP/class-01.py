'''
定义一个学生类，用来形容学生
'''

class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
mingyue = Student()

# 再定义一个类，用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1. def DoHomework的缩进层级
    # 2. 系统默认由一个self参数
    def DoHomework(self):
        print("i'm doing homework")

        # 推荐在函数末尾使用return语句
        return None
# 实例
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员杉树的调用没有传递进入参数
yueyue.DoHomework()
