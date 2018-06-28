# GEO1000 - Assignment 4
# Authors:
# Studentnumbers:

from bitlist import BitList


def as_timestamp_bitlist(lst):
    """
    Transforms a list with:
      [(timestamp0, payload0, padding0), ..., (timestampn, payloadn, paddingn)]
    into a list with:
      [(timestamp0:str, bitlist0:BitList), ...]

    Returns:
        list with tuples
    """
    temp=[]
    for item in lst:
       var=item[0],BitList(item[1])
       temp.append(var) 
    return temp


def as_dicts(lst):
    """
    Transforms a list with:
      [(timestamp0:str, bitlist0:BitList), ...]
    into:
      [{'msgtype': 1, ...}, ...]

    Uses:
      decode_msg_dict, postprocess_msg_dict

    Returns:
        list with dictionaries
    """
    temp=[]
   
    for item in lst:
        timestamp=str(item[0])
        bitlist=item[1]
        temp.append(decode_msg_dict(timestamp,bitlist))
    
    return temp
       

def decode_msg_dict(timestamp, bitlist):
    """
    Decode a BitList instance to a dictionary

    Arguments:
        timestamp: str
        bitlist: BitList instance

    Returns:
        Dictionary with keys/values: timestamp and all fields
        for the position message

    **Note, values of the fields are all (signed or unsigned) integers!**
    """
#    temp=bitlist[4:]
#    msgtype=temp[:6]
#    repeat=temp[6:8]
#    mmsi=temp[8:38]
#    status=temp[38:42]
#    turn=temp[42:50]
#    speed=temp[50:60]
#    accuracy=temp[60]
#    lon=temp[61:89]
#    lat=temp[89:116]
#    course=temp[116:128]
#    heading=temp[128:136]
#    second=temp[137:143]
#    maneuver=temp[143:145]
#    raim=temp[148]
#    radio=temp[149:167]
    
    """"(un)signed integer"""
    #A=ubits.BitList(bitlist,0,5)
    dic={}
    dic['msgtype']=bitlist.ubits(0,6)
    dic['repeat']=bitlist.ubits(6,2)
    dic['mmsi']=bitlist.ubits(8,30)
    dic['status']=bitlist.ubits(38,4)
    dic['turn']=bitlist.sbits(42,8)
    dic['speed']=bitlist.ubits(50,10)
    dic['accuracy']=bitlist.ubits(60,1)
    dic['lon']=bitlist.sbits(61,28)
    dic['lat']=bitlist.sbits(89,27)
    dic['course']=bitlist.ubits(116,12)
    dic['heading']=bitlist.ubits(128,9)
    dic['second']=bitlist.ubits(137,6)
    dic['maneuver']=bitlist.ubits(143,2)
    dic['raim']=bitlist.ubits(148,1)
    dic['radio']=bitlist.ubits(149,19)
    dic['timestamp']=timestamp
    
    postprocess_msg_dict(dic)
    return dic

def postprocess_msg_dict(msg):
    """
    Modifier function, post processes the fields:
        speed, lon, lat, course and heading

    Arguments:
        msg: dict (with all fields + timestamp of position message)

    Uses:
        functions: div10 and geo

    Returns:
        None
    """
#    for item in msg:
#        if item=='speed' or item=='course' or item=='heading':
#            msg[item]=div10(msg[item])
#        if item=='lon' or item=='lat':
#            msg[item]=geo(msg[item])
#            if msg[item]>180 or msg[item]>60:
#                print item
    for item in msg:
        if item=='speed':
            msg[item]=div10(msg[item])
        elif item=='course':
            msg[item]=div10(msg[item])
        elif item=='heading':    
            msg[item]=div10(msg[item])
        elif item=='lon':
            msg[item]=geo(msg[item])
        elif item=='lat':
            msg[item]=geo(msg[item])
    
    return msg        	

def div10(field):
    """
    Divide a field by 10.0
    """
    return field / 10.


def geo(field):
    """
    Divide field by 600000.0 and rounds to 5
    """
    
    return round(field / 600000., 5)


def _test():
    lst=[('2017-07-21Z00:00:17.986965', '33P>BD5P00PCLb<MeAEH??vR2Djr', 0), ('2017-07-21Z00:00:21.103635', '13aDpUwP000CMB<Me9J;Dgvb2<A;', 6), ('2017-07-21Z00:00:25.936983', '13aDpUgP000CMSFMe8fcHwvl2@?9', 7), ('2017-07-21Z00:00:31.094065', '13aDpUwP000CMBBMe9K;Bgvv2400', 7), ('2017-07-21Z00:00:35.442177', '13aDpUgP000CMS>Me8gcI?w82<@C', 6), ('2017-07-21Z00:00:40.438350', '13P<9Eh0000CLWDMeA3=2hu>0L8o', 1), ('2017-07-21Z00:00:41.338710', '13aDpUwP000CMBFMe9KsC?wD2400', 5)]
    A=as_timestamp_bitlist(lst)
    as_dicts(A)

if __name__ == "__main__":
    _test()
