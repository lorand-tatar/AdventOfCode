file_path = 'inputs/day12.txt'

edges = []
large_caves = []
small_caves = []
with open(file_path, 'r') as file:
    for line in file:
        (a, b) = line.rstrip().split('-')
        edges.append((a, b))
        if a[0].islower():
            if a not in small_caves:
                small_caves.append(a)
        else:
            if a not in large_caves:
                large_caves.append(a)
        if b[0].islower():
            if b not in small_caves:
                small_caves.append(b)
        else:
            if b not in large_caves:
                large_caves.append(b)

graph = {}
for vertex in small_caves:
    graph[vertex] = []
for vertex in large_caves:
    graph[vertex] = []
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
# print(graph)


def create_route_string(route):
    separator = "#"
    hashed = ""
    for vertex in route:
        hashed = hashed + separator + vertex
    hashed += "#end"
    # print(hashed)
    return hashed


def find_routes(complicated, spec_small=None):
    to_check = [['start', set({}), [], 2]]
    routes = set({})
    while len(to_check) != 0:
        last_junction = to_check.pop()
        # print("Checking", last_junction)
        if last_junction[0] == 'end':
            # print("Found a route")
            routes.add(create_route_string(last_junction[2]))
            # print("Routes so far", routes)
        else:
            spec_cnt = last_junction[3]
            if last_junction[0] == spec_small:
                spec_cnt -= 1
            visited_small = set({})
            for small in last_junction[1]:
                visited_small.add(small)
            if last_junction[0] in small_caves and (last_junction[0] != spec_small or spec_cnt == 0 or not complicated):
                visited_small.add(last_junction[0])
            for neighbor in graph[last_junction[0]]:
                if neighbor not in last_junction[1]:
                    updated_route = []
                    for route_element in last_junction[2]:
                        updated_route.append(route_element)
                    updated_route.append(last_junction[0])
                    to_check.append([neighbor, visited_small, updated_route, spec_cnt])
        # print("To check", to_check)
    return routes


print("Number of possible routes with small caves visited only once:", len(find_routes(complicated=False)))

all_routes = set({})
for special_small in small_caves:
    if special_small not in {'start', 'end'}:
        # print("####### Today's special:", special_small)
        all_routes = all_routes.union(find_routes(complicated=True, spec_small=special_small))
# print(all_routes)
print("All routes found with only one special small cave:", len(all_routes))
