from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='linkedin_scraper',
    version='1.0.0',
    author='Michael Nesterenko',
    description='Scrape public available jobs on Linkedin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mikiui59/linkedin_scraper.git',
    install_requires=[
        'selenium',
        'websocket-client',
        'requests',
        'pandas',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
