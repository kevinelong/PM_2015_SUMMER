__author__ = 'lenny'
name = "jesse"
print name
# the [ is how we pull the info out of the dictionary
fullname = {"first":"Jesse", "last":"Fitzjarrell"}
print fullname["last"]
# created the dictionary
kevin = {}
# set the key first to kevin
kevin["first"] = "Kevin"
# set the key last to long
kevin["last"] = "Long"
# referenced the kevin dictionary and printed the last key
print kevin["last"]

fruit = ["apple", "orange", "pear", "banana"]
print fruit[2]
for f in fruit:
    print f