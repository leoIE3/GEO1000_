# GEO1000 - Assignment 4
# Authors:
# Studentnumbers:


def get_payload(raw_msg):
    """
    Returns tuple of payload and padding of a given raw AIS message

    For the raw AIS message: 

        !AIVDM,1,1,1,A,13an?n002APDdH0Mb85;8'sn06sd,0*76

    the payload is:

        13an?n002APDdH0Mb85;8'sn06sd

    the padding (the digit before the *) is:

        0

    Returns:
        tuple (payload:str, padding:int)
    """
    payload=str(raw_msg[14:42])
    print payload
    padding=int(raw_msg[45])
    return payload,padding


def read_payloads(filenm):
    """
    Reads the AIS messages (timestamp, payload and padding) from the file

    Arguments:
        :filenm: name of the file to be opened

    Uses:
        get_payload to get the payload and padding from each raw AIS message

    Returns:
        A list with tuples:
        [(timestamp:str, payload:str, padding:int), ...]
    """
    read=[]
    with open(filenm,'r') as fin:
        for line in fin:
            temp=line.strip().split('\t')
            payload,padding=get_payload(temp[1])
            time=temp[0]
            var=time,payload,padding
            read.append(var)
    return read
def _test():
    read_payloads('aislog.txt')


if __name__ == "__main__":
    _test()
