def in_thong_tiet_kiem(so_tien_gui, so_nam, lai_suat):
    tien_tich_luy = so_tien_gui
    for nam in range(1, so_nam + 1):
        tien_lai = tien_tich_luy * lai_suat
        print(f"Năm {nam}: Lãi: {tien_tich_luy}đ x {lai_suat * 100}% = {tien_lai}đ,"
              + f"tiền tích lũy = {tien_tich_luy} + {tien_lai} = {tien_tich_luy + tien_lai}đ")
        tien_tich_luy += tien_lai

in_thong_tiet_kiem(10000000, 3, 0.05)