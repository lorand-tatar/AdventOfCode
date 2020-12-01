file_path = 'inputs/day6_input.txt'


class Planet:
    def __init__(self, direct_center, name):
        self.name = name
        self.center = direct_center
        self.minions = set()


com = Planet(None, "COM")
known_planets = {com}
with open(file_path, 'r') as file:
    for direct_orbit in file:
        (center, minion) = direct_orbit.split(")")
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
        center_obj.minions.add(minion_obj)
        if minion_obj.center is None:
            minion_obj.center = center_obj

print([x.name for x in known_planets])
print("Count of planets:", len(known_planets))

total_orbits = 0
for planet in known_planets:
    orbits_of_current = 0
    next = planet
    while next.center is not None:
        orbits_of_current += 1
        next = next.center
    total_orbits += orbits_of_current

print("Total orbits for all known planets:", total_orbits)
