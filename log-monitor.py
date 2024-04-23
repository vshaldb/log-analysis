import logging
import time
import os
import re
from sendemail import email

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the root logger level to DEBUG

# Create a logger
logger = logging.getLogger(__name__)

# Define log message formats
formats = {
    logging.INFO: "INFO message",
    logging.WARN: "WARN message",
    logging.ERROR: "ERROR message"
}

# Define log levels to cycle through
log_levels = [logging.INFO, logging.ERROR, logging.WARN]

LOG_FILE = "hadoop.log"

# Get the initial size of the log file
file_size = 0

# Main loop to continuously monitor the log file
while True:
    try:
        # Get the current size of the log file
        current_file_size = os.path.getsize(LOG_FILE)
        
        # Check if the file size has increased
        if current_file_size > file_size:
            # Open the log file and move to the previous position
            with open(LOG_FILE, "r") as file:
                file.seek(file_size)
                
                # Read new lines from the log file
                for line in file:
                    # Check the log level and extract the message
                    if "WARN" in line:
                        log_level = logging.WARN
                        log_message = line.split("]", 1)[-1].strip()
                    elif "ERROR" in line:
                        log_level = logging.ERROR
                        log_message = line.split("]", 1)[-1].strip()

                        #Occurence of Error
                        date_of_occurence = re.search(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", line)
                        time_of_occurence = re.search(r"[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?", line)

                        #HTML content for email to sent out
                        html_content = f"<p> Hi All, <br> We have found following error in your application. <br> Error Details: <br> Message: {log_message} <br> Date: {date_of_occurence.group()} <br> Time: {time_of_occurence.group()} <br><br> Thanks,<br> DevOps Team"
                        #Initialize Email
                        mail = email(html_content)
                        #Will send out an email to respective Owners with Error details
                        mail.sendEmail()
                    elif "INFO" in line:
                        log_level = logging.INFO
                        log_message = line.split("]", 1)[-1].strip()
                    else:
                        # Skip lines that don't contain log levels
                        continue
                    
                    # Log the message
                    logger.log(log_level, log_message)
                    
            # Update the file size
            file_size = current_file_size
        
        # Sleep for a short interval before checking the log file again
        time.sleep(1)
        
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nLogging interrupted. Exiting.")
        break