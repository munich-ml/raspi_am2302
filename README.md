# raspi_am2303
Reads temperature and humidity data from multiple __AM2302__ (DHT22) sensors, scheduled via __cron jobs__ (crontab)

## Adafruit not supported for Pi 4
The common way to read DHTxx / AM23xx temperature sensors is by using the Adafruit driver. Pi 4, however, seems not to be supported by Adafruit. That's why I moved to the alternative driver `pigpio`. 

Background article: https://buyzero.de/blogs/news/tutorial-dht22-dht11-und-am2302-temperatursensor-feuchtigkeitsensor-am-raspberry-pi-anschliessen-und-ansteuern

## pigpio
[pigpio](https://github.com/joan2937/pigpio) (from Raspberry Pi GPIO) can be alternatively be used to read e.g. DHT22 temperature sensors.
The [`DHT22.py`](DHT22.py) module of this project is directly cloned from https://github.com/joan2937/pigpio/blob/master/EXAMPLES/Python/DHT22_AM2302_SENSOR/DHT22.py and imported in my [`sensors.py`](sensor.py) as DHT22 driver.

The pigpio daemon needs to be running in order to use the [`DHT22.py`](DHT22.py) module. The daemon can be started by executing
```bash
sudo pigpiod    # start the pigpio deamon
```
That line can be added to the cronjob (described below) to be executed after boot.

## Periodic execution using crontab
Cron jobs allow periodic execution of commands, scripts and programs. https://de.wikipedia.org/wiki/Cron

```bash
crontab -l     # list existing cron jobs
crontab -e     # edit cron jobs
crontab -r     # remove cron jobs
```

Paste the following script into `crontab -e` in order to execute the `sensors.py` script every 15 minutes.
```bash
# ┌───────────── Minute (0 - 59)
# │ ┌───────────── Stunde (0 - 23)
# │ │ ┌───────────── Tag des Monats (1 - 31)
# │ │ │ ┌───────────── Monat (1 - 12)
# │ │ │ │ ┌───────────── Wochentag (0 - 6)
# │ │ │ │ │

*/15 * * * *  python /home/pi/Desktop/raspi_am2302/sensor.py  # execute every 15 minutes

@reboot sudo pigpiod   # start pigpio deamon after reboot
```