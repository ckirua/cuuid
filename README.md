# cuuid

Simple and efficient UUID implementation for Python with C backend.


### License
This project is dual-licensed:

1. The following files are licensed under the Apache 2.0 License as they originate from the [asyncpg](https://github.com/MagicStack/asyncpg) project:
   - `tohex.c`
   - `tohex.h` 
   - `uuid.pyx`

   ```
   Copyright (C) 2016-present the asyncpg authors and contributors
   See AUTHORS file for details
   Licensed under the Apache 2.0 License: http://www.apache.org/licenses/LICENSE-2.0
   ```

2. The remaining files are licensed under the BSD 3-Clause License (see LICENSE file).

### Example of Use

```python
import cuuid

print(cuuid.uuid4())

# or

print(cuuid.randstr_16())

# or

print(cuuid.UUID(random_str))
```


### Installation:

```bash
pip install git+ssh://git@github.com/ckirua/cuuid.git
```
See Makefile for details or run `make` for a list of commands.


### Benchmarks

Run with
```bash
python python -m benchmarks.bench_uuid
```

#### Last results
| **Operation** | Standard UUID | Our UUID | Speedup |
|---------------|--------------|----------|---------|
| **UUID creation from string** | 1.5 μs | 0.2 μs | 6.2x |
| **UUID4 generation** | 3.9 μs | 0.3 μs | 15.3x |
| **UUID hex property** | 0.3 μs | 0.1 μs | 2.6x |
| **UUID int property** | 0.1 μs | 0.1 μs | 0.5x |
| **Random bytes generation** | 1.4 μs | 0.2 μs | 5.7x |
