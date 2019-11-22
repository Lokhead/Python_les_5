file_a = open('dz5_new.txt', 'w+', encoding='UTF-8')
file_a.write('10 23 34 17 56 29')
file_a.seek(0)
nums = file_a.readline().split()
file_a.close()
nums_i = list()
for el in nums:
    nums_i.append(int(el))
print(sum(nums_i))
