# Benchmark UUID functionality
import os
import statistics
import timeit
import uuid as std_uuid

from cuuid import UUID, randstr_16, uuid4

# Test creation from string
std_uuid_str = str(std_uuid.uuid4())

repeat = 10
n = 100000


def create_std_uuid():
    return std_uuid.UUID(std_uuid_str)


def create_our_uuid():
    return UUID(std_uuid_str)


std_times = timeit.repeat(create_std_uuid, number=n, repeat=repeat)
our_times = timeit.repeat(create_our_uuid, number=n, repeat=repeat)

print("UUID creation from string benchmark:")
print(f"Standard UUID: {statistics.mean(std_times)/n*1e6:.1f} μs per operation")
print(f"Our UUID:     {statistics.mean(our_times)/n*1e6:.1f} μs per operation")
print(
    f"Speedup:      {statistics.mean(std_times)/statistics.mean(our_times):.1f}x\n"
)


# Test uuid4 generation
def std_uuid4_generation():
    return std_uuid.uuid4()


def our_uuid4_generation():
    return uuid4()


std_times = timeit.repeat(std_uuid4_generation, number=n, repeat=repeat)
our_times = timeit.repeat(our_uuid4_generation, number=n, repeat=repeat)

print("UUID4 generation benchmark:")
print(
    f"Standard UUID4: {statistics.mean(std_times)/n*1e6:.1f} μs per operation"
)
print(f"Our UUID4:     {statistics.mean(our_times)/n*1e6:.1f} μs per operation")
print(
    f"Speedup:       {statistics.mean(std_times)/statistics.mean(our_times):.1f}x\n"
)

# Test hex property access
test_uuid = std_uuid.uuid4()
our_uuid = UUID(str(test_uuid))


def std_uuid_hex():
    return test_uuid.hex


def our_uuid_hex():
    return our_uuid.hex


std_times = timeit.repeat(std_uuid_hex, number=n, repeat=repeat)
our_times = timeit.repeat(our_uuid_hex, number=n, repeat=repeat)

print("UUID hex property benchmark:")
print(f"Standard UUID: {statistics.mean(std_times)/n*1e6:.1f} μs per operation")
print(f"Our UUID:     {statistics.mean(our_times)/n*1e6:.1f} μs per operation")
print(
    f"Speedup:      {statistics.mean(std_times)/statistics.mean(our_times):.1f}x\n"
)


# Test int property access
def std_uuid_int():
    return test_uuid.int


def our_uuid_int():
    return our_uuid.int


std_times = timeit.repeat(std_uuid_int, number=n, repeat=repeat)
our_times = timeit.repeat(our_uuid_int, number=n, repeat=repeat)

print("UUID int property benchmark:")
print(f"Standard UUID: {statistics.mean(std_times)/n*1e6:.1f} μs per operation")
print(f"Our UUID:     {statistics.mean(our_times)/n*1e6:.1f} μs per operation")
print(
    f"Speedup:      {statistics.mean(std_times)/statistics.mean(our_times):.1f}x\n"
)


# Test randstr_16 generation
def std_uuid_bytes():
    return os.urandom(16)


def our_randstr_16():
    return randstr_16()


std_times = timeit.repeat(std_uuid_bytes, number=n, repeat=repeat)
our_times = timeit.repeat(our_randstr_16, number=n, repeat=repeat)

print("Random bytes generation benchmark:")
print(f"Standard UUID: {statistics.mean(std_times)/n*1e6:.1f} μs per operation")
print(f"randstr_16:   {statistics.mean(our_times)/n*1e6:.1f} μs per operation")
print(
    f"Speedup:      {statistics.mean(std_times)/statistics.mean(our_times):.1f}x"
)
