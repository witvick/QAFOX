import os
import logging

class LogGen:
    @staticmethod
    def loggen():
            log_dir = r"C:\Users\MR.WICK\PycharmProjects\QAFOX\Logs"
            # Clear existing handlers
            for handler in logging.root.handlers[:]:
                logging.root.removeHandler(handler)


            logging.basicConfig(
                filename=os.path.join(log_dir, "test_account_reg.log"),
                format='%(asctime)s: %(levelname)s: %(message)s',
                level=logging.DEBUG  # Set to DEBUG to capture all levels
            )

            # Add console handler to see logs in the console too
            #console_handler = logging.StreamHandler()
            #console_handler.setLevel(logging.DEBUG)  # Set to DEBUG
            #formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
            #console_handler.setFormatter(formatter)
            #logging.getLogger().addHandler(console_handler)

            logger = logging.getLogger()
            return logger
