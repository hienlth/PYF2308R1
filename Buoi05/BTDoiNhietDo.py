'''
Mô tả:
Viết chương trình nhập một giá trị là độ °C (Celsius) và chuyển nó sang độ °F (Fahrenheit).

Gợi ý các bước thực hiện:
+ Nhập vào giá trị độ °C muốn chuyển đổi
+ Tính độ °F tương ứng qua công thức:
    °F  =  ( °C × 1.8 ) +  32
+ Hiển thị độ °F (In ra màn hình)
'''
try:
    do_C = float(input("Nhập vào độ C:"))
    do_F = ( do_C * 1.8 ) +  32
    print("Độ F tương ứng là: ", do_F, "°F")
except:
    print('Lỗi')
  
print("END")