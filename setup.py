import setuptools as st

st.setup(
    version = "0.0.0",
    name = "keybits-py",
    description = "A Python library for interacting with Keybits data structures and files.",
    keywords = "keyboard layout editor",
    url = "https://github.com/DamSenViet/keybits-py",
    download_url = "https://github.com/DamSenViet/keybits-py/tarball/0.0.0",
    author = "",
    license = "MIT",
    packages = st.find_packages(exclude=["tests"]),
    install_requires = [],
    extras_require = {
      "tests": ["pytest"],
    },
    python_requires = '>=3.3',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
