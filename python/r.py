import random
import time

def generate_random_date(start_date, end_date):
    """Generate a random date between the start and end dates."""
    start_time = time.mktime(time.strptime(start_date, "%Y-%m-%d"))
    end_time = time.mktime(time.strptime(end_date, "%Y-%m-%d"))
    random_time = random.uniform(start_time, end_time)
    random_date = time.strftime("%Y-%m-%d", time.localtime(random_time))
    return random_date
start_date = "2022-01-01"
end_date = "2022-12-31"

random_date = generate_random_date(start_date, end_date)
print(f"Random date between {start_date} and {end_date}: {random_date}")

