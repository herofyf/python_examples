# http://varx.org/wordpress/2016/02/03/bit-fields-in-python/
import struct

# buf is the binary buffer
'''
like "C"
struct
{
 unsigned int x : 4
 unsigned int y : 3
 unsigned int z : 5
 unsigned int c : 20
}

'''

# just like 0x1234
buf = b'1234'

# return tuple result
i, = struct.unpack("<i", buf)

x = i & 0xf  # 4 bits
i = i >> 4
y = i & 0x7  # 3 bits
i = i >> 3
z = i & 0x1f  # 5 bits
i = i >> 5
c = i & 0xfffff # 20 bits
print(x, ",", y, ",", z, ",", c)

# another method
import ctypes

# 其是成员 相邻
class PacketBits(ctypes.LittleEndianStructure):
    # 其是内部attribute
    _fields_ = [
        ("x", ctypes.c_uint32, 4),
        ("y", ctypes.c_uint32, 3),
        ("z", ctypes.c_uint32, 5),
        ("c", ctypes.c_uint32, 20),
    ]

# 下面的成员是一个union结构
class Packet(ctypes.Union):
    _fields_ = [("bits", PacketBits),
                ("binary_data", ctypes.c_uint32)]

packet = Packet()
# 输出到union 一个int成员
packet.binary_data, = struct.unpack("<i", buf)
print(packet.bits.x, ",", packet.bits.y, ",", packet.bits.z, ",", packet.bits.c)