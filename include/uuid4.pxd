cdef extern from "include/uuid4.h":
    cdef void c_generate_uuid4(unsigned char* uuid)
