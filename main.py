import json 


ask = input('Whats your name? ')

with open('data.json', 'w') as f:
    json.dump(ask, f)
    
    
    
    
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)