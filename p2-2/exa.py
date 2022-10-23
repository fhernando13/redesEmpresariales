def fununo(a):
    return a ** a

def fundos(a):
    return fununo(1)*fununo(a)

print(fundos(2))