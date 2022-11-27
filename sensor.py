import logging, os, pathlib, pigpio, time
import datetime as dt
import DHT22

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s | %(levelname)s | %(funcName)s | %(message)s',
                    handlers=[logging.FileHandler("logging.txt"),
                              logging.StreamHandler()])

fn = dt.datetime.now().strftime("%Y-%m-%d.csv")
fp = os.path.join(pathlib.Path(__file__).parent, "logfiles", fn)

SENSORS = [23, 24]    # GPIO pin numbers of DHT22 sensors 

# create a new logfile if it doesn't exist yet
if not os.path.isfile(fp):
    
    # create a logfile headerline 
    header = "datetime,"
    for sen in SENSORS:
        for label in ("temp", "humi"):
            header += "{}{},".format(label, sen)
    header = header[:-1] + "\n"
    
    with open(fp, "w") as file:
        file.write(header)
        

# prepare new line in logfile
line = dt.datetime.now().strftime("%Y%m%d_%H%M%S")

try: 
    pi = pigpio.pi()
    for sen in SENSORS:
        s = DHT22.sensor(pi, sen)
        s.trigger()   # acquire sensor data
        time.sleep(0.2)
        if s.bad_checksum() or s.short_message() or s.missing_message() or s.sensor_resets():
            logging.warning("Sensor GPIO{} {} {} {} {} {} {} {}".format(sen, 
                s.temperature(), s.humidity(), s.staleness(), s.bad_checksum(), 
                s.short_message(), s.missing_message(), s.sensor_resets()))
        line += ",{:.1f}".format(s.temperature())
        line += ",{:.1f}".format(s.humidity())
        s.cancel()
except Exception as e:
    logging.error(str(e))        
else:
    with open(fp, "a") as file:
        file.write(line+"\n")
# finally:
#     pi.stop()   # pi.stop as proposed in DHT22.main causes exceptions
