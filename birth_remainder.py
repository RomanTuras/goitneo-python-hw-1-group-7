'''HW-1 Birthday remainder module'''

from datetime import datetime, timedelta

def get_birthdays_per_week(users: list, is_debug = False) -> None:
    '''
    Getting users, having birthdays on next working week
    '''

    if is_debug:
        today = datetime(2023, 12, 30).date()
        users = [
            {"name": "Bill Gates", "birthday": datetime(1955, 12, 31)},
            {"name": "Kate", "birthday": datetime(1955, 1, 3)},
            {"name": "John Dou", "birthday": datetime(1955, 1, 5)},
            {"name": "Kianu", "birthday": datetime(1955, 2, 24)},
            {"name": "Luke Skywalker", "birthday": datetime(1975, 2, 25)}
            ]
    else:
        today = datetime.today().date()

    next_seven_days = today + timedelta(days=7)

    # Create a dictionary to store users by weekday
    users_by_weekday = {day: [] for day in [
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}

    # Organize users by weekday if their birthday falls within the next 7 days
    for user in users:
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if today <= birthday_this_year <= next_seven_days:
            weekday = birthday_this_year.strftime('%A')
            # If the birthday falls on Saturday or Sunday, move it to the next Monday
            if weekday=='Saturday' and birthday_this_year + timedelta(days=2) <= next_seven_days:
                users_by_weekday['Monday'].append(user['name'])
            elif weekday=='Sunday' and birthday_this_year + timedelta(days=1) <= next_seven_days:
                users_by_weekday['Monday'].append(user['name'])
            else:
                users_by_weekday[weekday].append(user['name'])


    # Print the result
    for day, user_list in users_by_weekday.items():
        if user_list:
            formatted_users = ', '.join(user_list)
            print(f"{day}: {formatted_users}")

if __name__ == "__main__":
    get_birthdays_per_week([], is_debug = True)
