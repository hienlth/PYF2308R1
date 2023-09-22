'''
Bài 6: Viết chương trình mô phỏng trò chơi kéo búa bao theo luật chơi như sau:
Quy ước: 1 - búa, 2 - kéo, 3 - bao
Khi trò chơi bắt đầu, yêu cầu người chơi nhập 1 số từ bàn phím đại diện cho kéo, búa, bao
Chương trình tự random ra một lựa chọn từ 1 đến 3.
Nếu người chơi thua thì tiếp tục chơi cho đến khi thắng thì kết thúc chương trình.
Ví dụ:

Mời lựa chọn(1 - búa, 2 - kéo, 3 - bao): 1
Máy tính chọn: 3
Người chơi thua.

Mời lựa chọn(1 - búa, 2 - kéo, 3 - bao): 2
Máy tính chọn: 1
Người chơi thua.

Mời lựa chọn(1 - búa, 2 - kéo, 3 - bao): 1
Máy tính chọn: 2
Người chơi thắng.
'''
from random import randint

print('BÚA - KÉO - BAO')
lua_chon = int(input('Mời lựa chọn(1 - búa, 2 - kéo, 3 - bao): '))
may_chon = randint(1, 3)
print(f"Máy tính chọn: {may_chon}")

if lua_chon == may_chon:
    print('Hòa')
else:
    if lua_chon == 1: # Búa
        print("Người chơi thắng" if may_chon == 2 else "Máy thắng")
    elif lua_chon == 2: # Kéo
        print("Người chơi thắng" if may_chon == 3 else "Máy thắng")
    elif lua_chon == 3: # Bao
        print("Người chơi thắng" if may_chon == 1 else "Máy thắng")