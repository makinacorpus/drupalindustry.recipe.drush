"""Buildout recipes."""

import logging, zc.buildout

from drupal.drush.generator.bin.drush_generator import DrushInstaller


class DrushGeneratorRecipe:
    """Buildout recipe to configure drush script generation in Buildout
    configuration files."""
    def __init__(self, buildout, name, options):
        self.name, self.options = name, options

    def install(self):
        installer = DrushInstaller()
        installer()

    def update(self):
        pass
