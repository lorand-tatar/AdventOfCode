input_file_path = "inputs/day5_input.txt"
boarding_passes = []
with open(input_file_path, 'r') as file:
    for seat in file:
        seat = seat.rstrip()
        seat = seat.replace('B', '1')
        seat = seat.replace('F', '0')
        seat = seat.replace('L', '0')
        seat = seat.replace('R', '1')
        seat = int(seat, 2)
        boarding_passes.append(seat)
print(boarding_passes)
print(max(boarding_passes))

found_the_first = False
for i in range(1024):
    if i in boarding_passes:
        found_the_first = True
    if found_the_first and i not in boarding_passes:
        print("The missing seat ID:", i)
        break
