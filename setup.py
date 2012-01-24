# coding=utf-8
import os
from setuptools import setup, find_packages


version = '0.1'


def read_relative_file(filename):
    """Returns contents of the given file.
    Filename argument must be relative to this module.
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(name='drupalindustry.recipe.drush',
      version=version,
      description='Helpers to install drush and generate a "project-specific" ' \
                  'drush script. Includes a buildout recipe.',
      long_description=read_relative_file('README.txt'),
      platforms='Any',
      classifiers = [
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          "Programming Language :: Python",
          "Programming Language :: PHP",
      ],
      keywords="drupal deployment deploy install drush",
      author='Benoit Bryon',
      author_email='benoit@marmelune.net',
      url='https://github.com/makinacorpus/drupalindustry.recipe.drush',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'': 'src'},
      namespace_packages=['drupalindustry', 'drupalindustry.recipe'],
      include_package_data=True,
      zip_safe=False,
      data_files = [
          ('bin', ['bin/drush_generator.py']),
          ('src/drupalindustry/recipe/drush/templates/', ['src/drupalindustry/recipe/drush/templates/drush_wrapper.sh'])
      ],
      install_requires=['setuptools', ],
      entry_points=""" # -*- Entry points: -*-
      [zc.buildout]
      drush_generator = drupalindustry.recipe.drush.buildout:DrushGeneratorRecipe
      """,
      scripts=[
          'bin/drush_generator.py',
      ],
      )
