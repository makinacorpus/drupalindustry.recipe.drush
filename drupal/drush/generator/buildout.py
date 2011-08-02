"""Buildout recipes."""
import os.path
import logging
import zc.buildout

from drupal.drush.generator.generator import DrushInstaller


class DrushGeneratorRecipe:
    """Buildout recipe to configure drush script generation in Buildout
    configuration files."""
    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):
        installer = DrushInstaller()
        bin_directory = self.options.get('bin-directory', self.buildout['buildout'].get('bin-directory'))
        interpreter = self.options.get('interpreter', self.name)
        installer.drush_wrapper = os.path.join(bin_directory, interpreter)
        installer.drush_wrapper = os.path.normpath(installer.drush_wrapper)
        installer()

    def update(self):
        pass
