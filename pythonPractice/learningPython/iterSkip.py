# coding:UTF-8
class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def next(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

class SkipIteratorwu:
    """
    By test, this is a bad version of the desired function
    Because: 好吧，用中文吧，这里注意当嵌套循环的时候如果不用上面那种
    把next和iter分开来写的方法的话，就会导致偏移无法重新归零，从而在循环
    嵌套的迭代器中，内层循环会不断扩大标志，而不能得到我们想要的效果
    """
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset =0
    def __iter__(self):
        return self
    def next(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print I.next(),I.next(), I.next()

    for x in skipper:
        for y in skipper:
            print x+y,

    wulei = 'wuleishigehaoren'
    wu = SkipIteratorwu(wulei)
    w = iter(wu)
    #print w.next(), w.next(), w.next()

    for x in wu:
        for y in wu:
            print x+y



