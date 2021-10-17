import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "src"
USER_NAME = "pradhami"
USER_EMAIL = "amitpradhands@gmail.com"

setuptools.setup(
    name=f"{PROJECT_NAME}",
    version="0.0.1",
    author=USER_NAME,
    author_email=USER_EMAIL,
    description="A small ackage for ANN Inplementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pradhami/ANN",
    project_urls={
        "Bug Tracker": "https://github.com/pradhami/ANN/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=["src"],
    python_requires=">=3.6",
    install_requires=[
                    'tensorflow',
                    'matplotlib',
                    'seaborn',
                    'numpy',
                    'pandas']
)