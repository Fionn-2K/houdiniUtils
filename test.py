
# set param and return type
def addition(a: int, b: int) -> int:
    return a + b

res1 = addition(7, 4)
print(res1)
res2 = addition(12.0, 9.2) ## will result in an error. As test methods input params need to be an int
print(res2)