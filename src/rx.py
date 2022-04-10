import serial
from utility.some_logger import init_logger

# initialize logger
logger = init_logger(has_stream=True, has_file=True, logger_name='rx')

# open port
port_name = '/dev/pts/XX'
with serial.Serial(port=port_name, baudrate=9600) as ser:
    # read message
    while True:
        try:
            line = ser.readline()
            logger.debug(line.decode('utf-8'))
        except Exception as e:
            logger.exception(e)
            