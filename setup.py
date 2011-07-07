from setuptools import setup, find_packages

setup(
    name='drupal.drush.generator',
    version='0.1dev',
    author='Benoit Bryon',
    author_email='benoit@marmelune.net',
    entry_points={
        'zc.buildout': [
            'drush_generator = drupal.drush.generator.buildout:DrushGeneratorRecipe',
        ],
    },
    scripts=[
        'drupal/drush/generator/bin/drush_generator.py',
    ],
    packages=find_packages(),
    namespace_packages=['drupal'],
)
