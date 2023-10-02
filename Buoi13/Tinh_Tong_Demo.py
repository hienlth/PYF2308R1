def sum_even(n):
    # code below this line
    sum = 0
    
    for num in range(2, n + 1, 2):
        sum += num
    
    return sum
    # code above this line

gia_tri = sum_even(11)
print(gia_tri)
print(sum_even(121))
print(sum_even(12) + 5)