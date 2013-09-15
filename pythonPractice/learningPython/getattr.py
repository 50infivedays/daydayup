# coding: UTF-8

class empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError, attrname

if __name__ == '__main__':
    x = empty()
    print x.age
    print x.gender

