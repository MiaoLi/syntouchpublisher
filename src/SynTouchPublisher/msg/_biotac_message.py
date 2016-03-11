"""autogenerated by genpy from SynTouchPublisher/biotac_message.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class biotac_message(genpy.Message):
  _md5sum = "566b08c1093ee950c504ee7154bfb2a5"
  _type = "SynTouchPublisher/biotac_message"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint16[19] E
uint16[22] Pac
uint16 Pdc
uint16 Tac
uint16 Tdc
"""
  __slots__ = ['E','Pac','Pdc','Tac','Tdc']
  _slot_types = ['uint16[19]','uint16[22]','uint16','uint16','uint16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       E,Pac,Pdc,Tac,Tdc

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(biotac_message, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.E is None:
        self.E = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      if self.Pac is None:
        self.Pac = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      if self.Pdc is None:
        self.Pdc = 0
      if self.Tac is None:
        self.Tac = 0
      if self.Tdc is None:
        self.Tdc = 0
    else:
      self.E = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      self.Pac = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      self.Pdc = 0
      self.Tac = 0
      self.Tdc = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_19H.pack(*self.E))
      buff.write(_struct_22H.pack(*self.Pac))
      _x = self
      buff.write(_struct_3H.pack(_x.Pdc, _x.Tac, _x.Tdc))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 38
      self.E = _struct_19H.unpack(str[start:end])
      start = end
      end += 44
      self.Pac = _struct_22H.unpack(str[start:end])
      _x = self
      start = end
      end += 6
      (_x.Pdc, _x.Tac, _x.Tdc,) = _struct_3H.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(self.E.tostring())
      buff.write(self.Pac.tostring())
      _x = self
      buff.write(_struct_3H.pack(_x.Pdc, _x.Tac, _x.Tdc))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 38
      self.E = numpy.frombuffer(str[start:end], dtype=numpy.uint16, count=19)
      start = end
      end += 44
      self.Pac = numpy.frombuffer(str[start:end], dtype=numpy.uint16, count=22)
      _x = self
      start = end
      end += 6
      (_x.Pdc, _x.Tac, _x.Tdc,) = _struct_3H.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3H = struct.Struct("<3H")
_struct_19H = struct.Struct("<19H")
_struct_22H = struct.Struct("<22H")