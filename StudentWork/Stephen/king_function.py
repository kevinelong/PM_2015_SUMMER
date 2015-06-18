#this is my attempt working with a function
data_list_=[
	{"id": 246, "name": "king", "PHONE": "333"},
	{"id": 369, "name": "miller"},
	{"id": 459, "name": "dan"}
	]

# DEFINFE FUNCTION
def transform(data_list_input):
	data_dictionary_output = {}

	#DOING WORK HERE.
	#LOOP THROUGH ITEMS IN DATA_LIST
	for item in data_list_input:

				#EXTRACT ID FROM each extracted item
		id = item["id"]
		
				# creat an output item that is a new Dictionary/Object
		output_item = {}
		
		# copy all properties except id from the item
		# name = item["name"]
		# output_item["name"] = name

		# Previous to lines same as this.
		# output_item["name"] = item["name"]
		for key in item.keys():
			if key != "id":
				output_item[key] = item[key]

		# add the new item to the data_dictionary using the id as the key.
		data_dictionary_output[id] = output_item
			# this is the same a the line above without the local
			# 

		# data_dictionary_output[item["id"]] = itme ["name"]
	return (data_dictionary_output)
print (data_dictionary_results)
transform(data_list)