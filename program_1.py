def rainfall():
    rainfall_list = []

    for month in range(12):
        rainfall = float(input(f"Enter the total rainfall for month {month + 1}: "))
        rainfall_list.append(rainfall)

    total_rainfall = sum(rainfall_list)
    average_rainfall = total_rainfall / 12
    max_rainfall = max(rainfall_list)
    min_rainfall = min(rainfall_list)

    print(f"Total rainfall for the year: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {average_rainfall:.2f}")
    print(f"Month with the highest rainfall: Month {rainfall_list.index(max_rainfall) + 1} ({max_rainfall:.2f})")
    print(f"Month with the lowest rainfall: Month {rainfall_list.index(min_rainfall) + 1} ({min_rainfall:.2f})")

rainfall()
