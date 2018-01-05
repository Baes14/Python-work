# for count in range(1,10**6+1):
# 	print(count)

# million=list(range(1,10**6+1))
# print(min(million))
# print(max(million))
# print(sum(million))

# # Odd numbers
# for odd in range(1,20,2):
# 	print(odd)

# # Threes
# threes=list(range(3,31,3))
# print(threes)
# for three in threes:
# 	print(three)

# # Cubes
# cubes=[]
# for cube in range(1,11):
# 	cubes.append(cube**3)
# 	print(cube**3)

## Comprehension
cubes=[cube**3 for cube in range(1,11)]
print(cubes)