'''
Bài 4: Viết chương trình nhập vào một số nguyên n và in ra các số từ 1 đến n với các trường hợp ngoại lệ như sau:
- Nếu số đó chia hết cho 3 thì in "py"
- Nếu số đó chia hết cho 7 thì in "thon"
- Nếu số đó chia hết cho cả 3 và 7 thì in "python"
'''
n = int(input("Please input n: "))

i = 1 
while i <= n:
    if i % 21 == 0:
        print("python") 
    elif i % 3 == 0:
        print("py")
    elif i % 7 == 0:
        print("thon")
    else:
        print(i)
    
    i += 1
