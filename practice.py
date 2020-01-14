# create an empty set
showroom = set()

# add four types of cars to the set
showroom.add("Sedan")
showroom.add("Coupe")
showroom.add("Convertibles")
showroom.add("SUVs")

# print the length of the showroom set
print(len(showroom))

# Pick one of the items in your show room and add it to the set again.
showroom.add("Sedan")

# Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)


# Using update(), add two more car models to your showroom with another set.

showroom.update({"Jeep", "Truck"})

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("Jeep")

print(showroom)



# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.

junkyard = {"versa", "Jeep", "Truck", "mini van"}


# Use the intersection method to see which cars exist in both the showroom and that junkyard.

print(showroom.intersection(junkyard))


# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.

print(showroom.union(junkyard))

# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.

showroom.discard("mini van")
print(showroom)