内容备忘
========
## iteration.py
    文件描写了如何修改循环迭代器，
## iterSkip.py
    相对于上一个文件增加了在嵌套迭代时如何编写迭代器
    注意把iter和next分开写这种方法
## getattr.py
    当进行属性读取操作（点操作）时，会自动调用__getattr__方法，属性名就是函数的参数
## setattr.py
    当类属性赋值操作时，会被展开为self.__setattr__('attr',value),注意这个函数中的任何
    属性赋值操作都会导致无限递

