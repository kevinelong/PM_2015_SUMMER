import cPickle as pickle

pickle_file = '/home/jay/PycharmProjects/PM_2015_SUMMER/StudentWork/JayMattingly/PMSchoolWork/test.pickle'

progress_report_dict = {
    'james': {'gender': "male or female", 'age': 24, 'weight': 164, 'height': 72},
    'smith': {'gender': "male or female", 'age': 24, 'weight': 164, 'height': 72},
    'gordon': {'gender': "male or female", 'age': 24, 'weight': 164, 'height': 72},
    'munster': {'gender': "male or female", 'age': 24, 'weight': 164, 'height': 72},
    'robinson': {'gender': "male or female", 'age': 24, 'weight': 164, 'height': 72}
}


def write_to_file(progress_report_dict):
    with open(pickle_file, 'w') as prd_file:
        pickle.dump(progress_report_dict, prd_file)

def get_from_file():
    with open(pickle_file) as prd_file:
        loaded_obj = pickle.load(prd_file)
    return loaded_obj

#write_to_file(progress_report_dict)
print get_from_file()