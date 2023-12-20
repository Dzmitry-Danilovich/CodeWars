def what_time_is_it(angle):
    hour = int(angle//30)
    minut = int(angle%30*2)
    if hour == 0:
        hour = 12
    return "{:02d}".format(hour)+":"+"{:02d}".format(minut)
