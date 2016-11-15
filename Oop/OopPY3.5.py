# oop
class Student(object):
    def stuInfo(self, name, age):
        self.name = name
        self.age = age

    def stuPir(self):
        print('%s,%s' % (self.name, self.age))

    def ageIf(self):
        if self.age > 30 & self.age < 40:
            print('老男人')
        elif self.age > 20 & self.age < 30:
            print('老男孩')
        else:
            print('不符合')


s1 = Student()
s1.stuInfo('zhangsan', 20)
s1.ageIf()
s1.stuPir()


# 私有变量
class Student1(object):
    def stuInfo(self, name, age):
        self.__name = name
        self.age = age

    def stuPir(self):
        print('%s,%s' % (self.__name, self.age))

    def ageIf(self):
        if self.age > 30 & self.age < 40:
            print('老男人')
        elif self.age > 20 & self.age < 30:
            print('老男孩')
        else:
            print('不符合')

    def getName(self):
        return self.name


# 继承和多态

class Animmal(object):
    def speak(self, word):
        print('%s' % (word))


class Cat(Animmal):
    def run(self):
        print('run')


cat = Cat()
cat.speak('miaomiao')
cat.run()


class Dog(Animmal):
    def run(self):
        print('Dog is run')


wangwang = Dog()
wangwang.run()

# 获取类型
# type()
# isinstance
# dir获取该类的所有方法

a = 123
print('下面是打印结果')
print(type(a))

print(type(wangwang))

print(isinstance(wangwang, Dog))

print(isinstance(cat, Dog))

print(dir(Student))

print('分割线')

