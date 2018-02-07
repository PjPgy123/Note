# -*- coding: utf-8 -*-
"""------------------------------------------------
   File Name：     dict
   Description :
   Author :        PjPgy
   date：          2018/2/3 0003
-------------------------------------------------"""

info = {
  'stu1101':"TengLan Wu",
  'stu1102':"Longze Luola",
  'stu1103':"Xiaoze Maliya",
}

#print(info['stu1101'])
info["stu1101"] = "武藤兰"
info["stu1104"] = "Cang JingKong"


del info["stu1101"]
info.pop("stu1102")
info.popitem()
print(info)