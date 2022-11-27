import os, pathlib
import datetime as dt

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
    header = header[-1] + "\n"
    
    with open(fp, "w") as file:
        file.write(header)
        
# write new sensor data to the logfile
line = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
line += ",11.0,12.3,67.8,68.0\n"
with open(fp, "a") as file:
    file.write(line)
