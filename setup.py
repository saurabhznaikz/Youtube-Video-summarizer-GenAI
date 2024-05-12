from setuptools import find_packages,setup

setup(
    name='video-summarizer',
    version='0.0.2',
    author='saurabh naik',
    author_email='naiksaurabhd@gmail.com',
    install_requires=["langchain","streamlit","python-dotenv","PyPDF2","google-generativeai"],
    packages=find_packages()
)