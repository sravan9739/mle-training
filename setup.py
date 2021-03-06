import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="housing_price",
    version="0.3",
    author="Sravan kumar M",
    author_email="sravan.maripi@tigeranalytics.com",
    description="Package made for assignment 4.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sravan9739?tab=repositories",
    project_urls={
        "Bug Tracker": "https://github.com/sravan9739?tab=repositories",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
