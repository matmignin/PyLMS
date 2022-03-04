import json



def json_add_batch(new_data,n=0, filename='/Volumes/SHARED/PyLMS/codes.json'):
	with open(filename,'r+') as f:
		data = json.load(f)
		data["code"][n]['batch'].append(new_data)
		f.seek(0)
		json.dump(data, f, indent=4)

def json_add_product(new_data,n=0, filename='/Volumes/SHARED/PyLMS/codes.json'):
	with open(filename,'r+') as f:
		data = json.load(f)
		data["code"].append({"product":new_data})
		f.seek(0)
		json.dump(data, f, indent=4)

json_add_product("K444")
# json_add_batch("676-6666")

















