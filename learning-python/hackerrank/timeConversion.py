"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.
"""

def timeConversion(s):
    # Get the period for this time
    period = s[-2:]

    # Remove the period from this time
    time = s[:-2]

    # Split via those colons
    time = list(time.split(':'))

    # If period is AM then just return the time
    # but there is a special case though
    if period == 'AM':
        # Special case for 12, then just change it to 00
        if time[0] == '12':
            time[0] = '00'
        return ':'.join(time)

    # Get the hour part
    hour_part = int(time[0])

    # The starting hour
    start_hour = 12

    # If the hour is already 12 then just return the time
    if hour_part == start_hour:
        return ':'.join(time)

    # The first thingy just add 12 to it
    time[0] = str(hour_part + start_hour)

    return ':'.join(time)

if __name__ == '__main__':


    print(timeConversion('12:05:45AM'))
