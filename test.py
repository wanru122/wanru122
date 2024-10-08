import csv
import json

# 讀取 CSV 檔案
csv_file_path = 'aqx_p_432.csv'
json_file_path = 'aqx_p_432.json'

data = []

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        data.append(row)

# 將資料寫入 JSON 檔案
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print(f"已成功將 {csv_file_path} 轉換為 {json_file_path}")