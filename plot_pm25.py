import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 檔案並將其轉為 DataFrame
df = pd.read_csv('pm25.csv', header=None, names=['Time', 'Value'])

# 將時間欄位轉換為 datetime 格式，方便後續處理
df['Time'] = pd.to_datetime(df['Time'])

# 確認 DataFrame 資料
print(df)

# 繪製折線圖
plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['Value'], marker='o', linestyle='-', label='PM2.5 Value')

# 添加圖表細節
plt.xlabel('Time')  # X 軸標籤
plt.ylabel('PM2.5')  # Y 軸標籤
plt.title('PM2.5 Data Over Time')  # 圖表標題
plt.grid(True)  # 顯示網格
plt.legend()  # 顯示圖例
plt.xticks(rotation=45)  # 調整 X 軸標籤角度以便顯示時間
plt.tight_layout()  # 自動調整佈局

# 顯示圖表
plt.show()





# import pandas as pd
# import matplotlib.pyplot as plt


# def click_plot_pm25_button():
#     db_pm25 = pd.read_csv("pm25.csv")

#     df = pd.DataFrame(db_pm25)
#     # 將df 轉出成csv檔案


#     df = df.head(100)
#     print(df.head(100))
#     X=df.iloc(0)
#     Y=df.iloc(1)
#     print(list(df.iloc(0)))
    # assign the first column data as X
    
    # X=list(df.iloc(0))
    # Y=list(df.iloc(1)) 
 
    # X = list(df["create_at"])
    # Y = list(df["temperature"])


    # plt.plot(X, Y, "b-o")
    # plt.plot(X, Y, "ro--", linewidth=2, markersize=6)

    # plt.bar(X, Y, color="g")
    # plt.title("Temperature over time")
    # plt.xlabel("Time")
    # plt.ylabel("Temperature")

    # plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=time))
    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

    # plt.xticks(rotation=45)  # 旋轉 X 軸標籤

    # # 儲存為 JPG 圖檔
    # plt.tight_layout()
    # plt.savefig("bar_chart.jpg", format="jpg", dpi=300)
    # plt.show()
    # # print("圖表已經成功儲存！")
    # msg = "折線圖成功繪製，檔名為bar_chart.jpg，存放於目前資料夾"
    # strVar1.set(msg)
    # print("目前折線圖成功繪製，檔名為bar_chart.jpg，存放於目前資料夾")


# click_plot_pm25_button()