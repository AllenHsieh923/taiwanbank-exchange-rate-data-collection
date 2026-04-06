import random
import sqlite3
from datetime import datetime
from time import sleep

import pandas as pd

allday = pd.date_range("20250101", datetime.now())

conn = sqlite3.connect("台灣銀行.db")

for d in allday:
    d = str(d)[:10]
    sql = f"Select * from 匯率 where 日期 = '{d}'"

    try:
        df = pd.read_sql(sql, conn)

    except:
        df = pd.DataFrame()
    if len(df) > 0:
        print(f"{d} 當日已有資料")
    else:
        url = f"https://rate.bot.com.tw/xrt/all/{d}"

        df = pd.read_html(url)[0]

        sleep(random.randint(3, 15))
        if len(df) > 2:

            df = df.iloc[:, :5]
            df.columns = ["幣別", "現金買入", "現金賣出", "即期買入", "即期賣出"]
            df.insert(0, "幣別名稱", df["幣別"].str.split().str[0])
            df.insert(1, "幣別代號", df["幣別"].str.split().str[1].str.strip("()"))
            df["日期"] = d
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
            print(len(df))
            print(f"{d} 已儲存至資料庫")
        else:
            print(f"{d} 當日沒有營業")
