#!/usr/bin/env python3
"""
This is a simple utility that takes a time as seconds or milliseconds since the unix epoch (midnight 1970-01-01) and attempts to print it as an ISO-8601 string.

It will attempt to guess whether the number you give it is seconds or milliseconds.
"""

import time
from datetime import timezone, datetime
import argparse
import sys

VERSION = "1.1.0"

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def convertFloat(inputTime):
    try:
        floatTime = float(inputTime)
    except ValueError:
        eprint("Error: Currently only int or float as input is supported")
        sys.exit(1)

    try:
        dt = datetime.fromtimestamp(floatTime, timezone.utc)
        print("%f seconds since epoch is:" % floatTime)
    except ValueError:
        print("%f milliseconds since epoch is:" % floatTime)
        dt = datetime.fromtimestamp(floatTime/1000.0, timezone.utc)
    return dt

def printtime(dt, outputTimeZone):
    print("local time:")
    print(dt.astimezone().isoformat(" "))
    print("UTC time:")
    print(dt.astimezone(timezone.utc).isoformat(" "))

def converttime(inputTime, inputTimeZone, outputTimeZone):
    if inputTime == "now":
      dt = convertFloat(time.time())
    else:
      dt = convertFloat(inputTime)

    printtime(dt, outputTimeZone)

def main():
    parser = argparse.ArgumentParser('Convert unix time to ISO-8601')
    parser.add_argument('time', help='Time in either ms or s since epoch')
    parser.add_argument('-itz', help='Input timezone or offset')
    parser.add_argument('-otz', help='Output timezone or offset')
    parser.add_argument('-v', '--version', action='version',
        version=VERSION, help='Print the version')
    args = parser.parse_args()
    converttime(args.time, args.itz, args.otz)

if __name__ == "__main__":
    main()

