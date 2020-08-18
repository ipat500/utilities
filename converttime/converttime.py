#!/usr/bin/env python3
"""
This is a simple utility that takes a time as seconds or milliseconds since the unix epoch (midnight 1970-01-01) and attempts to print it as an ISO-8601 string.

It will attempt to guess whether the number you give it is seconds or milliseconds.
"""

import time
from datetime import timezone, datetime, timedelta
import argparse
import sys

VERSION = "1.2.0"

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
    # print("UTC time:")
    # print(dt.astimezone(timezone(timedelta(hours=7))).isoformat(" "))

def converttime(inputTime, inputTimeZone, outputTimeZone):
    if inputTime == "now":
      dt = convertFloat(time.time())
    else:
      dt = convertFloat(inputTime)

    printtime(dt, outputTimeZone)

def main():
    parser = argparse.ArgumentParser('Convert unix time to ISO-8601')
    parser.add_argument('time', nargs='?', default='now', help='Time as a number in either ms or s since epoch, or "now"')
    parser.add_argument('-itz', '--input-timezone', help='Input timezone or offset (not implemented)')
    parser.add_argument('-otz', '--output-timezone', help='Output timezone or offset (not implemented)')
    parser.add_argument('-v', '--version', action='version',
        version=VERSION, help='Print the version')
    args = parser.parse_args()
    converttime(args.time, args.input_timezone, args.output_timezone)

if __name__ == "__main__":
    main()

