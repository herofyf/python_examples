class Bf:
    def __init__(self, val):
        self._val = val

    def __iter__(self):
        self._pos = 0
        return self

    def __next__(self):
        pos = self._pos
        curValBitStr = bin(self._val)
        if pos >= len(curValBitStr):
            raise  StopIteration

        bitVal = curValBitStr[pos]
        self._pos += 1
        return bitVal

    def __getitem__(self, index):
        if not isinstance(index, slice):
            return (self._val >> index) & 1
        else:
            return self.__getslice__(index.start, index.stop)

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            self.__setslice__(index.start, index.stop, value)
        else:
            # first to generate mask for index and value
            setBitMask = (1) << index
            setBitValue = (value & 1) << index

            # fist clear and then or the new value
            self._val = (self._val & ~setBitMask) | setBitValue


    def __getslice__(self, start, end):
        # 1.将start位置移动到0，然后再求相应几位mask的值
        mask = 2 ** (end - start + 1) - 1
        shiftForStart = self._val >> start
        return (shiftForStart & mask)

    def __setslice__(self, start, end, value):
        # 先将相应的几位值做清除,
        # 1.先看需要几位mask
        mask = 2 ** (end -start + 1) -1
        # 2.然后移到相应位置
        mask = mask << start

        # 将要设置的值移位
        shiftedVal = value << start

        # clear the bits
        self._val = self._val & mask

        # set the value
        self._val = self._val | value





    def __repr__(self):
        return str(self._val)

k = Bf(8)

klist = [x for x in k]
print(klist)

kstr = ''.join(klist)
# to convert binary
val = int(kstr, 2)
print(val)

k[0] = 1
print(repr(k))

# to set based on slice
k[3:7] = 5
print(k[3])

#k[7] = 1
print(k[2:4])
