import random,numpy as np  
# a = []
# for i in range(20):
#     a.append(random.randint(0,100))
# print("List random: \n",a)

# print(type(a))


# b =[]
# for x in a: 
#     if x > 50: 
#         b.append(x)
        
# print("List giá trị lớn hơn 50: \n",b)

# c = []
# avg= 0
# for i in enumerate(a):
#     avg = sum(a) / len(a) 

# for x in a: 
#     if x > avg: 
#         c.append(x)
# print("List giá trị lớn hơn 50 giá trị trung bình: \n",c)

# d = []

# for x in a: 
#     if x%2 ==0: 
#         d.append(x)
# print("List các số chẵn: \n",d)

# e= []
# f = []
# for x in a: 
#     if x%2 ==0 : 
#         e.append(x)
#     else:
#         f.append(x)
# g=e+f
# print("List sắp xếp chẵn trước lẻ sau: \n",g)


print("==============================================================")
s = "hello"
v = 5
t = (1, 5)
l =["a", "b", "c"]
a = np.array([4,6,3])

print(s,v,t,l,a)
def test(s,v,t,l,a):
    s = "Chao"
    v = np.pi**2
    t = (1.1, 2.9)
    l[-1] ="end"
    a[0] = 9
    return s,v,t,l,a

s1, v1, t1, l1,a1 = test(s,v,t,l,a)

print(s1,v1,t1,l1,a1)
print(s,v,t,l,a)

print("==============================================================")
def test1(*p):
    print("Original numbers: ", p)
    print("Inverse numbers: ", end= "")
    for n in p:
        n = 1/n
        print(n, end= " ")


def test2(*p):
    print("Original numbers: ", p)
    print("Inverse numbers: ", end= "")
    for n in p:
        n = 1/n
    print("Original numbers: ", p)


test1(1.5,3,7)
print("\n==============================================================")
test2(1.5,3,7)
print("\n\n\n==============================================================")
def su_ly_data(value, su_ly_so_nho, su_ly_so_lon ):
    su_ly_so_nho(value)
    su_ly_so_lon(value)
def bang_zeros(value):
    value[np.abs(value)<1.e-5] = 0
def nhan_10(value):
    value[np.abs(value)<1.e-5] *= 10
def chia_2(value):
    value[np.abs(value)<1.e+5] /= 2
def lay_can(value):
    value[np.abs(value)<1.e+5] **= 0.5  # Căn bậc 2

a = np.array([1.e-6, -1.e-7, 3., 100., 3.e+6, 2019])
np.set_printoptions(precision=1)

print("original data: ", a)
su_ly_data(a, nhan_10, chia_2)
print("1st preprocess:", a)
su_ly_data(a,bang_zeros, lay_can)
print("2st preprocess:", a)



