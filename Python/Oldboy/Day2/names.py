# -*- coding: utf-8 -*-
"""-------------------------------------------------
   File Name：     names
   Description :
   Author :        PjPgy
   date：          2018/1/28 0028
-------------------------------------------------"""

import  copy

#names = "ZhangYang GuYun XiangPeng XuLiuChen"

names = ["ZhangYang","GuYun",["zhang3","li4"],"XiangPeng","XuLiuChen"]

print(names[0:-1:2])
print(names[::2])
#for name in names:
  #print(name)


'''
names2 = names.copy()

names3 = copy.deepcopy(names)
names4 = copy.copy(names)

print(names)
print(names3)

names[0]="张鹏"
names[2][0]="张三"

print(names)
print(names3)
'''

#print(names)
#print(names[0],names[2])
#print(names[1:3]) # 切片 顾头不顾尾
#print(names[-1])
#print(names[-2:])

#names.append("LeiHaiDong")
#print(names)

#names.insert(1,"ChenRongHua")
#print(names)

#names.insert(3,"XinZhiYu ")
#print(names)