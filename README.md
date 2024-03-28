# travelog

This is a collection of mobile-based command-line travel location logging tools based on the `termux-location` command. The idea for the first of these scripts came when the author was traveling in remote regions of Mongolia where data connection was unavailable and it was difficult to log the actual location. The [termux](https://termux.dev/en/) program `termux-location` provided a very basic way to obtain basic location information such as latitude, longitude, speed, bearing etc and these can be saved together with short descriptions for re-tracing of the trip later on. 

## Requirements

The scripts here are based on `termux-location`, which requires the installation of [termux](https://termux.dev/en/) and the `termux-location` command-line program. Installation instructions can be found [here](https://termux.dev/en/) and [here](https://wiki.termux.com/wiki/Termux-location). An Android environment is necessary since termux is built only for that environment.

A Python interpreter should be installed as it is required by some scripts here.

## Scripts

### loglocation.sh

This script logs location information using the `termux-location` command. The date/time and user-provided description will be captured together in a json structure and appended to a log file named `location.log` stored in the home directory. When used in the Android environment, location access needs to be enabled. It is important that the description should be enclosed in quotes (") when supplied to this script, for example:

```
$ loglocation.sh "left the national park"
```

Note that location access needs to be turned on for termux. In the event that `termux-location` is unable to provide any output, the script simply logs only the date/time and user-provided description.

### showlocation.py

This Python script runs the `termux-location` command and outputs the latitude, longtitude, altitude, speed and bearing in more human readable form.

Sample output:
```
$ python showlocation.py
Latitude: 1° 21' 45.0" N
Longitude: 113° 57' 55.1" E
Altitude: 18.47 m
Speed: 0.13 m/s, 0.48 km/h
Bearing: 317.99° (NW)
```

Note that location access needs to be turned on for termux. Anomalous data may be output from `termux-location` when the program is run too quickly in succession. Usually waiting some time before trying again should solve the problem. The altitude information usually seems to be wildly inaccurate.

## TODO

The next step would be to ingest the output of `loglocation.sh` and produce some kind of visualization on Google Map or other mapping apps to retrace and present the trip later on.
