import logging
import time
logging.basicConfig(filename="img.png",level=logging.DEBUG)

logger=logging.getLogger()

def read_file_timed(path):
    start_time=time.time()
    try:
        f=open(path,mode="rb")
        data=f.read()
        return data
    except fileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time=time.time()
        dt=stop_time-start_time
        logger.info("time reuired for {file}={time}".format(file=path,time=dt))

data=read_file_timed('img.png')

