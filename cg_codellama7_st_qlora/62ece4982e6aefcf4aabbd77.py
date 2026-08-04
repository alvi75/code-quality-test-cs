def parse_frequency(frequency):
    """
    Given a frequency string with a number and a unit of time, return a corresponding
     datetime.timedelta instance.
     If the frequency is None or "always", return None.
     Raise ValueError if the given frequency cannot be parsed.
     For instance, given "3 timeunit", return datetime.timedelta(timeunit=3)

     @param frequency :  A frequency string "number timeunit"

    @return str, the corresponding datetime
    """
    if frequency is None or frequency == "always":
        return None
    try:
        number, unit = frequency.split()
        number = int(number)
    except ValueError:
        raise ValueError("Invalid frequency: %s" % frequency)
    if unit == "second":
        return timedelta(seconds=number)
    elif unit == "minute":
        return timedelta(minutes=number)
    elif unit == "hour":
        return timedelta(hours=number)
    elif unit == "day":
        return timedelta(days=number)
    elif unit == "week":
        return timedelta(weeks=number)
    elif unit == "month":
        return timedelta(days=number * 30)
    elif unit == "year":
        return timedelta(days=number * 365)
    else:
        raise ValueError("Invalid frequency unit: %s" % unit)