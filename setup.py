from setuptools import find_packages, setup
setup(
    name="mcqgenrative",
    version="0.0.1",
    author="Dhruvil-11",  # Your name or GitHub username
    author_email="dhruvilchodvadia@gmail.com",  # Your email
    description="A package for generating MCQs",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages(),
)
