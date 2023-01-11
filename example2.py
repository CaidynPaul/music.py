import music
import json

new_config_file = open('fake.json','r')
new_config_data = json.load(new_config_file)

music.play(0,'<Insert Song Here>',1000,new_config_data)
music.wait()
