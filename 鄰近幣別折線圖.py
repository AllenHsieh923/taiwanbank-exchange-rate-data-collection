import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

conn = sqlite3.connect("台灣銀行.db")
sql = "Select * from 匯率 order by 日期"
df = pd.read_sql(sql, conn)
print(df["幣別名稱"].unique())
sophia = input("請輸入幣別 : ")
df1 = df[df["幣別名稱"] == sophia]

s = df.groupby("幣別名稱")["現金買入"].mean().sort_values()
s1 = s[s.between(s[sophia] * 0.8, s[sophia] * 1.2)]

plt.figure(figsize=(16, 10), dpi=150)
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"

for i in s1.index:
    df1 = df[df["幣別名稱"] == i]
    plt.plot(df1["日期"], df1["現金買入"], label=i)
plt.legend()
plt.xlabel("日期", fontsize=16)
plt.ylabel("現金買入", fontsize=16)
plt.title(f"{sophia} 和鄰近幣別折線圖", fontsize=24)
plt.xticks(np.linspace(0, len(df1) - 1, 12))


print(s)
plt.show()
