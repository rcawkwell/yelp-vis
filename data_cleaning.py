import os 
import json

#load in  photo.json to data_photo and business.json to data_business
data_photo = []
with open('photo.json') as f:
    for line in f:
        data_photo.append(json.loads(line))
data_business = []
with open('business.json') as f:
    for line in f:
        data_business.append(json.loads(line))




def getData(filename):
    for j in data_business:
        if i['business_id'] == j['business_id']:
            return j
                    
                    
for i in data_photo:
    getData(i["photo_id"])
    
#directory = os.fsencode("./yelp_photos/photos")

#for file in os.listdir(directory):
    #filename = os.fsdecode(file)
    #file_id, trash = filename.split(".")
    
    #getData(file_id)
