# GitHub Contribution Graph Generator

This script allows you to generate GitHub contributions by creating empty commits with custom dates. It's useful for testing or filling your contribution graph for demonstration purposes.

## ⚠️ Important Note
This script is for educational purposes only. Using scripts to artificially inflate your GitHub contributions may violate GitHub's terms of service. Use responsibly.

## Prerequisites

- Python 3.6 or higher
- A new private repository on GitHub

## Setup Instructions

1. **Create a New Private Repository**
   - Go to GitHub and create a new private repository
   - Do not initialize it with a README, .gitignore, or license

2. **Clone This Repository**
   ```bash
   git clone <this-repo-url>
   cd <repo-name>
   ```

3. **Configure the Script**
   Open `graph.py` and modify the following variables at the top of the file:
   ```python
   EMAIL = "your-github-email@example.com"
   USERNAME = "your-github-username"
   REPO_URL = "https://github.com/username/repo-name.git"  # Your new private repo URL
   ```

4. **Customize Commit Parameters (Optional)**
   You can modify these variables to adjust the commit pattern:
   ```python
   YEAR = datetime.datetime.now().year  # Current year by default
   FROM_MONTH = 1                       # Starting month (1-12)
   TO_MONTH = 10                        # Ending month (exclusive)
   
   COMMIT_THRESHOLD_PER_MONTH = 20      # Number of days per month to commit
   MIN_COMMITS = 1                      # Minimum commits per day
   MAX_COMMITS = 26                     # Maximum commits per day
   ```

## Usage

1. **Run the Script**
   ```bash
   python graph.py
   ```

2. **What the Script Does**
   - Initializes a new git repository
   - Configures git with your username and email
   - Creates empty commits with dates spread across your specified time range
   - Pushes all commits to your private repository

3. **Verify Results**
   - Visit your GitHub profile
   - Check your contribution graph
   - The new commits should appear in your contribution history

## Customization

### Adjusting Time Range
- Modify `FROM_MONTH` and `TO_MONTH` to change the date range
- The script uses the current year by default, but you can modify `YEAR`

### Commit Frequency
- `COMMIT_THRESHOLD_PER_MONTH`: Controls how many days per month will have commits
- `MIN_COMMITS` and `MAX_COMMITS`: Control the range of commits per day

## Troubleshooting

1. **Authentication Issues**
   - Ensure you have proper GitHub authentication set up
   - Use SSH URL if you have SSH keys configured
   - Or use HTTPS URL with your GitHub credentials

2. **Push Errors**
   - Verify your repository URL is correct
   - Ensure you have write permissions to the repository
   - Check if your repository already exists and is properly initialized

3. **Script Errors**
   - Make sure all required variables are properly set
   - Verify Python and Git are properly installed
   - Check if you have necessary permissions to execute Git commands

## License

This project is for educational purposes only. Use at your own risk.

## Contributing

Feel free to submit issues and enhancement requests! 