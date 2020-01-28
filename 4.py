# Arr = [1, 42, 16 ,8]

# print(Arr)

# Arr.append(28)

# print(Arr)

# Arr.insert(2, 100500)

# print(Arr)

# Arr.remove(100500)

# print(Arr)

# Arr.clear()

# print(Arr)

# Arr.append(14)
# Arr.append(34)
# Arr.append(14)
# Arr.append(54)
# Arr.append(14)
# print(Arr)

# # print(Arr.index(54))

# Arr.pop(1)

# print(Arr)

# print(Arr.count(14))

# Arr.append("Microsoft")

# print(Arr)

# # Arr.sort()

# # print(Arr)

# Arr.reverse()

# print(Arr)

# print(len(Arr))

# Arr.remove("Microsoft")

# print(min(Arr))

# print(max(Arr))

# print(" ")

# for item in Arr:
#     print(item)


# names = ["Dima", "Kamila", "Bob", "Mike", "Jhon" ]
# names.sort()
# for item in names:
#     print(item)


# import copy

# names1 = ["Tom", "Jim", "Bill", "Jack", "Oliver", "Julya"]

# names2 = copy.deepcopy(names1)
# # names2 = names1
# names2.append("Steave")

# names3 = names1[3:5]

# print("names1", names1)
# print("names2", names2)
# print("names3", names3)






#1

# mas1 = [134, 32, 24, 52, 231, 532, 64, 42, 1, 3, 42, 42]

# print(mas1)
# min_value = min(mas1)
# max_value = max(mas1)
# min_index = mas1.index(min_value)
# max_index = mas1.index(max_value)

# print("min_value", min_value)
# print("max_value", max_value)
# print("min_index", min_index)
# print("max_index", max_index)

# temp = mas1[min_index]
# mas1[min_index] = mas1[max_index]
# mas1[max_index] = temp

# print(mas1)




# 2

# mas2 = [134, 32, 24, 52, 231, 532, 64, 42, 1, 3, 42, 42]

# print(sum(mas2[1::2]))




# 3

# res_index = mas2.index()

# print(sum(res_index))
# print(mas2)




# 4

# import copy
# masA = [134, 32, 24, 52, 231, 532, 64, 42, 1, 3, 42, 42]
# masB = copy.deepcopy(masA)




# 5

# masA = [134, 32, 24, 52, 231, 532, 64, 42, 1, 3, 42, 42]
# masB = [134, 32, 24, 52, 231, 532, 64, 42, 1, 3, 42, 42]

# masA.sort()
# masB.sort()

# masC = masA + masB

# print(masC)




# • • • • • • • • 
# • HOME  WORK  •
# • • • • • • • • 


# Задача №1 / №2

# from random import randint

# mas1 = [randint(-123, 123) for i in range(13)]

# minN = min(mas1)
# maxN = max(mas1)
# minN_index = mas1.index(minN)
# maxN_index = mas1.index(maxN)

# print(mas1)

# print("minN", minN)
# print("maxN", maxN, "\n")

# print("minN_index ", minN_index)
# print("maxN_index ", maxN_index, "\n")

# minimal = mas1[minN_index]

# mas1[minN_index] = mas1[maxN_index]
# mas1[maxN_index] = minimal

# print("список з поміняними числами ", mas1)




# Задача №3 
#треба було б якось через цикл
#//////// i = 0
# while i < len(companies):
#     print(companies[i])
#     i += 1 ) //////


# from random import randint

# mas2 = [randint(1, 100) for i in range(10)]

# print(mas2, " - простий список \n")

# in1 = mas2[1]
# mas2[1] = mas2[0]
# mas2[0] = in1

# in3 = mas2[3]
# mas2[3] = mas2[2]
# mas2[2] = in3

# in5 = mas2[5]
# mas2[5] = mas2[4]
# mas2[4] = in5

# in7 = mas2[7]
# mas2[7] = mas2[6]
# mas2[6] = in7

# in9 = mas2[9]
# mas2[9] = mas2[8]
# mas2[8] = in9

# print(mas2, " - змінений список \n")




# Завдання №4

# A = list(range(12, 36, 2))
# B = A[:6]
# C = A[6:12]

# print(A, " - список А \n")
# print(B, " - список B \n")
# print(C, " - список C \n")