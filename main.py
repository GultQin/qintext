def show_example(word): #定义函数
    print(word)
#再在主函数中调用
result=lambda x :x*x
def a():

    print("one")
def b():
    print("two")
def c():
    a()
    b()
def use(n):
    if n==1:
        return 1
    else:
        return n+ use(n-1)
if __name__ == '__main__':#主函数
    c()
    n=10
    print(use(n))





