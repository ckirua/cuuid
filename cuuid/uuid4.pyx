from cpython.bytes cimport PyBytes_FromStringAndSize
from .uuid cimport uuid_from_buf, UUID  # Import UUID type from .pxd file


cdef extern from "../include/uuid4.h":
    void c_uuid4(unsigned char* dest) nogil

cpdef bytes randstr_16():
    cdef:
        unsigned char dest[16]
        bytes result
    with nogil:
        c_uuid4(dest)
    result = PyBytes_FromStringAndSize(<char*>dest, 16)
    return result

cpdef UUID uuid4():
    cdef:
        unsigned char dest[16]
        UUID result
    with nogil:
        c_uuid4(dest)
    result = uuid_from_buf(<const char *>dest)
    return result
