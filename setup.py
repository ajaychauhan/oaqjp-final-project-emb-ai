# setup.py
from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.28.0',
    ],
    python_requires='>=3.7',
    description='Watson Emotion Detection API wrapper',
    license='MIT',
)