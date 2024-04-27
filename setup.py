from setuptools import setup

setup(name='lasotuvi',
      version='0.1.2',
      description='An sao tu vi',
      url='https://github.com/doanguyen/lasotuvi',
      author='doanguyen',
      author_email='dungnv2410@gmail.com',
      license='MIT',
      packages=['lasotuvi'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      install_requires=[
          "attrs==17.4.0",
          "ephem==3.7.6.0  ; sys_platform == 'linux'",
          "more-itertools==4.1.0",
          "mypy==1.10.0",
          "pluggy==0.6.0",
          "py==1.10.0",
          "pytest==3.5.0",
          "six==1.11.0",
          "typed-ast==1.5.5"
      ],
      zip_safe=False)
