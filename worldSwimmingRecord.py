world_record = float(input())
distance_meters = float(input())
time_for_meter = float(input())

ivan_time = distance_meters * time_for_meter
water_resistance = distance_meters // 15

if water_resistance >= 1:
    ivan_time += water_resistance * 12.5

if world_record < ivan_time:
    difference = ivan_time - world_record
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
elif ivan_time < world_record:
    print(f" Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
