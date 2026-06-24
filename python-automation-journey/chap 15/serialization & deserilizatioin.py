# ==============================================================================
# MAIN PRACTICE FILE: ADVANCED SERIALIZATION AND DESERIALIZATION
# Author: Sehar Ali
# ==============================================================================

import json
import pickle

# ==============================================================================
# PART 1: TEXT SERIALIZATION (JSON MODULE)
# ==============================================================================
print("=== Running Part 1: JSON Processing ===")

L = [1, 2, 3, 4]
with open('demo.json', 'w') as f:
    json.dump(L, f)

d = {
    'name': 'Sehar',
    'age': 24,
    'gender': 'female'
}
with open(r'D:\python-automation-journey\demo.json', 'w') as f:
    json.dump(d, f, indent=4)

t = (1, 2, 3, 4)
with open('demo.json', 'w') as f:
    json.dump(t, f)

class PersonJSON:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

person_json_obj = PersonJSON('Sehar', 'Ali', 24, 'female')

def show_object_as_dict(obj):
    if isinstance(obj, PersonJSON):
        return {
            'name': obj.fname + ' ' + obj.lname,
            'age': obj.age,
            'gender': obj.gender
        }
    raise TypeError("Object is not an instance of PersonJSON")

with open('demo.json', 'w') as f:
    json.dump(person_json_obj, f, default=show_object_as_dict, indent=4)

with open('demo.json', 'r') as f:
    loaded_dict = json.load(f)
    print("JSON Loaded Data:", loaded_dict)
    print("JSON Loaded Type:", type(loaded_dict))


# ==============================================================================
# PART 2: BINARY SERIALIZATION (PICKLE MODULE - BOTH BINARY METHODS)
# ==============================================================================
print("\n=== Running Part 2: Pickle (Binary Processing) ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Object create kiya
p = Person('Sehar', 23)


# --- SYSTEM 1: File-Based Binary (dump & load) ---
# Yeh method data ko direct hard drive par kisi file (.pkl) mein save/read karta hai.

print("\n--- System 1: File-Based Pickle ---")

# 1. Pickling to File ('wb' mode zaroori hai)
with open('person.pkl', 'wb') as f:
    pickle.dump(p, f)  
print("System 1: Object saved in 'person.pkl' file.")

# 2. Unpickling from File ('rb' mode zaroori hai)
with open('person.pkl', 'rb') as f:
    loaded_from_file = pickle.load(f)

print("Loaded Type from File:", type(loaded_from_file))
loaded_from_file.display_info()


# --- SYSTEM 2: Memory/Bytes-Based Binary (dumps & loads) ---
# 's' ka matlab hai Serialization to String/Bytes. 
# Yeh koi file nahi banata, balki object ko direct Python ki RAM/memory mein byte-stream bana deta hai.

print("\n--- System 2: Memory-Based Pickle (dumps/loads) ---")

# 1. Pickling to Bytes Object (dumps)
# Isme kisi file variable 'f' ki zaroorat nahi hoti
binary_bytes = pickle.dumps(p)  

print("System 2: Object converted to RAM Bytes stream.")
print("Binary Stream Preview:", binary_bytes[:50])  # Pehle 50 bytes ka preview print karega
print("Data Type of Stream:", type(binary_bytes))      # Output: <class 'bytes'>

# 2. Unpickling from Bytes Object (loads)
# Yeh un bytes ko wapas real object mein badal dega
loaded_from_bytes = pickle.loads(binary_bytes)

print("Loaded Type from Bytes:", type(loaded_from_bytes))
loaded_from_bytes.display_info()