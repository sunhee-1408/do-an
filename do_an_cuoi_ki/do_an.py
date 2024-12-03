import pandas as pd # được sử dụng để xử lý và phân tích dữ liệu
import numpy as np # hữu ích cho các phép tính số học và xử lý mảng.
import matplotlib # dùng để tạo các biểu đồ và hình ảnh minh họa
matplotlib.use('Agg') # tạo hình ảnh mà không cần giao diện đồ họa
import matplotlib.pyplot as plt #tạo các biểu đồ và hình ảnh trực quan.
import seaborn as sns #giúp tạo các biểu đồ thống kê đẹp mắt và dễ sử dụng.
import warnings
warnings.filterwarnings('ignore') #Bỏ qua các cảnh báo để đầu ra gọn gàng hơn

file_path = r'c:\Users\giabao\Downloads\all_youtube_analytics.csv'
df =pd.read_csv(file_path)
print(df.head())
