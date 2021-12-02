def group_increase(data_list):
    count = 0
    res = 0
    data_list = [int(i) for i in data_list]
    len_data = len(data_list)
    for x in data_list:
        if count < len_data - 3:
            x2 = data_list[count + 1]
            x3 = data_list[count + 2]
            x4 = data_list[count + 3]
            res1 = x + x2 + x3
            res2 = x2 + x3 + x4
            if res2 > res1:
                res = res + 1
        count = count + 1
    return (res)

f = open("d01.txt", "r")
data =  f.read()
data_list = data.splitlines()
f.close()

print(group_increase(data_list))