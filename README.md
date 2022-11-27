# raspi_am2303
Connecting to a AM2302 temperature / humidity sensor

## Periodic execution using crontab
https://de.wikipedia.org/wiki/Cron

```bash
crontab -l     # list existing cron jobs
crontab -e     # edit cron jobs
crontab -r     # remove cron jobs
```


```
┌───────────── Minute (0 - 59)
│ ┌───────────── Stunde (0 - 23)
│ │ ┌───────────── Tag des Monats (1 - 31)
│ │ │ ┌───────────── Monat (1 - 12)
│ │ │ │ ┌───────────── Wochentag (0 - 6)
│ │ │ │ │
/15 * * * *  /Pfad/Programmname
```