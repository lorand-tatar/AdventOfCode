file_path = 'inputs/day1.txt'

depths = []
with open(file_path, 'r') as file:
    for depth in file:
        depths.append(int(depth))

prev = depths[0]
sink_cnt = 0
for depth in depths[1:]:
    # print("Prev:", prev)
    # print("actual:", depth)
    if prev < depth:
        # print("Sink detected")
        sink_cnt += 1
    prev = depth

print("# of all single sinking:", sink_cnt)

prev_depth_trio_sum = sum(depths[:3])
trio_sink_cnt = 0
for i in range(1, len(depths) - 2):
    new_trio_sum = sum(depths[i:i + 3])
    print(prev_depth_trio_sum)
    print(new_trio_sum)
    if prev_depth_trio_sum < new_trio_sum:
        print("Trio sink detected")
        trio_sink_cnt += 1
    prev_depth_trio_sum = new_trio_sum

print("# of trio sinkings:", trio_sink_cnt)
