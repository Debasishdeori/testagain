a = [1,2,3,4]
def fin_val(a):
    a[0] = 5
    a[1] = 6
    a[2] = 7
    a[3] = 8

    print("Values inside the function:",a)

print("Values before the function:",a)
fin_val(a)
print("Values after the function:",a)