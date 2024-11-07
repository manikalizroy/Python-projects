import time

hours = int(input("Enter the time in hours: ")) 

my_time = hours * 3600

for x in range(my_time, 0, -1):
    sec = x % 60
    min = int(x // 60) % 60
    hr = int(x // 3600)
    print(f"{hr:02}:{min:02}:{sec:02}")
    time.sleep(1)

print("TIME'S UP!")