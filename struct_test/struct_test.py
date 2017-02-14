import struct, string
import locale, _functools
def inet_aton(packme):
    """
    Givin a IP address as string of form 123.45.67.90 pack it into 32 bit
    :param packme:
    :return:
    """
    ip_parts = packme.split('.')

    a, b, c, d = map(locale.atoi, ip_parts)
    return struct.pack('BBBB', a, b, c, d)

def inet_ntoa(packed_val):
    a, b, c, d = struct.unpack('BBBB', packed_val)
    un = map(str, (a, b, c, d))
    return _functools.reduce(lambda x, y: x + "." + y, un)

ip = "123.45.67.90"

packed = inet_aton(ip)
print(inet_ntoa(packed))

