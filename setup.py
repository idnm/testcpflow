from distutils.core import setup

setup(name='testcpflow',
      packages=['cpflow'],
      version='1.0.0',
      description='Brief Description HERE',
      url='https://github.com/idnm/testcpflow',
      download_url='https://github.com/idnm/testcpflow/archive/refs/tags/1.0.0.tar.gz',  # FILL IN LATER
      author='Nikita Nemkov',
      author_email='nnemkov@gmail.com',
      keywords=['quantum', 'circuits', 'decomposition', 'synthesis'],
      license='MIT',

      install_requires=['pandas', 'numpy', 'jax'],

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Quantum engineers',
          'Topic :: Quantum Computing :: Circuit Synthesis',
          'License :: OSI Approved :: MIT License',  # Your License Here
          'Programming Language :: Python :: 3.8',
      ],
      )
