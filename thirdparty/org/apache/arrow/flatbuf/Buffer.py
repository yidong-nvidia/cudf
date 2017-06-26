# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers

# /// ----------------------------------------------------------------------
# /// A Buffer represents a single contiguous memory segment
class Buffer(object):
    __slots__ = ['_tab']

    # Buffer
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// The shared memory page id where this buffer is located. Currently this is
# /// not used
    # Buffer
    def Page(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
# /// The relative offset into the shared memory page where the bytes for this
# /// buffer starts
    # Buffer
    def Offset(self): return self._tab.Get(flatbuffers.number_types.Int64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
# /// The absolute length (in bytes) of the memory buffer. The memory is found
# /// from offset (inclusive) to offset + length (non-inclusive).
    # Buffer
    def Length(self): return self._tab.Get(flatbuffers.number_types.Int64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))

def CreateBuffer(builder, page, offset, length):
    builder.Prep(8, 24)
    builder.PrependInt64(length)
    builder.PrependInt64(offset)
    builder.Pad(4)
    builder.PrependInt32(page)
    return builder.Offset()