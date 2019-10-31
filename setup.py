from setuptools import setup, find_packages

setup(
    name='datatlas', # this is what the user will install
	version='1.0.2',
	packages=find_packages(),
    description='Basic functionality for data science & engineering',
	url="https://github.com/mei-yong/datatlas",
    license='MIT',
	classifiers=[
              "Development Status :: 4 - Beta"
              ,"License :: OSI Approved :: MIT License"
			  ,"Intended Audience :: Developers"
              ,"Programming Language :: Python :: 3"
              ,"Programming Language :: Python :: 3.6"
              ,"Programming Language :: Python :: 3.7"
              ,"Operating System :: OS Independent"
              ],
)
