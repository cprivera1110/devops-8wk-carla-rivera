trainees = ["Carla", "Patrick", "Joban", "Josie", "Haiman", "Calvin", "Lawrence"]

# foreach loop
for trainee in trainees:
    print(f"Welcome {trainee} to Tech Consulting!")
print()

# for loop - executes a block of code for a specific amount of times
for i in range(1,10):
    print("index ", i)
print()

# while loop - a loop that repeats a block of code so long as the conditions are met
counter = 1
while counter <= 5:
    print("counter: ", counter)
    counter += 1
print("end of while loop")
print()

# do while loop - does not technically exist but can be simulated with a while loop like so
# condition = some condition
# while True:
#     # loop body (runs at least once)
#     if not condition:
#         break
count = 1
while True:
    print("count: ", count)
    count += 1
    if not(count < 5): # loop continues while count < 5
        break
print()

# Print a triangle pattern using for loop
for i in range(1,6):
    print(i * "*")
print()

for i in range(0,8):
    print(i * "*")
for i in range(8,0,-1):
    print(i * "*")
print()

for i in range(1, 6):
    if i == 3:
        break # break out of the loop completely and move to the next line of code outside the loop
    print(i)
print()
for i in range(1, 6):
    if i == 3:
        continue # skip the current iteration and move to the next
    print(i)
print()
for i in range(1, 6):
    if i == 3:
        pass # do nothing and move to the next iteration; can be useful when you need syntactically valid code but don't want to implement any logic yet
    print(i)
print()

servers = ["web01","web02","web03","web04","db01","db02","db03"]
for server in servers:
    if server == "db01":
        continue # skip the current iteration
    print("Checking: ", server)