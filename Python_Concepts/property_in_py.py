class Person:
    def __init__(self, name):
        self.__name = name

    def setname(self, name):
        print('set name : ', name)
        self.__name = name

    def getname(self):
        print('get name')
        return self.__name

    name = property(getname, setname)


p1 = Person('cal')
p1.getname()
p1.setname('net')
# -----------------
print('-'*10, 'Using property func ', '-'*10)
p2 = Person('dhule')
print(p2.name)
p2.name = 'pune'
# -----------------
print('-'*10, 'Using property decorator ', '-'*10)


class Language:
    def __init__(self, lang):
        self.__lang = lang

    @property
    def lang(self):
        print('get lang')
        return self.__lang

    @lang.setter
    def lang(self, lang):
        print('set lang : ', lang)
        self.__lang = lang


p3 = Language('Perl')
p3.lang
p3.lang = 'python'

