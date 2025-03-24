import setuptools

with open("README.md", "r", encoding = 'utf-8') as f: 
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = 'Kidny_Disease_Classification_DL_Project'
AUTHOR_USER_NAME = 'UsmanAhamed12'
SRC_REPO = 'cnnclassifier'
AUTHOR_EMAIL = 'ahmeduzman432@gmail.com'

setuptools.setup(
    name="cnnclassifier",
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package to classify Kidney Disease",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    
)