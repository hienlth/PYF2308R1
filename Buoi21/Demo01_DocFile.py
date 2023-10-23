myfile = open("workinghours.txt", encoding="utf8")

# Đọc file
lines = myfile.readlines()
print(lines)
myfile.close()

for line in lines:
    # print(line)
    data = line.split()
    print("Đọc được và phân tách:", data)
    hours = list(map(lambda item: float(item), data[2:]))
    print(data[0], data[1], sum(hours))

    # total_hours = 0
    # for item in data[2:]:
    #     total_hours += float(item)