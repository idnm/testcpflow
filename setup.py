import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='cpflow',
     version='1.0.2',
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

from setuptools import setup

setup(name='testcpflow',
      packages=['cpflow'],
      version='1.0.1',
      description='Brief Description HERE',
      url='https://github.com/idnm/testcpflow',
      download_url='',  # FILL IN LATER
      author='Nikita Nemkov',
      author_email='nnemkov@gmail.com',
      keywords=['quantum', 'circuits', 'decomposition', 'synthesis'],
      license='MIT',

      install_requires=['pandas', 'numpy', 'jax', 'jaxlib'],

      )
