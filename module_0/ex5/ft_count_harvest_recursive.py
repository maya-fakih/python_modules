def count_days(day, total_days):
        if day > total_days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count_days(day + 1, total_days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_days(1, days)

