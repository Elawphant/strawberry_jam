from setuptools import setup, find_packages

setup(
    name="strawberry_jam",
    version="1.0.0",
    description="Codegen django command for strawberry-django for rapid schema boilerplate generation from given models",
    author="Gevorg Hakobyan",
    author_email="gevorg.hakobyan@elawphant.am",
    url="https://github.com/Elawphant/strawberry_jam",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "django>=4.0.0",
        "tqdm>=4.50.0",
        "pytest>=8.2.1",
        "strawberry-graphql-django>=0.44.1",
        # List your dependencies here, e.g.:
        # "requests>=2.25.1",
        # "numpy>=1.21.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
