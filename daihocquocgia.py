# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:17:25 2024

@author: DiemKieu
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
chuoia = [s.strip() for s in chuoi.split(",")]
#danh sach 1
danhsach1 = chuoia 

#danh sach 2 
chuoi= chuoi.replace("P.", "").replace("Q.","").replace("Tp.","")
chuoi= [s.strip() for s in chuoi.split(",")]
print("Danh sach 1:")
for item in danhsach1:
    print(item)
print("Danh sach 2:")
for item in chuoi:
    print(item)
    