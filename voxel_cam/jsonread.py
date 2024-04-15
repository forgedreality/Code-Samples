#read camara.json
import json

def normalize(val):
    return (val % 360 + 360) % 360

with open('config.json') as json_file:
    data = json.load(json_file)

for i in range(len(data["keyframe"])):
    #if smaller than 0 normalsise
    if data["keyframe"][i]["param"]["cam ry"] < 0:
        p = normalize(data["keyframe"][i]["param"]["cam ry"])
    else:
        p = data["keyframe"][i]["param"]["cam ry"] 
    p = str(p)
    print(p)