# demonstrate the logging api in Python

# use the built-in logging module
import logging

def main():
    # Use basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG,
                        filemode="w",
                        filename="output.log")
    
    # Try out each of the log levels
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")

    # Output formatted string to the log
    logging.info("Here's a {} variable and an int: {}".format("string", 10))

if __name__ == "__main__":
    main()
