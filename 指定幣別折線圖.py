import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

conn = sqlite3.connect("台灣銀行.db")

sql = "Select * from 匯率"

df = pd.read_sql(sql, conn)
print(df["幣別名稱"].unique())
jessica = input("請輸入幣別名稱 : ")
plt.figure(figsize=(16, 10), dpi=150)
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"
df1 = df[df["幣別名稱"] == jessica].sort_values("日期")
plt.plot(df1["日期"], df1["現金買入"], label=df1["幣別名稱"].iloc[0])
plt.xlabel("日期", fontsize=16)
plt.ylabel("現金買入", fontsize=16)
plt.title(f"{df1['幣別名稱'].iloc[0]} 匯率走勢圖", fontsize=24)
plt.xticks(np.linspace(0, len(df1["日期"]) - 1, 12))
plt.legend()
plt.tight_layout()
plt.savefig("指定幣別折線圖.png")

plt.show()
