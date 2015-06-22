# create a new empty dictionary
me = {}
# annother way to do the same
me = dict()

#define two new keys for first and last name
me["first"] = "Kevin"
me["last"] = "Long"

#we often see this done in short hand all at once e.g.:
me = {"first": "Kevin", "Last": "Long"}

#print first name
print(me["first"])

#print last name
print(me["last"])

#print full name
print(me["first"] + " " + me["last"])
