# 从Excel到Python——数据分析进阶指南.pdf

# 导入pandas、numpy库

# Pandas是一个强大的分析结构化数据的工具集；它的使用基础是Numpy（提供高性能的矩阵运算）；
# 用于数据挖掘和数据分析，同时也提供数据清洗功能。
import pandas as pd
import numpy as np
# numpy是个运行速度非常快的数学库，主要用于数组计算。

'''【第1章 数据表生成】
常见的生成数据表的方法有两种，第一种是导入外部数据，第二种是直接写入数据。
Excel中的“文件”菜单中提供了获取外部数据的功能，支持数据库和文本文件和页面的多种数据源导入。
Python支持从多种类型的数据导入。在开始使用Python进行数据导入前需要先导入pandas库，
为了方便起见，我们也同时导入numpy库。
'''
# 导入数据表
# df = pd.DataFrame(pd.read_excel('1.xlsx'))
# print(df)

# 创建数据表
df = pd.DataFrame({
    "id": [1001, 1002, 1003, 1004, 1005, 1006],
    "date": pd.date_range('20130102', periods=6),
    "city": ['Beijing', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING'],
    "age": [23, 44, 54, 32, 34, 32],
    "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
    "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
    columns=['id', 'date', 'city', 'category', 'age', 'price']
)

'''【第2章 数据表检查】
Python中处理的数据量通常会比较大，我们无法一目了然地了解数据表的整体情况，
必须要通过一些方法来获得数据表的关键信息。
检查的另一个目的是了解数据的概况，例如整个表的大小、所占空间、数据格式、
是否有空值和重复项和具体的数据内容，为后面的清洗和预处理做好准备。
'''
# 查看数据表维度，结果(6, 6)六行六列
# print(df.shape)

# 查看数据表信息
# print(df.info())

# 查看数据格式
# print(df.dtypes)

# 检验空值，可以对整个数据表进行检查，
# print(df.isnull)
# 也可单独对某一列进行空值检查。
# print(df['price'].isnull)

# Unique是查看唯一值的函数，只能对数据表中的特定列进行检查。
# 返回的结果是该列中的唯一值,类似与Excel中删除重复项后的结果。
# 查看city列中的唯一值
# print(df['city'].unique())

# Values函数用来查看数据表中的数值。以数组的形式返回，不包含表头信息。
# print(df.values)

# Columns函数用来单独查看数据表中的列名称。
# print(df.columns)

# Head函数用来查看数据表中的前N行数据，默认显示前5行，
# 可以自己设置参数值来确定查看的行数。
# 查看前3行数据
# print(df.head(3))

# Tail行数与head函数相反，用来查看数据表中后N行的数据，默认显示后5行数据，
# 可以自己设置参数值来确定查看的行数。
# 查看最后3行
# print(df.tail(3))

'''【第3章 数据表清洗】
主要内容包括对空值、大小写问题、数据格式和重复值的处理。
这里不包含对数据间的逻辑验证。
'''
# 处理空值(删除或填充)
# 1、使用Dropna函数用来删除数据表中包含空值的数据
# print(df.dropna(how='any'))

# 2、使用fillna函数将特定数据对空值进行填充，
# 对空值字段填充数字0或字符串
# print(df.fillna(value=0))   # print(df.fillna(value='anyString'))
# 对特定列的空值字段填充特定数据，如平均值
# print(df['price'].fillna(df['price'].mean()))

# 字符中的空格也是数据清洗中一个常见的问题，
# 清除city字段中的字符空格
# df['city'] = df['city'].map(str.strip)
# print(df.values)

# 英文字段中，字母大小写不统一也是一个常见的问题。
# 大小写转换
# df['city'] = df['city'].str.upper()
# df['city'] = df['city'].str.lower()
# print(df.values)

# dtype是查看数据格式的函数,
# 与之对应的astype函数用来修改数据格式
# print(df['price'].astype('Int64'))  # 类型float64转为Int64

# Rename是更改列名称的函数
# print(df.rename(columns={'category': 'category-size'}))

# drop_duplicates函数可删除重复值，区分大小写，
# 默认情况将删除后出现的重复值(与Excel逻辑一致)，
# 增加keep='last'参数后将删除最先出现的重复值（删前保后）。
# print(df['city'].str.lower().drop_duplicates(keep='last'))

# 数值修改及替换，replace函数实现数据替换
# print(df['city'].replace('SH', 'shanghai'))


'''【第4章 数据预处理】
对清洗完的数据进行整理以便后期的统计和分析工作,
主要包括数据表的合并，排序，数值分列，数据分组及标记等工作。
'''
# 建立df1数据表，用于和df数据表进行合并。
df1 = pd.DataFrame({
    "id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "gender": ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
    "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y', ],
    "m-point": [10, 12, 20, 40, 40, 40, 30, 20]
})

# 使用merge函数对两表进行合并，方式为inner（left,right,outer),
# 将两个数据表中共有的数据匹配到一起生成新的数据表，并命名为df_inner。
# 数据表匹配合并
df_inner = pd.merge(df, df1, how='inner')
# print(df_inner)
#
# df_left = pd.merge(df, df1, how='left')
# df_right = pd.merge(df,df1,how='right')
# df_outer = pd.merge(df,df1,how='outer')
# print('-'*75,df_left,sep='\n')
# print('-'*75,df_right,sep='\n')
# print('-'*75,df_outer,sep='\n')

# 完成表合并后对df_inner数据表设置索引列，
# 索引列可以进行数据提取，汇总，数据筛选等。
# 设置索引列
# print(df_inner.set_index('id'))

# 可以使用sort_values函数（按数值）,
# sort_index函数（按索引）完成排序。
# print(df_inner.sort_values(by=['age']))
# print(df_inner.sort_index())

# Where函数用来对数据进行判断和分组，对某列的值进行判断，
# 符合条件的分一组，不符合的分另一组，并使用group字段（新增）进行标记。
# 若price列的值>3000，group列显示high，否则显示low。
# df_inner['group'] = np.where(df_inner['price'] > 3000, 'high', 'low')
# print(df_inner)

# 除where函数外，还可对多个字段的值判断再分组，
# 将city列=beijing且price列>=4000的数据标记为1。
# 对复合多个条件的数据进行分组标记
# df_inner.loc[(df_inner['pay'] == 'Y') & (df_inner['price'] >= 4000), 'sign'] = 1
# print(df_inner)

# 与数据分组相反的是对数据进行分列，同字段一列可分多列，使用split函数实现。
# 对category字段值依次分列，并创建表，索引值为df_inner索引列，列名称为category和size。
df2 = pd.DataFrame(data=(x.split('-') for x in df_inner['category']),
                   index=df_inner.index, columns=['category', 'size'])
# print(df2)

# 将完成分列后的数据表与原df_inner数据表进行匹配
df_inner = pd.merge(df_inner, df2, left_index=True, right_index=True)
# print(df_inner)

'''【第5章 数据提取】
数据分析中最常见的一个工作，主要使用3个函数：loc、iloc、ix。
loc函数按标签值进行提取，iloc函数按位置进行提取，ix函数可以同时按标签和位置进行提取.
'''
# loc函数按表的索引标签进行提取，
# 提取了索引列为3的单条（单行）数据。
# print(df_inner.loc[3])

# 使用冒号可以限定提取数据的范围，
# ":"前面为开始的标签值，后面为结束的标签值。
# print(df_inner.loc[3:])   # 提取标签值3到最后的所有数据

# Reset_index函数用于恢复索引（重置索性），
# df_inner.reset_index()
# 重设索引,将date字段的日期设置为数据表的索引
df_inner = df_inner.set_index('date')
# print(df_inner)

# 用冒号限定提取索引值数据的范围，
# 提取所有2013年1月4日以后的数据。
# print(df_inner['2013-01-05':])

# 使用iloc按位置区域提取数据
# 冒号前后数字不再是索引标签名称，而是数据所在位置，从0开始。
# print(df_inner.iloc[:3, :2])    # 前0~2行，后0~1列

# 使用iloc函数还可根据位置逐条单独提取数据，
# 方括号中的数值对应所在行、列的位置（前行后列）。
# print(df_inner.iloc[[0, 2, 5], [2, 5]]) # 第0、2、5行的2、5列

# 按标签和位置提取（ix）
# ix是loc和iloc的混合，既能按索引标签提取，也能按位置进行数据提取。
# print(df_inner.ix['2013-01-04 ':, 0:4]) # （前后）行按标签，列按位置
'''警告：官方不推荐使用IX索引器，在0.20.0开始，ix索引器已被弃用，赞成更加严格.iloc 和.loc索引。
.ix可以根据索引的数据类型决定按位置或通过标签进行索引。多年来，这引起了相当多的用户混淆。
'''

# 除了按标签和位置提起数据外，还可按具体的条件。
# 用isin函数对city中的值是否为beijing进行判断。
# print(df_inner['city'].isin(['shanghai']))  # 判断返回布尔值
# isin和loc两个函数配合使用，按指定条件对数据进行提取。
# print(df_inner.loc[df_inner['city'].str.lower().isin(['beijing', 'shanghai'])])
# print(df_inner)

# 数值提取还可完成类似数据分列的工作，从字段数据中提取出制定的数值。
# print(pd.DataFrame(df_inner['category_x'].str[:3]))
# 提取category_x字段数据的前三个字符，并生成数据表

'''【第6章 数据筛选】
使用与，或，非三个条件配合大于，小于和等于对数据进行筛选，并进行计数和求和。
与Excel中的筛选功能和countifs和sumifs功能相似。
'''
# 使用（与&、或|、非!）三个条件配合大于，小于和等于对数据进行筛选，并进行计数和求和。
# 按条件筛选（与、或、非）,Python中使用loc函数配合筛选条件来完成筛选功能。
# 配合sum和count函数还能实现Excel中sumif和countif函数的功能。
# print(df_inner.loc[(df_inner['city'] == 'shanghai') & (df_inner['age'] > 25),['id','size']])
# 筛选后只显示id、size两列

# print(df_inner.loc[(df_inner['city'] == 'Beijing') | (df_inner['age'] > 35)].age.sum())
# print(df_inner.loc[(df_inner['city'] == 'Beijing') | (df_inner['age'] > 35)].age.count())
# 对筛选后的数据按age字段进行求和、计数

# 使用“非”条件进行筛选
# print(df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']]
#       .sort_values(['age']))
# print(df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']]
#       .sort_index())
# 注意：DataFrames对象已弃用支持sort属性，改为sort_values或者sort_index分别描述。


# 还有一种筛选的方式是用query函数
# 使用query函数进行筛选
# print(df_inner.query('city == ["Beijing", "shanghai"]').age.sum())


'''【第7章 数据汇总】
Excel中使用分类汇总和数据透视可以按特定维度对数据进行汇总，
对应的，Python中使用的主要函数是groupby和pivot_table。
'''
# 一、分类汇总
# Groupby是进行分类汇总的函数，支持多级分类汇总。
# 制定要分组的列名称就可以，也可同时制定多个列名称，按列名称出现的顺序进行分组。
# 同时要制定分组后的汇总方式，常见的是计数和求和两种。
# print(df_inner.groupby('city').count()) #对所有列进行计数
# print(df_inner.groupby('city')['price'].sum()) #对特定的price列进行汇总
# print(df_inner.groupby(['city', 'size'])['age'].sum()) #对两个字段进行汇总求和

# print(df_inner.groupby('city')['price'].agg([len, np.sum, np.mean]))
# 对city字段进行汇总并计算price的数量、合计和均值。

# 二、数据透视
# 数据透视表也是常用的一种数据分类汇总方式，并且功能上比groupby要强大一些。
# Python中通过pivot_table函数也能实现数据透视表同样的功能效果。
# print(
#     pd.pivot_table(
#         df_inner,
#         index=['city'],
#         columns=['size'],
#         values=['price'],
#         aggfunc=[
#             len,
#             np.sum],
#         fill_value=0,
#         margins=True))
# 设定city为行字段，size为列字段，price为值字段，分别计算price的数量和金额并且按行与列进行汇总求和。


'''【第8章 数据统计】
本章主要介绍数据采样，标准差，协方差和相关系数的使用方法。
'''
# 数据采样
# Sample是进行数据采样函数，设置n的数量自动返回参与的结果。
# print(df_inner.sample(n=3))

# Weights参数是采样的权重，通过设置不同的权重可以更改采样的结果，权重高的数据将更有希望被选中。
# 这里手动设置6条数据的权重值，将前面4个设置为0，后面两个分别设置为0.5。
# weights = [0, 0, 0, 0, 0.5, 0.5]
# print(df_inner.sample(n=2, weights=weights))

# Sample函数中还有一个参数replace，用来设置采样后是否放回。
# df_inner.sample(n=6, replace=False) # 采样后不放回
# print(df_inner.sample(n=6, replace=True))   # 采样后放回

#描述统计
# Describe函数是进行描述统计的函数，自动生成数据的数量，均值，标准差等数据。
# round函数设置结果显示的小数位，并对结果数据进行转置。
# 数据表描述性统计
# print(df_inner.describe().round(2).T)

# 标准差
# Std函数用来接算特定数据列的标准差。
# print(df_inner['price'].std())

# 协方差
# Cov函数用来计算两个或各字段间的协方差，
# 可以只对特定字段进行计算，也可对整个数据表中各列之间进行计算。
# 两字段间的协方差
# df_inner['price'].cov(df_inner['m-point'])  # 17263.200000000001
#数据表中所有字段间的协方差
# print(df_inner.cov())

# 相关分析
# Corr函数用来计算数据间的相关系数。
# 可单独对特定数据进行计算，也可以对整个数据表中各个列进行计算。
# 相关系数在-1到1之间，接近1为正相关，接近-1为负相关，0为不相关。
# df_inner['price'].corr(df_inner['m-point']) # 0.77466555617085264
# 数据表相关性分析
# print(df_inner.corr())


'''【第9章 数据输出】
处理和分析完的数据可以输出为xlsx格式和csv格式。
'''
# workbook是xlsxwriter库中最基本的操作类，用于编写Excel XLSX工作簿文件。
from xlsxwriter import workbook

# 创建名为Ex_1的xlsx文件，表名为sheet_1
# df_inner.to_excel('Ex_1.xlsx',sheet_name='sheet_1') # 写入Excel

# 创建名为Ex_1的CSV文件
# df_inner.to_csv('Ex_1.csv')   # 写入csv
