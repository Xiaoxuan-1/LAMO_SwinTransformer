import json
import csv

def read_json_file(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        for line in file:
            data = json.loads(line.strip())
            yield data

total_count = 0
correct_count = 0

file_path = '/data/solarLLM/output/deepseek-vl-7b-chat/v11-20240507-185808/checkpoint-9375/infer_result/20240508-105114.jsonl'
data = read_json_file(file_path)
# create test.csv
filename = 'LLM_test.csv'
with open (filename, mode='w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["#objid","label"])

    for item in data:
        label = item.get("response")[-2]
        objid = item.get("query").split('/')[6][:-5]           
        # 写入csv文件
        csvwriter.writerow([objid,label])
    


print('LLM_test.csv生成完毕！')