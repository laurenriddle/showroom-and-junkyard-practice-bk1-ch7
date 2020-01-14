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
