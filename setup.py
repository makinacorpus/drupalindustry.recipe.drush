# coding=utf-8
import os.path
from setuptools import setup, find_packages


def read_relative_file(filename):
    """Returns contents of the given file.
    Filename argument must be relative to this module.
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name='drupal.drush.generator',
    version='0.1dev',
    url='https://github.com/benoitbryon/drupal-drush-generator',
    author='Benoit Bryon',
    author_email='benoit@marmelune.net',
    license='BSD',
    description='Helpers to install drush and generate a "project-specific" ' \
                'drush script. Includes a buildout recipe.',
    long_description=read_relative_file('README.txt'),
    platforms='Any',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    namespace_packages=['drupal', 'drupal.drush'],
    include_package_data=True,
    data_files = [('etc', ['drupal/drush/generator/templates/drush_wrapper.sh'])],
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'zc.buildout': [
            'drush_generator = drupal.drush.generator.buildout:DrushGeneratorRecipe',
        ],
    },
    scripts=[
        'bin/drush_generator.py',
    ],
)
