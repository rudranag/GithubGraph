import pytest
from unittest import mock
import subprocess
import random
import calendar
import datetime

# Mocking subprocess.run
@pytest.fixture(autouse=True)
def mock_subprocess_run():
    with mock.patch('subprocess.run') as mock_run:
        yield mock_run

# Mocking random.sample
@pytest.fixture(autouse=True)
def mock_random_sample():
    with mock.patch('random.sample') as mock_sample:
        yield mock_sample

# Mocking calendar.monthrange
@pytest.fixture(autouse=True)
def mock_calendar_monthrange():
    with mock.patch('calendar.monthrange') as mock_monthrange:
        yield mock_monthrange

# Mocking datetime.datetime.now
@pytest.fixture(autouse=True)
def mock_datetime_now():
    with mock.patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime.datetime(2023, 10, 1)
        yield mock_datetime

# Mocking the functions in the source code
import graph

@pytest.fixture(autouse=True)
def mock_graph_functions():
    with mock.patch('graph.make_commits') as mock_make_commits, \
         mock.patch('graph.get_days_in_month') as mock_get_days_in_month, \
         mock.patch('graph.pick_random_numbers') as mock_pick_random_numbers, \
         mock.patch('graph.main') as mock_main:
        yield mock_make_commits, mock_get_days_in_month, mock_pick_random_numbers, mock_main

# happy path - make_commits - Test that make_commits executes the git command with correct date
def test_make_commits_executes_git_command(mock_subprocess_run):
    graph.make_commits(2023, 5, 15)
    mock_subprocess_run.assert_called_with(
        'git commit --allow-empty -m "Empty commit" --date="2023-5-15 12:00:00"',
        shell=True
    )


# happy path - get_days_in_month - Test that get_days_in_month returns correct number of days for a typical month
def test_get_days_in_month_typical_month(mock_calendar_monthrange):
    mock_calendar_monthrange.return_value = (0, 31)
    days = graph.get_days_in_month(2023, 5)
    assert days == 31


# happy path - pick_random_numbers - Test that pick_random_numbers returns correct number of unique numbers
def test_pick_random_numbers_unique_numbers(mock_random_sample):
    mock_random_sample.return_value = [1, 2, 3, 4, 5]
    result = graph.pick_random_numbers(30, 5)
    assert len(result) == 5
    assert result == [1, 2, 3, 4, 5]


# happy path - main - Test that main function exits early when EMAIL is not set
def test_main_exits_early_without_email(mock_subprocess_run, capsys):
    graph.EMAIL = ''
    graph.USERNAME = 'user'
    graph.REPO_URL = 'http://repo.url'
    graph.main()
    captured = capsys.readouterr()
    assert 'Email is required' in captured.out
    mock_subprocess_run.assert_not_called()


# happy path - main - Test that main function initializes git repository correctly
def test_main_initializes_git_correctly(mock_subprocess_run):
    graph.EMAIL = 'user@example.com'
    graph.USERNAME = 'user'
    graph.REPO_URL = 'http://repo.url'
    graph.main()
    expected_calls = [
        mock.call('git init', shell=True),
        mock.call('git config user.name "user"', shell=True),
        mock.call('git config user.email "user@example.com"', shell=True)
    ]
    mock_subprocess_run.assert_has_calls(expected_calls, any_order=True)


# edge case - make_commits - Test that make_commits handles invalid date gracefully
def test_make_commits_invalid_date(mock_subprocess_run):
    graph.make_commits(2023, 2, 30)
    mock_subprocess_run.assert_not_called()


# edge case - get_days_in_month - Test that get_days_in_month handles leap year February correctly
def test_get_days_in_month_leap_year_february(mock_calendar_monthrange):
    mock_calendar_monthrange.return_value = (0, 29)
    days = graph.get_days_in_month(2020, 2)
    assert days == 29


# edge case - pick_random_numbers - Test that pick_random_numbers returns empty list when threshold is zero
def test_pick_random_numbers_zero_threshold(mock_random_sample):
    mock_random_sample.return_value = []
    result = graph.pick_random_numbers(30, 0)
    assert len(result) == 0


# edge case - main - Test that main function exits early when USERNAME is not set
def test_main_exits_early_without_username(mock_subprocess_run, capsys):
    graph.EMAIL = 'user@example.com'
    graph.USERNAME = ''
    graph.REPO_URL = 'http://repo.url'
    graph.main()
    captured = capsys.readouterr()
    assert 'Username is required' in captured.out
    mock_subprocess_run.assert_not_called()


# edge case - main - Test that main function handles missing REPO_URL gracefully
def test_main_exits_early_without_repo_url(mock_subprocess_run, capsys):
    graph.EMAIL = 'user@example.com'
    graph.USERNAME = 'user'
    graph.REPO_URL = ''
    graph.main()
    captured = capsys.readouterr()
    assert 'Repo url is required' in captured.out
    mock_subprocess_run.assert_not_called()


