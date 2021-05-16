import pylunar, datetime

# City lati/long in DMS format
TEHRAN_LAT = (35, 41, 21.308)
TEHRAN_LONG = (51,23,22.561)

def get_shape_moon(phase):
    """
    get shape of moon by passing phase

    :phase: current moon phase
    :return: string contain shape of moon
    """ 
    with open('moon.txt', 'r') as file:
        lines = file.readlines()        
        index = [lines.index(line) for line in lines if phase in line][0]
        return ''.join(lines[index-2:index+4])
        
                
     
moon = pylunar.MoonInfo(TEHRAN_LAT, TEHRAN_LONG)
today = datetime.datetime.now()

moon.update((today.year, today.month, today.day, today.hour, today.minute, 0))

# normalize the phase name by removing '_' 
phase = moon.phase_name().replace('_', ' ')

print(get_shape_moon(phase))
