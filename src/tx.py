import serial
from utility.some_logger import init_logger

# initialize logger
logger = init_logger(has_stream=True, has_file=True, logger_name='tx')

# open port
port_name = '/dev/pts/XX'
with serial.Serial(port=port_name, baudrate=9600) as ser:
    # write message
    mes = 'Test message from python\n'
    logger.debug(
        'message volume is {} bytes'.format(
            ser.write(
                mes.encode('ascii'))))

logger.debug('---end---')
