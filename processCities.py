#coding=utf-8
import json
provices = {}
with open('cities','r+') as f:
    for line in f:
        number = line.split(' ')[0]
        province = number[0:2]
        city = number[2:4]
        area = number[4:6]
        name = line.split(' ')[len(line.split(' '))-1].strip().replace('　','')
        if city == '00':
            provices[province]={};
            provices[province]['name'] = name
            provices[province]['cities'] = {}
        elif area == '00':
            provices[province]['cities'][city]={}
            provices[province]['cities'][city]['name']=name
            provices[province]['cities'][city]['areas'] = {}
        else:
            provices[province]['cities'][city]['areas'][area]=name
f.close()
# print(json.dumps(provices,encoding='utf-8',ensure_ascii=False).decode('UTF-8'))
print(json.dumps(provices['14']['cities']['05']['areas']['25'],encoding='utf-8',ensure_ascii=False).decode('UTF-8'))

w = open('cities.js','w')
w.write(json.dumps(provices,encoding='utf-8',ensure_ascii=False))
w.close()