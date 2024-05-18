a=4
b=3

try:
    ans=a/b
    print(ans)
except ZeroDivisionError:
    print("wrong input. divisor can not be zero.")
except:
    print("something went wrong.")
finally:
    print("It will always run.")