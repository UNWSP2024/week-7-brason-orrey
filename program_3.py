def main():
    population_data = []

    while True:
        year = input("Enter the year (or type 'done' to finish): ")
        if year.lower() == 'done':
            break  
        
        state = input("Enter the name of the state: ")
        population = input("Enter the population: ")

        population_data.append([int(year), state, int(population)])

    print("\nPopulation Data Entered:")
    for data in population_data:
        print(data)

    query_year = int(input("\nEnter a year to get the total population for that year: "))
    
    total_population = sum(item[2] for item in population_data if item[0] == query_year)
    
    if total_population > 0:
        print(f"The total population for the year {query_year} is: {total_population}")
    else:
        print(f"No data available for the year {query_year}.")

main()
