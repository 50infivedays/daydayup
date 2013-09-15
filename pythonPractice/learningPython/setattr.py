class accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError, attr+ 'not allowed'

if __name__ == '__main__':
    x = accesscontrol()
    x.age = 40
    print x.age
    x.name = 'mel'
