# a = complex(2, 3)
# b = complex(3, 2)
# print(a / b)
def rfe(x):
    x[0] = x[0] * 2
x = [5, 6]
rfe(x), rfe(x)
print(x)