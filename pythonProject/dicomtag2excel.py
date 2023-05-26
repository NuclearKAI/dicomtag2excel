import os
import pandas as pd
import pydicom

# 定义需要提取的标签列表
tags = ['PatientName', 'PatientID', 'PatientBirthDate', 'PatientSex',
        'SOPClassUID', 'SOPInstanceUID', 'GroupLength', 'Manufacturer',
        'ReferringPhysicianName', 'StudyID', 'PatientOrientation', 'SeriesNumber',
        'StudyDate', 'SeriesDate', 'PatientAge', 'PatientSize', 'PatientWeight']

# 定义需要处理的DICOM文件夹路径和输出Excel文件路径
dicom_folder_path = '/Users/kai/NCAC相关/ncac/202303/11QGS000'
output_excel_path = '/Users/kai/NCAC相关/ncac/202303/patient_info.xlsx'

# 遍历DICOM文件夹中的所有文件，提取标签信息并保存到DataFrame中
df_list = []
for root, dirs, files in os.walk(dicom_folder_path):
    for filename in files:
        filepath = os.path.join(root, filename)
        try:
            dcm = pydicom.dcmread(filepath)
            info = {}
            for tag in tags:
                if hasattr(dcm, tag):
                    info[tag] = str(getattr(dcm, tag)).strip()
                else:
                    info[tag] = ''
            df_list.append(pd.DataFrame([info]))
        except:
            pass

# 将所有数据框合并为一个大数据框
df_merged = pd.concat(df_list)

# 将提取的标签信息保存到Excel中
df_merged.to_excel(output_excel_path, index=False)

