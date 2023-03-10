"""
 _*_ coding: utf-8 _*_

 Copyright (C) 2023 - 2023 Tony Huang All Rights Reserved 

 @Time    : 2023/3/10 20:42
 @Author  : Tony Huang
 @File    : gen_data.py
 @IDE     : PyCharm
 @Contact : hhh_htz@outlook.com
 """
import faker
import pandas as pd
import os

# ================ 配置 ================
# 生成数据的数量
data_num = 100
# 生成旷课 作弊 缺考的概率
# 公式： 生成率 = {1 / {nums}
# nums：数据总量
nums = 80
# =====================================
"""
1. 列数据：[学号 班级 姓名 性别 英语 体育 军训 数分 高代 解几]
2. 生成1000条数据
3. 学号：2308024 + 3位随机数
4. 班级：230802 + 2位随机数
5. 姓名：faker生成
6. 性别：随机生成
7. 英语：40-100随机生成
8. 体育：40-100随机生成
9. 军训：40-100随机生成
10. 数分：40-100随机生成
11. 高代：40-100随机生成
12. 解几：40-100随机生成
"""
# 删除已有的文件
if os.path.exists('stu_score.csv'):
    os.remove('stu_score.csv')
if os.path.exists('stu_score.xlsx'):
    os.remove('stu_score.xlsx')
# 生成随机数据
f = faker.Faker(locale='zh_CN')
# 生成表头
columns = ['学号', '班级', '姓名', '性别', '英语', '体育', '军训', '数分', '高代', '解几']
# 生成学号
stu_id = []
for i in range(data_num):
    stu_id.append('2308024' + str(f.random_int(min=1, max=999, step=1)).zfill(3))
# 生成班级
stu_class = []
for i in range(data_num):
    stu_class.append('230802' + str(f.random_int(min=1, max=99, step=1)).zfill(2))
# 生成姓名
stu_name = []
for i in range(data_num):
    stu_name.append(f.name())
# 生成性别
stu_sex = ['男' if f.random_int(min=0, max=1, step=1) == 1 else '女' for i in range(data_num)]
# 生成六科成绩
stu_score = []
for i in range(data_num):
    stu_score.append([f.random_int(min=40, max=100, step=1) for i in range(6)])
# 生成DataFrame
df = pd.DataFrame(columns=columns)
df['学号'] = stu_id
df['班级'] = stu_class
df['姓名'] = stu_name
df['性别'] = stu_sex
df['英语'] = [i[0] for i in stu_score]
df['体育'] = [i[1] for i in stu_score]
df['军训'] = [i[2] for i in stu_score]
df['数分'] = [i[3] for i in stu_score]
df['高代'] = [i[4] for i in stu_score]
df['解几'] = [i[5] for i in stu_score]
# 保存为csv
df.to_csv('stu_score.csv', index=False)
# 读取excel
df = pd.read_csv('stu_score.csv')
print(df)
# 随机替换军训和体育列的数据为[缺考 作弊 旷课]
df['体育'] = df['体育'].apply(
    lambda x: f.random_element(elements=('缺考', '作弊', '旷课')) if f.random_int(min=1, max=nums, step=1) == 2 else x)
df['军训'] = df['军训'].apply(
    lambda x: f.random_element(elements=('缺考', '作弊', '旷课')) if f.random_int(min=1, max=nums, step=1) == 2 else x)
df['解几'] = df['解几'].apply(
    lambda x: f.random_element(elements=('缺考', '作弊', '旷课')) if f.random_int(min=1, max=nums, step=1) == 2 else x)
df['高代'] = df['高代'].apply(
    lambda x: f.random_element(elements=('缺考', '作弊', '旷课')) if f.random_int(min=1, max=nums, step=1) == 2 else x)
df['英语'] = df['英语'].apply(
    lambda x: f.random_element(elements=('缺考', '作弊', '旷课')) if f.random_int(min=1, max=nums, step=1) == 2 else x)
# 保存为xlsx
df.to_excel('stu_score.xlsx', index=False)
