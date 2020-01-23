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



# res_index = mas2.index()

# print(sum(res_index))
# print(mas2)


# import copy
# masA = [134, 32, 24, 52, 231, 532, 64, 42, 1, 3, 42, 42]
# masB = copy.deepcopy(masA)

masA = [134, 32, 24, 52, 231, 532, 64, 42, 1, 3, 42, 42]
masB = [134, 32, 24, 52, 231, 532, 64, 42, 1, 3, 42, 42]

masA.sort()
masB.sort()

masC = masA.extend(masB)

print(masC)