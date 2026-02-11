
def odd():
    print("number is odd")


def even():
    print("number is even")

def even_odd(a):
    if a%2==0:
        return even()
    else:
        return odd()
    
num=int(input("enter number to check whether its odd /even:\n"))
result=even_odd(num)