import os, pathlib, pigpio, time
import datetime as dt
import DHT22

fn = dt.datetime.now().strftime("%Y-%m-%d.csv")
fp = os.path.join(pathlib.Path(__file__).parent, "logfiles", fn)

SENSORS = [23, 24]    # GPIO pin numbers of DHT22 sensors 

# create a new logfile if it doesn't exist yet
if not os.path.isfile(fp):
    
    # create a logfile headerline 
    header = "datetime,"
    for label in ("temp", "humi"):
        for sen in SENSORS:
            header += "{}{},".format(label, sen)
    header = header[:-1] + "\n"
    
    with open(fp, "w") as file:
        file.write(header)
        
# acquire sensor data
pi = pigpio.pi()
s = DHT22.sensor(pi, 23)

s.trigger()

time.sleep(0.2)

#print("{} {} {} {:3.2f} {} {} {} {}".format(
#    r, s.humidity(), s.temperature(), s.staleness(),
#    s.bad_checksum(), s.short_message(), s.missing_message(),
#    s.sensor_resets()))

s.cancel()
pi.stop()
        
# write new sensor data to the logfile
line = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
line += ",{:.1f},xxx,{:.1f},xxx\n".format(s.temperature(), s.humidity())
with open(fp, "a") as file:
    file.write(line)
