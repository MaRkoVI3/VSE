n = int(input())
time = input()

taxi_day = 0.70 + n * 0.79
taxi_night = 0.70 + n * 0.90
bus = n * 0.09
train = n * 0.06

if time == "ден":
    taxi = taxi_day
else:
    taxi = taxi_night

print(f"{min(taxi, bus, train):.2f}")
