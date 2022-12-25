import json
	
# Data to be written
State_Capital ={
"Bihar": "Patna","Goa": "Panaji","Chattisghar": "Naya Raipur","Madhya Pradesh": "Bhopal","West Bengal" : "Kolkata","Maharastra" : "Mumbai","Gujrat" : "Gandhinagar"
}
#  Writing it in the JSONs file
file = open(r"state.json","w")
json_object = json.dump(State_Capital,file)
