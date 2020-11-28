file_path = 'inputs/day6a_input.txt'


class Planet:
    def __init__(self, direct_center, name):
        self.name = name
        self.center = direct_center
        self.minions = set()


# Reading the planets graph
# Central object
com = Planet(None, "COM")
known_planets = {com}
with open(file_path, 'r') as file:
    for direct_orbit in file:
        (center, minion) = direct_orbit.split(")")
        # Removing new line char
        minion = minion.rstrip()
        if center not in [x.name for x in known_planets]:
            center_obj = Planet(None, center)
            known_planets.add(center_obj)
        else:
            for planet in known_planets:
                if planet.name == center:
                    center_obj = planet
                    break
        if minion not in [x.name for x in known_planets]:
            minion_obj = Planet(center_obj, minion)
            known_planets.add(minion_obj)
        else:
            for planet in known_planets:
                if planet.name == minion:
                    minion_obj = planet
                    break
        # Linking planets both directions
        center_obj.minions.add(minion_obj)
        if minion_obj.center is None:
            minion_obj.center = center_obj

# print([x.name for x in known_planets])
# print("Count of planets:", len(known_planets))

# Determining what planet Santa and you are orbiting
for x in known_planets:
    if x.name == "YOU":
        you_center = x.center
    if x.name == "SAN":
        san_center = x.center

# Collecting centers from you to COM
you_indirect_centers = [you_center]
actual_obj = you_center
while actual_obj.center is not None:
    actual_obj = actual_obj.center
    you_indirect_centers.append(actual_obj)

# Collecting centers from Santa to COM
san_indirect_centers = [san_center]
actual_obj = san_center
while actual_obj.center is not None:
    actual_obj = actual_obj.center
    san_indirect_centers.append(actual_obj)

print("san line:", [x.name for x in san_indirect_centers])
print("you line:", [x.name for x in you_indirect_centers])

steps = 0
curr_center = you_indirect_centers[0]
# Moving from the direct your center to first planet which is an indirect center of Santa's direct center
while curr_center not in san_indirect_centers:
    steps += 1
    curr_center = curr_center.center
print("Steps on your line:", steps)
print("First common element with santa's line:", curr_center.name)
steps += san_indirect_centers.index(curr_center)

print("Minimum necessary steps from YOUr planet to SANta's planet:", steps)
