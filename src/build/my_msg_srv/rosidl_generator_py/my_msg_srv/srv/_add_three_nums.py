# generated from rosidl_generator_py/resource/_idl.py.em
# with input from my_msg_srv:srv/AddThreeNums.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AddThreeNums_Request(type):
    """Metaclass of message 'AddThreeNums_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_msg_srv')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_msg_srv.srv.AddThreeNums_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__add_three_nums__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__add_three_nums__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__add_three_nums__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__add_three_nums__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__add_three_nums__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AddThreeNums_Request(metaclass=Metaclass_AddThreeNums_Request):
    """Message class 'AddThreeNums_Request'."""

    __slots__ = [
        '_a',
        '_b',
        '_c',
    ]

    _fields_and_field_types = {
        'a': 'double',
        'b': 'double',
        'c': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.a = kwargs.get('a', float())
        self.b = kwargs.get('b', float())
        self.c = kwargs.get('c', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.a != other.a:
            return False
        if self.b != other.b:
            return False
        if self.c != other.c:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def a(self):
        """Message field 'a'."""
        return self._a

    @a.setter
    def a(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'a' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'a' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._a = value

    @builtins.property
    def b(self):
        """Message field 'b'."""
        return self._b

    @b.setter
    def b(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'b' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'b' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._b = value

    @builtins.property
    def c(self):
        """Message field 'c'."""
        return self._c

    @c.setter
    def c(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'c' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'c' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._c = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_AddThreeNums_Response(type):
    """Metaclass of message 'AddThreeNums_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_msg_srv')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_msg_srv.srv.AddThreeNums_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__add_three_nums__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__add_three_nums__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__add_three_nums__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__add_three_nums__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__add_three_nums__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AddThreeNums_Response(metaclass=Metaclass_AddThreeNums_Response):
    """Message class 'AddThreeNums_Response'."""

    __slots__ = [
        '_sum',
    ]

    _fields_and_field_types = {
        'sum': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.sum = kwargs.get('sum', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.sum != other.sum:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property  # noqa: A003
    def sum(self):  # noqa: A003
        """Message field 'sum'."""
        return self._sum

    @sum.setter  # noqa: A003
    def sum(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'sum' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'sum' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._sum = value


class Metaclass_AddThreeNums(type):
    """Metaclass of service 'AddThreeNums'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_msg_srv')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_msg_srv.srv.AddThreeNums')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__add_three_nums

            from my_msg_srv.srv import _add_three_nums
            if _add_three_nums.Metaclass_AddThreeNums_Request._TYPE_SUPPORT is None:
                _add_three_nums.Metaclass_AddThreeNums_Request.__import_type_support__()
            if _add_three_nums.Metaclass_AddThreeNums_Response._TYPE_SUPPORT is None:
                _add_three_nums.Metaclass_AddThreeNums_Response.__import_type_support__()


class AddThreeNums(metaclass=Metaclass_AddThreeNums):
    from my_msg_srv.srv._add_three_nums import AddThreeNums_Request as Request
    from my_msg_srv.srv._add_three_nums import AddThreeNums_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
