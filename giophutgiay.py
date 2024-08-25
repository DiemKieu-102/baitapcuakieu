# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:54:43 2024

@author: DiemKieu
"""

# Nhập thời gian và tách các giá trị
hh, mm, ss = map(int, input("Nhập thời gian (hh:mm:ss): ").split(':'))
# Tính tổng số giây
sum = hh* 3600 + mm * 60 + ss
# In kết quả
print(sum)