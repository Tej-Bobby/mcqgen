from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Bobby Mancha",
    author_email="monsterleader@gmail.com",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langchain-community",
        "langchain-huggingface",
        "transformers",
        "torch",
        "huggingface_hub",
        "sentence-transformers",
        "accelerate",
        "streamlit",
        "python-dotenv",
        "PyPDF2",
        "pandas"
    ]
)