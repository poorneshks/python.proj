import logging
import time
import random

# Configure logging to log to a file
logging.basicConfig(filename='log_output.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# Define log message formats
formats = {
    logging.INFO: "INFO message",
    logging.DEBUG: "DEBUG message",
    logging.ERROR: "ERROR message"
}

# Define log levels to cycle through (expanded for demonstration)
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR, logging.WARNING]

# Main loop to log messages
def main(interval):
    try:
        while True:
            # Randomly select a log level
            log_level = random.choice(log_levels)
            
            # Get the log message format for the selected log level
            log_message = formats.get(log_level, "Unknown log level")
            
            # Log the message
            logger.log(log_level, log_message)
            
            # Sleep for the specified interval
            time.sleep(interval)
            
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        logger.info("Logging interrupted. Exiting.")
        raise SystemExit
    except Exception as e:
        # Log any other exceptions
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        interval = float(input("Enter logging interval (in seconds): "))
        main(interval)
    except ValueError:
        print("Invalid input. Please enter a valid number for the logging interval.")
    finally:
        # Close the logger explicitly
        logging.shutdown()
