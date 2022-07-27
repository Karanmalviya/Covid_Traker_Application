import requests
import json

my_keys = ['active', 'confirmed', 'recovered', 'deceased']
my_dict = {}
# getting the data from the api
data = requests.get('https://api.covid19india.org/state_district_wise.json')
# getting the textual data
text_data = data.text
# converting into python datatype that is dictionary
parse_data = json.loads(text_data)


# function for getting all State names.
def get_state_names():
    return parse_data.keys()


# function for getting district names.
def get_district_names(state_name):
    return parse_data[state_name]


# function for getting district data.
def get_district_data(state_name, district_name):
    return parse_data[state_name][district_name].keys()


# function for getting district data details.
def get_district_data_details(district_data):
    obj = parse_data[district_data]['districtData']
    my_list = []
    for i, j in obj.items():
        my_list.append(i)
        for k in my_keys:
            my_list.append({k: j[k]})
    return my_list

def get_district_name_list(state_name):
    obj = parse_data[state_name]['districtData']
    my_list = []
    for i, j in obj.items():
        my_list.append(i)

    return my_list


# function for getting single district data details.
def get_single_district_data_details(state_name, district_name):
    obj = parse_data[state_name]['districtData'][district_name]
    district_dict = {}
    for i in my_keys:
        district_dict[i] = obj[i]
    return district_dict
