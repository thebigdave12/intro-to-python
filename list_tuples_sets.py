list = ["bob", "rolf", "tom"] # can add items, keeps order
tuple = ("bob", "rolf", "tom") # cannot add items, keeps order
set = {"bob", "rolf", "tom"} # can add items, but no duplicates, does keep order 

print(list[1]) # can use for list or tuple but set will give you random item

list.append("smith") # can use for list to add item to list 

list.remove("bob") # can use to remove item from list

set.add("smith") # can use add to make additon to a set

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = abroad.difference(friends)
print(local_friends) # will show Rolf

# .union unites two sets
# .intersection identifies items that are in both sets

both = friends.intersection(abroad)
print(both)