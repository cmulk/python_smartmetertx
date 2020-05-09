from SmartMeterTX import SmartMeterTX

USER="<<YOUR_USERNAME>>"
PASS="<<YOUR_PASSWORD>>"
ESSID = "<<YOUR_ESSID or list of ESSIDS>>"

tx = SmartMeterTX()

r = tx.login(USER, PASS)

j = tx.get_daily_read(ESSID, "05/05/2020", "05/08/2020")

print(repr(j))