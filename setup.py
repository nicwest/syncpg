import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="syncpg",
    version="0.0.1",
    author="nic west",
    author_email="nicwest@mailbox.org",
    description="a syncronous layer on top of asyncpg",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicwest/syncpg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
