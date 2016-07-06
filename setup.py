from setuptools import setup

setup(
    name="Bookoholic",
    description="A desktop app for bookoholics",
    long_description=open("README.md").read(),
    version="0.1",
    author="Denitsa Petrova",
    author_email="dkostova93@gmail.com",
    install_requires=['PyQt>=5.2.1'],
    packages=['goodreads'],
    license="GNU",
    keywords="book library goodreads",
    url="https://github.com/DenitsaKostova/Bookoholic"
)