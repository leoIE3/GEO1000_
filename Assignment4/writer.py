# GEO1000 - Assignment 4
# Authors:
# Studentnumbers:

def write_tsv(lst, filenm_out):
    """
    Writes Tab Separated values to a file with name filenm_out

    Arguments:

        lst: list of dictionaries with the message content
             [{'msgtype': 1, ...}, {...}, ...]
        filenm_out: string specifying name of the file to use for output

    """
    #header=lst[0].keys()  
#    with open(filenm_out,'w') as fout:
#        fout.write('timestamp\tmsgtype\trepeat\tmmsi\tstatus\tturn\tspeed\tlon\tlat\tcourse\theading\tsecond\tmaneuver\traim\tradio\n')
#        for item in lst:
#            #print item['status'].keys
#            fout.write('timestamp\t%s\n'%(item['timestamp']))
#            fout.write('msgtype\t%s\n'%(item['msgtype']))
#            fout.write('repeat\t%s\n'%(item['repeat']))
#            fout.write('mmsi\t%s\n'%(item['mmsi']))
#            fout.write('status\t%s\n'%(item['status']))
#            fout.write('turn\t%s\n'%(item['turn']))
#            fout.write('speed\t%s\n'%(item['speed']))
#            fout.write('lon\t%s\n'%(item['lon']))
#            fout.write('lat\t%s\n'%(item['lat']))
#            fout.write('course\t%s\n'%(item['course']))
#            fout.write('heading\t%s\n'%(item['heading']))
#            fout.write('second\t%s\n'%(item['second']))
#            fout.write('maneuver\t%s\n'%(item['maneuver']))
#            fout.write('raim\t%s\n'%(item['raim']))
#            fout.write('radio\t%s\n'%(item['radio']))

    with open(filenm_out,'w') as fout:
        fout.write('timestamp\tmsgtype\trepeat\tmmsi\tstatus\tturn\tspeed\tlon\tlat\tcourse\theading\tsecond\tmaneuver\traim\tradio\n')
        for item in lst:
            #print item['status'].keys
            fout.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(item['timestamp'],item['msgtype'],item['repeat'],item['mmsi'],item['status'],item['turn'],item['speed'],item['lon'],item['lat'],item['course'],item['heading'],item['second'],item['maneuver'],item['raim'],item['radio']))
           
       

def _test():
    A=[{'status': 5, 'maneuver': 0, 'repeat': 0, 'course': 210.8, 'timestamp': '2017-07-21Z00:00:17.986965', 'mmsi': 235115088, 'lon': 4.24844, 'raim': 1, 'turn': -128, 'second': 17, 'msgtype': 1, 'lat': 51.91737, 'radio': 85178, 'speed': 0.0, 'heading': 51.1, 'accuracy': 1}, {'status': 15, 'maneuver': 0, 'repeat': 0, 'course': 289.8, 'timestamp': '2017-07-21Z00:00:21.103635', 'mmsi': 244660375, 'lon': 4.25057, 'raim': 1, 'turn': -128, 'second': 21, 'msgtype': 0, 'lat': 51.91399, 'radio': 50251, 'speed': 0.0, 'heading': 51.1, 'accuracy': 0}, {'status': 15, 'maneuver': 0, 'repeat': 0, 'course': 291.5, 'timestamp': '2017-07-21Z00:00:25.936983', 'mmsi': 244660374, 'lon': 4.25148, 'raim': 1, 'turn': -128, 'second': 26, 'msgtype': 0, 'lat': 51.9137, 'radio': 66505, 'speed': 0.0, 'heading': 51.1, 'accuracy': 0}, {'status': 15, 'maneuver': 0, 'repeat': 0, 'course': 289.0, 'timestamp': '2017-07-21Z00:00:31.094065', 'mmsi': 244660375, 'lon': 4.25058, 'raim': 1, 'turn': -128, 'second': 31, 'msgtype': 0, 'lat': 51.91399, 'radio': 16384, 'speed': 0.0, 'heading': 51.1, 'accuracy': 0}, {'status': 15, 'maneuver': 0, 'repeat': 0, 'course': 291.6, 'timestamp': '2017-07-21Z00:00:35.442177', 'mmsi': 244660374, 'lon': 4.25148, 'raim': 1, 'turn': -128, 'second': 36, 'msgtype': 0, 'lat': 51.9137, 'radio': 50195, 'speed': 0.0, 'heading': 51.1, 'accuracy': 0}, {'status': 0, 'maneuver': 0, 'repeat': 0, 'course': 333.9, 'timestamp': '2017-07-21Z00:00:40.438350', 'mmsi': 235080023, 'lon': 4.24828, 'raim': 0, 'turn': 0, 'second': 39, 'msgtype': 0, 'lat': 51.91725, 'radio': 115255, 'speed': 0.0, 'heading': 3.0, 'accuracy': 0}, {'status': 15, 'maneuver': 0, 'repeat': 0, 'course': 289.2, 'timestamp': '2017-07-21Z00:00:41.338710', 'mmsi': 244660375, 'lon': 4.25058, 'raim': 1, 'turn': -128, 'second': 42, 'msgtype': 0, 'lat': 51.914, 'radio': 16384, 'speed': 0.0, 'heading': 51.1, 'accuracy': 0}]
    write_tsv(A,'output.txt')


if __name__ == "__main__":
    _test()
