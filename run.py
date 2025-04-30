import json
from datetime import datetime, timedelta
from collections import defaultdict
def check_capacity(max_capacity: int, guests: list) -> bool:
    hotel = defaultdict(list)
    for guest in guests:
        check_in = datetime.strptime(guest['check-in'], "%Y-%m-%d").date()
        check_out = datetime.strptime(guest['check-out'], "%Y-%m-%d").date()

        current_day = check_in
        while current_day < check_out:
            hotel[current_day].append(guest['name'])
            current_day+=timedelta(days=1)
    for days, names in hotel.items():
        if len(names) > max_capacity:
            return False
    
    return True

if __name__ == "__main__":
    # Чтение входных данных
    max_capacity = int(input())
    n = int(input())


    guests = []
    for _ in range(n):
        guest_json = input()
        guest_data = json.loads(guest_json)
        guests.append(guest_data)


    result = check_capacity(max_capacity, guests)
    print(result)
    