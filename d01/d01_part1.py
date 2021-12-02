def increases(data_list):

    res = 0
    count = 0
    data_list = [int(i) for i in data_list]
    len_data = len(data_list)
    for x in data_list:
        if (count < len_data - 1):
            next = data_list[count + 1]
            if (next > x):
                res = res + 1
        count = count + 1
    return(res)

f = open("d01.txt", "r")
data = f.read()
data_list = data.splitlines()
f.close()

print(increases(data_list))