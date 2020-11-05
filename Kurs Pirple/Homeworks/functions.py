
def artist():
    output = "Kwiat Jabłoni"
    return output

def title():
    output = "Dziś Późno Pójdę Spać"
    return output

def durationInSeconds():
    output = 232
    return output

def isSongLongerThan3Minutes(songDurationInSeconds):
    output = False

    if songDurationInSeconds > 180:
        output = True

    return output

artist()
title()
duration = durationInSeconds()
isItLong = isSongLongerThan3Minutes(duration)
print(isItLong)