mylist = [1, 2, 2, 3, 4, 5, 5]

List<String> list2 = new ArrayList<String>();

HashSet<String> lookup = new HashSet<String>();
    for (String item : list) {
        if (lookup.add(item)) {
            // Set.add returns false if item is already in the set
            list2.add(item);
        }
    }
list = list2;


mylist = list(set(mylist))
print mylist

def no_dups(mylist):
    out_put = []
    for x in mylist:
        if x not in mylist:
            out_put.append(x)
    return out_put
print no_dups(mylist)
