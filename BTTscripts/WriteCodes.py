import json



def json_add_batch(new_batch,n=0, filename='/Users/matbook/PyLMS/codes.json'):
	with open(filename,'r+') as f:
		data = json.load(f)
		data['products'][n]['batches'].append({'batch':new_batch})
		f.seek(0)
		json.dump(data, f, indent=4)



def json_add_product(new_product,filename='/Users/matbook/PyLMS/codes.json'):
	with open(filename,'r+') as f:
		data = json.load(f)
		data['products'].append({'product':new_product})
		f.seek(0)
		json.dump(data, f, indent=4)

def json_add_lot(new_lot,x=0,y=0, filename='/Users/matbook/PyLMS/codes.json'):
	with open(filename,'r+') as f:
		data = json.load(f)
		data['products'][x]['batches'][y]['lot'].append(new_lot)
		f.seek(0)
		json.dump(data, f, indent=4)


def json_add_code(new_product='',new_batch='',new_lot='',n=0,m=0, filename='/Users/matbook/PyLMS/codes.json'):
	with open(filename,'r+') as f:
		data = json.load(f)
		if new_product:
			data['products'][n]['batches'].append({'batch':new_batch})
		if new_batch:
			data['products'].append({'product':new_product})
		if new_lot:
			data['products'][n]['batches'][m]['lot'].append(new_lot)
		f.seek(0)
		json.dump(data, f, indent=4)

# json_add_code('K999','222-9999','9090K2')
# json_add_prodct('K555')
# json_add_batch('676-6666')
# json_add_lot('6666B2')



























