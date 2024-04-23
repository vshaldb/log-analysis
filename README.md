# Log Analysis Script

This Python script `log-analysis.py` continuously monitors a log file (`hadoop.log` by default), detects new log entries, extracts relevant information from ERROR and WARN logs, and sends out email notifications for each ERROR log.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- The `sendgrid` library for sending emails. You can install it using pip:

```shell
pip install sendgrid
```

## How to Use

1. **Configure Log File**: Ensure that the log file path is correctly set in the script. By default, it monitors a file named `hadoop.log`.

2. **Set Up SendGrid API Key**: You need to set up a SendGrid account and obtain an API key. Then, set this API key as an environment variable named `SENDGRID_API_KEY`.

3. **Customize Email Configuration**: In the `sendEmail.py` file, customize the email sender, recipient, and subject as per your requirements.

4. **Run the Script**: Execute the `log-analysis.py` script using Python:

```shell
python log-analysis.py
```

5. **Monitor Logs**: The script will continuously monitor the log file. Whenever it detects a new ERROR log entry, it extracts relevant information (message, date, time) and sends an email notification to the configured recipient.

## File Structure

- `log-analysis.py`: The main script for log analysis.
- `sendEmail.py`: A helper class for sending email notifications.
- `hadoop.log`: A Sample log file consisting hadoop logs.

## Customization

- You can customize the log file path, email sender, recipient, and subject as per your requirements by modifying the script variables.
- Additional error handling or logging functionality can be added as needed.

