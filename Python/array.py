import numpy as np
# a = np.linspace(0, 20, num=10, dtype=int, endpoint=False)
# print(a)

# b = np.arange(0,20,20/10, dtype=int)
# print(b)

# c = np.random.randint(0,100,20,dtype=int)
# print(c)

# d = c[c%2==0]
# d.sort()
# print(d)

# e = np.concatenate([c[c%2!=0],c[c%2==0]])
# e.sort()
# print(e)

print("===============================================================================================")

# y = np.array([0., 1.3, 5. , 10.9, 18.9, 28.7, 40.])
# t = np.array([0., 0.49, 1. , 1.5 , 2.08, 2.55, 3.2])


# # y1 = y[:-1]
# # vt = y - y1

# # t1 = t[:-1]
# # vd = t-t1

# v=(y[1:]-y[:-1])/(t[1:]-t[:-1])
# print(v)


print("===============================================================================================")

name = np.array(["Quyen", "Duy","","","",])
tuoi = np.array([-150, -60, -30, 180, 200])

name[name == ""] = "ha"
print(name)

tuoi[tuoi <0] = 0
tuoi[tuoi >150] = 150
print(tuoi)

print("Longest name", max(name, key=len))
print("Shortest name", min(name, key=len))

print("longest name size = ", max(list(map(len,name))))
print("Shortest name size = ", min(list(map(len,name))))

print("===============================================================================================")

a = np.linspace(0, 0, num=10, dtype=int, endpoint=False)
i=0
while i>10 :
    a+=a
    i =i+1
print(a)