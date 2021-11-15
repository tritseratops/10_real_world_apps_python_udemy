import json

gold_data = {
    "gold":
        {
         "conductivity": 33.5,
         "density": 0.255,
         "heat": 0.129,
         "melting point": 2171,
         "thermal expansion": 4.7,
         "yield strength": 288,
         "tensile strength": 441,
         "minimum impact energy": 22
        }
    }

file_path = "105jsongold\\file3.txt"
file_out_path = "105jsongold\\file4.txt"
data = None
with open(file_path, "r") as read_file:
    data = json.load(read_file)

data['metals']['gold']=gold_data['gold']
with open(file_out_path, 'w') as write_file:
    json.dump(data, write_file)
