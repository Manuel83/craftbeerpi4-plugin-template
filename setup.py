from setuptools import setup

setup(name='{{ name }}',
      version='0.0.2',
      description='{{ description }}',
      author='{{ author }}'',
      author_email='{{ email }}'',
      url='{{ website }}'',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-ui-plugin': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-ui-plugin'],
     )
