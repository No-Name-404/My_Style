import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="V7xStyle",
    version="2.0",
    author="Example Author",
    author_email="mohammedkainaiahmaed@gmail.com",
    description="Style for (termux & kali) tools...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/No-Name-404/Style",
    packages=['V7xStyle'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    #install_requires=["threading],
)
