#dictionaries associate a key to a value

example_dict = {
    "class"      :"ASTR19",  #key on the left, value on the right
    "prof"       :"Brant",
    "awesomeness":10         #values in a  dict can be different types
}


#Values on the right are now associated with the keys on the left

print(type(example_dict)) #prints <class 'dict'>

course = example_dict["class"] #sets course = ASTR19

example_dict["awesomeness"] += 1 #increments the value associated with "awesomeness" by one

for x in example_dict:
    print(x, example_dict[x])



