import time
start_time = time.time()
# Calculate Average temperature

days = int(input("Enter the number of days:"))

temperatures = []

for i in range(1, days+1):
    temperature = (float(input("Enter the temperature of Day " + str(i) + ":")))
    temperatures.append(temperature)
s = sum(temperatures)
avg = s/days
print(f"The average temperature during this time period is {avg}")


#Find the days above Average temperature

days_above_avg_temp = []

for temp in temperatures:
    if temp > avg:
        days_above_avg_temp.append(temperatures.index(temp) + 1)
print(f"Days above average temperatures are {days_above_avg_temp}")

#Calculating Time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")