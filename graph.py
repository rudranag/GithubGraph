import datetime
import calendar
import random
import subprocess
import time

EMAIL = "rudranag.katroju@gmail.com"
USERNAME = "rudranag"
REPO_URL = "git@github.com:rudranag/tests.git"

YEAR = datetime.datetime.now().year
FROM_MONTH = 1
TO_MONTH = 10  # exclusive


COMMIT_THRESHOLD_PER_MONTH = 20
MIN_COMMITS = 1
MAX_COMMITS = 26


def make_commits(year, month, day):

    commit_command = f'git commit --allow-empty -m "Empty commit" --date="{year}-{month}-{day} 12:00:00"'

    subprocess.run(commit_command, shell=True)


def get_days_in_month(year, month):
    # Use calendar.monthrange() to get the number of days in the month
    _, days_in_month = calendar.monthrange(year, month)
    return days_in_month


def pick_random_numbers(n, threshold):
    # Pick 'threshold' number of unique random numbers from the range 1 to n
    return sorted(random.sample(range(1, n + 1), threshold))


def setup():

    subprocess.run("rm -rf .git", shell=True)
    subprocess.run("git init", shell=True)

    subprocess.run(f'git config user.name "{USERNAME}"', shell=True)
    subprocess.run(f'git config user.email "{EMAIL}"', shell=True)

    subprocess.run("git add README.md", shell=True)
    subprocess.run('git commit -m "first commit"', shell=True)
    subprocess.run(f"git remote add origin {REPO_URL}", shell=True)
    subprocess.run("git push -u origin master", shell=True)


def main():
    
    setup()

    for month in range(FROM_MONTH, TO_MONTH):
        month_days = get_days_in_month(YEAR, month)
        days_committed = pick_random_numbers(month_days, COMMIT_THRESHOLD_PER_MONTH)

        # each day in a month
        for each_day in days_committed:
            # no of commits
            for _ in range(random.randint(MIN_COMMITS, MAX_COMMITS)):
                make_commits(year=YEAR, month=month, day=each_day)

    time.sleep(5)
    subprocess.run("git push", shell=True)

    print("Success")
    


if __name__ == "__main__":
    main()
