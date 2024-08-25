# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:25:12 2024

@author: DiemKieu
"""

print("======MENU======")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("================")
lua_chon=input("Moi nhap lua chon:")
print("================")
if lua_chon == '1':
    print("Chon Hu tieu")
elif lua_chon == '2':
    print("Chon Chao long")
elif lua_chon == '3':
    print("Chon Banh canh")
elif lua_chon == '4':
    print("Chon Bun rieu")
elif lua_chon == '5':
    print("Chon Pho bo")
else:
    print("Không chọn ăn gì cả")