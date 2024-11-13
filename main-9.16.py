num_list = input().split()

nega_num = []

for num in num_list:
    if int(num) < 0:
        nega_num.append(int(num))

nega_num.sort(reverse = True)

for item in nega_num:
    print(item, end=' ')
