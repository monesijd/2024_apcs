mylist = list()
for i in range(2, 100000):
    mylist.append(i**2)

number = int(input())
for _ in range(number):
    length = int(input())

    for each_num in mylist:
        if len(str(each_num)) == length:

            for each_chr in str(each_num):
                if int(each_chr) % 2 != 0:
                    break
            else:
                print(each_num)
                break
