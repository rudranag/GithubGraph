import datetime
import calendar
import random
import subprocess

EMAIL = "rudranag.katroju@gmail.com"
USERNAME = "rudranag"

YEAR = datetime.datetime.now().year
CURRENT_MONTH = datetime.datetime.now().month

COMMIT_THRESHOLD_PER_MONTH = 20
MIN_COMMITS = 1
MAX_COMMITS = 26


def commiter(year, month, day):

    commit_command = f'git commit --allow-empty -m "Empty commit" --date="{year}-{month}-{day} 12:00:00"'

    subprocess.run(commit_command, shell=True)


def get_days_in_month(year, month):
    # Use calendar.monthrange() to get the number of days in the month
    _, days_in_month = calendar.monthrange(year, month)
    return days_in_month


def pick_random_numbers(n, threshold):
    # Pick 'threshold' number of unique random numbers from the range 1 to n
    return sorted(random.sample(range(1, n + 1), threshold))


def main():

    subprocess.run(f'git config user.email "{EMAIL}"', shell=True)
    subprocess.run(f'git config user.name "{USERNAME}"', shell=True)
    
    for month in range(1, CURRENT_MONTH):
        month_days = get_days_in_month(YEAR, month)
        days_committed = pick_random_numbers(month_days, COMMIT_THRESHOLD_PER_MONTH)

        for each_day in days_committed:
            for _ in range(random.randint(MIN_COMMITS, MAX_COMMITS)):
                commiter(year=YEAR, month=month, day=each_day)

    push_command = "git push"
    push_result = subprocess.run(push_command, shell=True, capture_output=True)

    if push_result.returncode != 0:
        return {
            "statusCode": 500,
            "body": f"Error pushing changes: {push_result.stderr.decode()}",
        }

    return {"statusCode": 200, "body": "Changes committed and pushed successfully!"}


if __name__ == "__main__":
    main()
