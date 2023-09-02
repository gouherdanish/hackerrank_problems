def timeConversion(s):
    """
    Given a time in -hour AM/PM format, convert it to military (24-hour) time.

    Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
    - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
    """
    ampm = s[-2:]
    hours = s[:2]
    minutes = s[3:5]
    seconds = s[6:8]
    if ampm.lower() == 'pm':
        hours = int(hours) if hours == '12' else int(hours) + 12
    if ampm.lower() == 'am':
        hours = int(hours) - 12 if hours == '12' else int(hours)
    return f'{hours:02}:{minutes}:{seconds}'