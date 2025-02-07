# Copyright (C) 2016-present the asyncpg authors and contributors
# <see AUTHORS file>
#
# This module is part of asyncpg and is released under
# the Apache 2.0 License: http://www.apache.org/licenses/LICENSE-2.0

cimport cython

cdef uuid_bytes_from_str(str u, char *out)
cdef uuid_from_buf(const char *buf)

cdef class __UUIDReplaceMe:
    pass

@cython.final
cdef class UUID(__UUIDReplaceMe):
    cdef:
        char _data[16]
        object _int
        object _hash
        object __weakref__
