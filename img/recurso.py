import json
with open('img.json') as file:
    data = json.load(file)
    y=data['cartas'][0]['recurso1']
print(y[0]['imagen']) 
