'''Nhập vào chiều cao (cm) và cân nặng (kg), tính số BMI và xét rồi xin kết quả theo dữ liệu sau:
# BMI = cân nặng / (chiều cao ^ 2)
BMI < 16: Gầy cấp độ III
16 <= BMI < 17: Gầy cấp độ II
17<= BMI < 18.5: Gầy cấp độ I
18.5 <= BMI < 25: Bình thường
25 <= BMI < 30: Thừa cân
30 <= BMI < 35 : Béo phì cấp độ I
35 <= BMI < 40: Béo phì cấp độ II
BMI > 40: Béo phì cấp độ III'''

chieu_cao = int(input("Nhập chiều cao (cm): ")) / 100
can_nang = float(input("Nhập cân nặng (kq): "))

BMI = can_nang / (chieu_cao ** 2)
print(f"Nặng: {can_nang} kg, cao: {chieu_cao} m, BMI={BMI}")

if BMI < 16:
    print("Gay cap do III")
elif BMI < 17:
    print("Gay cap do II")
elif BMI < 18.5:
    print("Gay cap do I")
elif BMI < 25:
    print("Binh thuong")
elif BMI < 30:
    print("Thua can")
elif BMI < 35:
    print("Beo phi cap do I")
elif BMI < 40:
    print("Beo phi cap do II")
else:
    print("Beo phi cap do III")
