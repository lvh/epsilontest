import setuptools

setuptools.setup(name='epsilontest',
      version='0',
      description='epsilon test',

      author='Laurens Van Houtven',
      author_email='_@lvh.cc',

      packages = setuptools.find_packages(),

      requires=['twisted', 'epsilon', 'axiom'],

      license='ISC',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Twisted",
        "License :: OSI Approved :: ISC License (ISCL)"
        ]
)
