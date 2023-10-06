'''Viết hàm find_distance() nhận vào 4 tham số x1, y1, x2, y2 là tọa độ của 2 điểm trên trục tọa độ và in ra khoảng cách của 2 điểm đó theo công thức:
find_distance = sqrt((x1-x2)^2 + (y1-y2)^2)
'''
from math import sqrt

def find_distance(x1, y1, x2, y2):
    '''Get distance between A(x1, y1) and B(x2, y2).'''
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# find_distance(0, 0, 4, 5)
print(find_distance(0, 0, 4, 5))
print(sqrt(7))