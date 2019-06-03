# Info Row
# [id, 'MM-DD-YYYY, h:myy' , 'TT.T, HH.HH, PPPPP'] 



def break_info(info_row):
    id = info_row[0]
    date = info_row[1]
    infos = info_row[2]

    temperature = float(infos[0:4])
    humidity = float(infos[6:11])
    pressure = int(infos[13:18])

    return temperature 
