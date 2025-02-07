from Cython.Build import cythonize
from setuptools import Extension, find_packages, setup

extensions = [
    Extension(
        "cuuid.*",
        ["cuuid/*.pyx", "cuuid/cuuid4.c"],
        extra_compile_args=["-O2", "-march=native", "-Wno-unused-function"],
    ),
]
setup(
    name="cuuid",
    packages=["cuuid"]
    + [f"cuuid.{pkg}" for pkg in find_packages(where="cuuid")],
    ext_modules=cythonize(
        extensions,
        build_dir="src",
        compiler_directives={
            "language_level": 3,
            "boundscheck": False,
            "wraparound": False,
            "cdivision": True,
            "infer_types": True,
        },
    ),
)
