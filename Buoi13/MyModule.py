LUONG_CO_BAN = 1800

def tinh_tong(n):
    return 10 ** n // (10 + n)

def greeting(name):
    print("Hello, " + name)

class HinhChuNhat:
    def __init__(self, x, y): # Method - contructor
        self.Dai = x
        self.Rong = y