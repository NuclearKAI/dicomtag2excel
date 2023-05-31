import os
import tkinter as tk
from tkinter import filedialog

def extract_files():
    # 获取用户输入的源文件夹路径和目标文件夹路径
    source_folder_path = source_folder_entry.get()
    target_folder_path = target_folder_entry.get()

    # 获取用户输入的相同字段文件名
    keyword = keyword_entry.get()

    # 检查输入的源文件夹路径和目标文件夹路径是否存在
    if not os.path.isdir(source_folder_path):
        result_label.config(text="Invalid source folder path")
        return
    if not os.path.isdir(target_folder_path):
        result_label.config(text="Invalid target folder path")
        return

    # 遍历源文件夹内的所有文件
    for filename in os.listdir(source_folder_path):
        if keyword in filename:
            source_path = os.path.join(source_folder_path, filename)
            target_path = os.path.join(target_folder_path, filename)

            # 检查目标文件是否已经存在
            if os.path.exists(target_path):
                result_label.config(text="File already exists: " + filename)
                continue

            with open(source_path, 'rb') as source_file:
                with open(target_path, 'wb') as target_file:
                    target_file.write(source_file.read())

    result_label.config(text="Completed!")


# 创建GUI界面
root = tk.Tk()
root.title("File Extractor")

# 创建源文件夹路径输入框和按钮
source_folder_label = tk.Label(root, text="Source Folder:")
source_folder_label.grid(row=0, column=0)

source_folder_entry = tk.Entry(root, width=50)
source_folder_entry.grid(row=0, column=1)

source_folder_button = tk.Button(root, text="Browse", command=lambda: source_folder_entry.insert(0, filedialog.askdirectory()))
source_folder_button.grid(row=0, column=2)

# 创建目标文件夹路径输入框和按钮
target_folder_label = tk.Label(root, text="Target Folder:")
target_folder_label.grid(row=1, column=0)

target_folder_entry = tk.Entry(root, width=50)
target_folder_entry.grid(row=1, column=1)

target_folder_button = tk.Button(root, text="Browse", command=lambda: target_folder_entry.insert(0, filedialog.askdirectory()))
target_folder_button.grid(row=1, column=2)

# 创建相同字段文件名输入框
keyword_label = tk.Label(root, text="Keyword:")
keyword_label.grid(row=2, column=0)

keyword_entry = tk.Entry(root, width=50)
keyword_entry.grid(row=2, column=1)

# 创建提取按钮
extract_button = tk.Button(root, text="Extract Files", command=extract_files)
extract_button.grid(row=3, column=1)

# 创建结果标签
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=1)

root.mainloop()
