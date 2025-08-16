from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Flipkart Chatbot",
    version="0.1",
    author="Rishee",
    packages=find_packages(),
    install_requires = requirements,
)