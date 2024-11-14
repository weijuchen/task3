import tkinter as tk
from tkinter import ttk

# import my file pull_v5.py
# from pull_v6 import pull_file_from_device


# import pymysql
import os
import sqlite3
import csv
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timezone, timedelta
import tkinter.font as tkFont
import matplotlib.dates as mdates

# Get today's date
today_date = datetime.now().strftime("%Y%m%d")

# Get downloads folder
user_downloads_folder = os.path.expanduser("~/Downloads")

# D:\D_Download\zap_database

conn = sqlite3.connect("zap_database")
# conn = sqlite3.connect("D:\D_Download\zap_database")
cursor = conn.cursor()


def query_info():

    query = "SELECT pm25,temperature,humidity,create_at FROM airqualitydata"
    cursor.execute(query)
    data = cursor.fetchall()
    # print(data)

    with open("mj.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([header[0] for header in cursor.description])
        writer.writerows(data)
    print("匯出成功！")


interval = "5T"
time = 1


def click_button1_2():
    query_info()
    msg = "SQL轉換為CSV檔案成功，檔名為mj.csv，存放於目前資料夾"
    strVar1.set(msg)
    print("使用者SQL轉換為CSV檔案成功，檔名為mj.csv，存放於目前資料夾")


def click_plot_button(interval, time):
    db_data = pd.read_csv("mj.csv")

    df = pd.DataFrame(db_data)
    # 將df 轉出成csv檔案

    df["create_at"] = pd.to_datetime(df["create_at"], unit="ms")
    # df.to_csv("mj_ms.csv", index=False)

    df = df.head(100)
    # df.to_csv("mj_head.csv", index=False)
    # df.set_index("create_at", inplace=True)

    # df_resampled = df.resample(interval).mean().reset_index()

    X = list(df["create_at"])
    Y = list(df["temperature"])

    # X = list(df_resampled["create_at"])
    # Y = list(df_resampled["temperature"])
    # plt.plot(X, Y, "r")
    plt.plot(X, Y, "b-o")
    # plt.plot(X, Y, "ro--", linewidth=2, markersize=6)

    # plt.bar(X, Y, color="g")
    plt.title("Temperature over time")
    plt.xlabel("Time")
    plt.ylabel("Temperature")

    plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=time))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

    plt.xticks(rotation=45)  # 旋轉 X 軸標籤

    # 儲存為 JPG 圖檔
    plt.tight_layout()
    plt.savefig("bar_chart.jpg", format="jpg", dpi=300)
    plt.show()
    # print("圖表已經成功儲存！")
    msg = "折線圖成功繪製，檔名為bar_chart.jpg，存放於目前資料夾"
    strVar1.set(msg)
    print("目前折線圖成功繪製，檔名為bar_chart.jpg，存放於目前資料夾")


root = tk.Tk()
root.title("GUI Ver1 @v0.02 2024-11-13")
root.geometry("800x400")


notebook = ttk.Notebook(root)


tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="page 1")

strVar1 = tk.StringVar()
fontStyle = tkFont.Font(family="Helvetica", size=11, weight="normal", slant="roman")

button1_1 = tk.Button(
    tab1,
    text="Download ZAP Database",
    font=("Arial", 16),
    # command=lambda: pull_file_from_device(
    #     "/data/data/com.avalue.factory_test2/databases",
    #     os.path.join(user_downloads_folder, f"newname_{today_date}"),
    # ),
    # command=query_info,
    command=lambda: print("Page 1 按鈕 1 被點擊"),
)
# button1_1.pack(side='left',pady=5,padx=10)
button1_1.grid(column=0, row=0, padx=5, pady=10)

button1_2 = tk.Button(
    tab1,
    text="Convert data to CSV",
    font=("Arial", 16),
    command=click_button1_2,
    # command=query_info,
    # command=lambda: plot_bar_chart("5T", 5),
    # command=lambda: print("Page 1 按鈕 2 被點擊"),
)
button1_2.grid(column=1, row=0, padx=5, pady=10)
# button1_2.pack(side="left", pady=5, padx=10)
button1_3 = tk.Button(
    tab1,
    text="Plot Line Chart",
    font=("Arial", 16),
    command=lambda: click_plot_button("5T", 1),
    # command=click_button1_3,
    # command=lambda: plot_bar_chart("5T", 5),
)
button1_3.grid(column=2, row=0, padx=5, pady=10)
# button1_3.pack(side="left", pady=5, padx=10)
button1_4 = tk.Button(
    tab1,
    text="Step 4",
    font=("Arial", 16),
    command=lambda: print("Page 1 按鈕 4 被點擊"),
)
button1_4.grid(column=0, row=1, padx=5, pady=10)
# button1_4.pack(side="left", pady=5, padx=10)

button1_5 = tk.Button(
    tab1,
    text="Step 5",
    font=("Arial", 16),
    command=lambda: print("Page 1 按鈕 5 被點擊"),
)
button1_5.grid(column=1, row=1, padx=5, pady=10)
# button1_5.pack(side="left", pady=5, padx=10)


button1_6 = tk.Button(
    tab1,
    text="15 minutes",
    font=("Arial", 16),
    command=lambda: click_plot_button("15T", 1),
    # command=plot_bar_chart(15),
    # command=lambda: print("間隔時間15分鐘"),
)
button1_6.grid(column=0, row=10, padx=10, pady=60)

button1_7 = tk.Button(
    tab1,
    text="30 minutes",
    font=("Arial", 16),
    command=lambda: click_plot_button("30T", 1),
    # command=lambda: print("間隔時間30分鐘"),
)
button1_7.grid(column=1, row=10, padx=10, pady=60)

button1_8 = tk.Button(
    tab1,
    text="60 minutes",
    font=("Arial", 16),
    command=lambda: click_plot_button("60T", 1),
    # command=lambda: print("間隔時間60分鐘"),
)
button1_8.grid(column=2, row=10, padx=10, pady=60)

# frame1 = tk.LabelFrame(root, text='Print messages', width=450, height=50)
label1 = tk.Label(
    master=tab1,
    bg="light grey",
    width=60,
    height=2,
    textvariable=strVar1,
    font=fontStyle,
)
label1.grid(row=30, column=1, padx=10, pady=40)


tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="page2")


button2_1 = tk.Button(
    tab2,
    text="按鈕 2",
    font=("Arial", 16),
    command=lambda: print("Page 2 按鈕 2 被點擊"),
)
button2_1.pack(pady=20)


notebook.pack(expand=True, fill="both")


root.mainloop()
