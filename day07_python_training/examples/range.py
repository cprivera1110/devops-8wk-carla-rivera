# Range()

# Everything in python is a string!!!! Don't forget that!

# start by default is 0
# stop is always required
# step by default is 1
# range(start, stop, step)

nums = range(10) # 0 to 9
for i in nums:
    print(i)
print()

# range(start=0, stop=6, step=1)
r1 = range(0, 6, 1) # 0, 1, 2, 3, 4, 5 - stopped at 6 non-inclusive
for i in r1:
    print(i)
print()

print(list(range(0,6,1))) # 0, 1, 2, 3, 4, 5