data = []

with open('sad_4.txt', 'r') as f:
    for line in f:
        nums = list(map(int, line.split()))
        data.append(nums)

print(data)