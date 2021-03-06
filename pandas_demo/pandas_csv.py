import pandas as pd

"""
python3
读csv
增加一列自增列 
输出行数列数
写csv
"""
if __name__ == '__main__':
    # person.csv包括id,name,age三个列
    sourceFile = '/Volumes/Samsung_T5/huzekang/数据集/Data Analysis/链家jupty数据分析/community.csv'
    # 读取csv,设置low_memory=False防止内存不够时报警告
    df = pd.read_csv(sourceFile, low_memory=False)

    # id列改名成longid
    df['longid'] = df['id']
    # id列变成自增列
    df['id'] = range(len(df))
    # 输出行数和列数
    print("行数：%s ,列数：%s" % (df.shape[0], df.shape[1]))

    # 以下保存指定的列到新的csv文件，index=0表示不为每一行自动编号，header=1表示行首有字段名称
    df.to_csv('/Volumes/Samsung_T5/huzekang/数据集/Data Analysis/链家jupty数据分析/new_community.csv', columns=[
              'id', 'longid', 'title', 'link', 'district', 'bizcircle', 'validdate'], index=0, header=1)
