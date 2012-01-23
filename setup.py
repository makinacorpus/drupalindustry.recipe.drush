# coding=utf-8
import os.path
from setuptools import setup, find_packages


def read_relative_file(filename):
    """Returns contents of the given file.
    Filename argument must be relative to this module.
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


version = '0.1'


setup(
    name='drupalindustry.recipe.drush',
    version=version,
    url='https://github.com/makinacorpus/drupalindustry.recipe.drush',
    author='Benoit Bryon',
    author_email='benoit@marmelune.net',
    license='BSD',
    description='Helpers to install drush and generate a "project-specific" ' \
                'drush script. Includes a buildout recipe.',
    long_description=read_relative_file('README.txt'),
    platforms='Any',
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    namespace_packages=['drupalindustry', 'drupalindustry.recipe'],
    include_package_data=True,
    data_files = [('drupalindustry/recipe/drush/templates/', ['drupalindustry/recipe/drush/templates/drush_wrapper.sh'])],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'zc.buildout': [
            'drush_generator = drupalindustry.recipe.drush.buildout:DrushGeneratorRecipe',
        ],
    },
    scripts=[
        'bin/drush_generator.py',
    ],
)
