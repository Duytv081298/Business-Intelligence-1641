import random,numpy as np  

# a = []
# for i in range(20):
#     a.append(i)

# print(a)

# lhalf = int(len(a)/2)


# print("a) 1st way: ", a[:10])
# print("a) 2st way: ", a[:lhalf])
# print("a) 3st way: ", a[:-10])


# n = int(input('Enter n:'))
# print('b)', a[n: -n])

# print("c)", a[0:n]+ a[-n : ])

# print("a[{0}] = {1}".format(n,a[n]))
# b = []
# while(len(b)<5):
#     a = []
#     for i in range(5):
#         a.append(i) 
#     b.append(a)

# print(b)


# print("a) 1st way: ", b[1:4])
# print("a) 2st way: ", b[1:-1])

# print("b) 1st way:", b[-2:])
# print("b) 2st way:", b[3:])
# print("b) 3st way:", b[3:5])

# n = int(input('Enter n:'))
# print('Max of row {0} = {1:0.2f}'.format(n, max(a[n])))
# print('Min of row {0} = {1:0.2f}'.format(n, min(a[n])))
# print('Sum of row {0} = {1:0.4f}'.format(n, max(a[n])))
# c = b[:n]
# print("c) 2st way:", c[:1], c[-1:])

# 

a= np.ones((8,8))
a[1:-1, 1:-1] = 0
print("a)",a)
print()

b= np.ones((8,8))
b[0::2, 1::2] = 0
b[1::2, 0::2] = 0

print("b) 1st way: ", b)
r1 = [1, 0, 1, 0, 1, 0, 1, 0]
r2 = [0, 1, 0, 1, 0, 1, 0, 1]
b  = [r1, r2, r1, r2, r1, r2, r1, r2]
b  = np.reshape(b, (8, 8)) 
print("b) 2nd way: ", b)




# c)Create an 8x8 array of random intergers, make all the numbers not divisible by 3 negative..
c = np.random.randint(low=-100, high=100, size=(8, 8))
c[c%3!=0] *=-1
print("c) ", c)


q1 = c[:4, :4]
q2 = c[:4, 4:]
q3 = c[4:, :4]
q4 = c[4:, 4:]

print("q1 = \n{0}, size = {1}, shape = {2}, mean = {3}, std = {4}".format(q1, q1.size,q1.shape,np.mean(q1), np.std(q1)))
print("q2 = \n{0}, size = {1}, shape = {2}, mean = {3}, std = {4}".format(q2, q2.size,q2.shape,np.mean(q2), np.std(q2)))
print("q3 = \n{0}, size = {1}, shape = {2}, mean = {3}, std = {4}".format(q3, q3.size,q3.shape,np.mean(q3), np.std(q3)))
print("q4 = \n{0}, size = {1}, shape = {2}, mean = {3}, std = {4}".format(q4, q4.size,q4.shape,np.mean(q4), np.std(q4)))


print("=================================================================================================================")

students= {"Ha": 15, "Tam":14, "Tham":13, "Quyen":16, "Duy": 12}

name = input("Enter name mới: ")
gpa =int(input("Enter GPA")) 
students[name] = gpa
print(students)

print("Student who has max GPA: ", max(students))
print("Student who has max GPA: ", min(students))
print("Mean GPA: ", np.mean(list(students.values()))) # mean trung bình

name = input("Enter name: ")
gpa = input("Enter new GPA")
students[name] = gpa

print(students)

students.pop(name)
print(students)


# inverse = [(value, key) for key, value in students.items()]
# print(max(inverse)[1])




    
    




