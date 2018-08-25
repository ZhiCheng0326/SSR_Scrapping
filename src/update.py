# -*- coding: utf-8 -*-
import json

def updateConfig(newConfig):
    #Load file
    with open('gui-config.json') as json_data_file:
        data = json.load(json_data_file)
    
    #Begin update for the configuration        
    for keys, values in newConfig.items():
        for config in data['configs']:    
            config[keys] = values
            
    #Write file
    with open('gui-config.json', 'w') as outfile:  
        json.dump(data, outfile, indent = 2)
