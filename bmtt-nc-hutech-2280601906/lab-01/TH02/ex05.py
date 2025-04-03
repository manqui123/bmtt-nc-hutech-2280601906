so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input('Nhập thù lao sau mỗi giờ làm tiêu chuẩn: '))
gio_tieu_chuan = 25 #số giờ làm chuẩn mỗi tuần
gio_vuot_chuan = max(0,so_gio_lam - gio_tieu_chuan) #Số giờ làm vượt mỗi tuần
thuc_linh = gio_tieu_chuan *luong_gio + gio_vuot_chuan*luong_gio*1.5 # Tính lương thu nhập
print(f'Số tiền thực lĩnh của nhân viên:{thuc_linh}')
