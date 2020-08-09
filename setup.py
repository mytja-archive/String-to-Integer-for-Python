import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="String-to-Integer",
    version="1.0",
    author="MyTja Team",
    author_email="mamnju21@gmail.com",
    description="Convert your string to integer",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mytja/String-to-Integer-for-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.3,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    setup_requires=['wheel'],
)
