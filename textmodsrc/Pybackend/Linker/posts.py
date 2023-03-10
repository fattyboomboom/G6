import json
import os

from collections import Counter

def write_json(new_data, filename='post.json'):
    idCount = 0

    # check if file exists and if the file isnt empty. if true, we read the filename
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename,'r+') as file:
            # load existing data from current file if it exists and isnt empty
            file_data = json.load(file)
    else:
        #to avoid an error and create new posts, we create an empty list of dictionaries
        file_data = []

    # using generator expression to find the occurences of 'id' in loaded file
    # then uses sum to find the count of each 'id'
    idKeys = (1 for k in file_data if k.get('id'))
    idCount = sum(idKeys)

    # we append a new key of 'id' and assign it equal to current idCount + 1
    # then we add the new data to the list of dictionaries
    new_data['id'] = idCount + 1
    file_data.append(new_data)

    # sets file's current position at offset.
    with open(filename,'w') as file:
        # convert back to json.
        json.dump(file_data, file, indent = 4)