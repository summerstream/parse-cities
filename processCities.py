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
# print(json.dumps(provices['14']['cities']['05']['areas']['25'],encoding='utf-8',ensure_ascii=False).decode('UTF-8'))
#台湾 澳门 香港特殊处理
# print (json.dumps(provices['71'],encoding='utf-8',ensure_ascii=False).decode('UTF-8'))
provices['71']['cities']['00'] = {}
provices['71']['cities']['00']['name'] = '台湾'
provices['71']['cities']['00']['areas'] = {
    '00':'台湾'
}
# print (json.dumps(provices['71'],encoding='utf-8',ensure_ascii=False).decode('UTF-8'))
provices['81']['cities']['00'] = {}
provices['81']['cities']['00']['name'] = '香港特别行政区'
provices['81']['cities']['00']['areas'] = {
    '00':'香港特别行政区'
}
# print (json.dumps(provices['71'],encoding='utf-8',ensure_ascii=False).decode('UTF-8'))
provices['82']['cities']['00'] = {}
provices['82']['cities']['00']['name'] = '澳门特别行政区'
provices['82']['cities']['00']['areas'] = {
    '00':'澳门特别行政区'
}
w = open('cities.js','w')
w.write(json.dumps(provices,encoding='utf-8',ensure_ascii=False))
w.close()