import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="presspy",
    version="2.0",
    author="BD103",
    author_email="dont@stalk.me",
    description="A Python Compression Software",
    long_description=long_description,  # Keep
    long_description_content_type="text/markdown",
    url="https://github.com/BD103/PressPy",
    packages=setuptools.find_packages(),
    install_requires=["click"],
    entry_points={"console_scripts": ["presspy=presspy.cli:cli"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
    ],
    python_requires=">=3.7",
)
