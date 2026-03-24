from setuptools import setup

setup(name='eirenex',
      version='1.0.4',
      description='EIRENE post-processing package',
      url='',
      author='Nathan Bartlett',
      author_email='bartlettnbb2@gmail.com',
      license='NONE',
      packages=['eirenex'],
      install_requires=[
          'xarray', 'numpy','pandas','netCDF4','imageio','matplotlib','pytest','os' ],
      zip_safe=False)
