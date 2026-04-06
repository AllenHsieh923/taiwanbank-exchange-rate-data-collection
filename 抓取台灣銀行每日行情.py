import sqlite3

import pandas as pd

conn = sqlite3.connect("台灣銀行.db")
# sql = 'Select * from 匯率 where 日期 = ""'

url = "https://rate.bot.com.tw/xrt/all/2026-04-02"

df = pd.read_html(url)[0]
df = df.iloc[:, :5]
df.columns = ["幣別", "現金買入", "現金賣出", "即期買入", "即期賣出"]
df.insert(0, "幣別名稱", df["幣別"].str.split().str[0])
df.insert(1, "幣別代號", df["幣別"].str.split().str[1].str.strip("()"))
df["日期"] = "2026-04-02"
df.drop("幣別", axis=1, inplace=True)
columns_list = [
    "日期",
    "幣別名稱",
    "幣別代號",
    "現金買入",
    "現金賣出",
    "即期買入",
    "即期賣出",
]
df = df[columns_list]
for i in df.columns[3:]:
    df[i] = pd.to_numeric(df[i], errors="coerce")

df.to_sql("匯率", conn, if_exists="append", index=False)
print(df.head())
