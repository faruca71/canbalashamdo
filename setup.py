from setuptoools import setup

setup(
  name='canbalashamdo',
  version='1.0',
  long_description=__doc__,
  packages=['canbalashamdo',],
  include_package_data=True,
  zip_safe=False,
  install_requires=['Flask'],
  setup_requires['pytest-runner'],
  setup_requires['pytest']
)
