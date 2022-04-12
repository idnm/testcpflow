import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='cpflow',
     version='1.0.3',
     author="Nikita Nemkov",
     author_email="nnemkov@gmail.com",
     description="Variational synthesis of quantum circuits.",
     url="https://github.com/idnm/testcpflow",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Topic :: Scientific/Engineering :: Mathematics",
         "Operating System :: OS Independent",
     ],
 )
