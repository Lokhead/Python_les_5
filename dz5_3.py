file_a = open('dz3.txt', encoding='UTF-8')
nums = list()
for line_a in file_a:
    line_b = list(line_a.split())
    if int(line_b[1]) < 20000:
        print(line_b[0])
    nums.append(int(line_b[1]))
print(f'Средний доход сотрудников: {sum(nums) / len(nums)}')
file_a.close()
