my_list = [2, 4, 5, 6, 2, 3, 4, 6, 6, 8, 1, 2, 100, 12]

def remove_dups(list_o_stuff):
	my_set = set()
	my_set = set(list_o_stuff)
	new_list = list(my_set)
	return new_list

print remove_dups(my_list)