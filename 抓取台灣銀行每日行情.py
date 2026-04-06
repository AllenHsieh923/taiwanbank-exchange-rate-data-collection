import pandas as pd

url = "https://rate.bot.com.tw/xrt/all/2026-04-02"

df = pd.read_html(url)[0]
print(df.head())
