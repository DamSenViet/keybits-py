import setuptools as st

st.setup(
    version = "0.0.0",
    name = "key-labs-py",
    description = "A Python library for interacting with Key Labs data structures and files.",
    keywords = "keyboard layout editor serial",
    url = "https://github.com/DamSenViet/kle-labs-py",
    download_url = "https://github.com/DamSenViet/key-labs-py/tarball/0.0.0",
    author = "",
    license = "MIT",
    packages = st.find_packages(exclude=["tests"]),
    install_requires = [],
    python_requires = '>=3.3',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)