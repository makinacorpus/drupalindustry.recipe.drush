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
        # Configure drush interpreter
        bin_directory = self.options.get('bin-directory', self.buildout['buildout'].get('bin-directory'))
        interpreter = self.options.get('interpreter', self.name)
        installer.drush_wrapper = os.path.join(bin_directory, interpreter)
        installer.drush_wrapper = os.path.normpath(installer.drush_wrapper)
        # Configure base_dir
        base_dir = self.options.get('directory', self.buildout['buildout'].get('directory'))
        installer.base_dir = os.path.normpath(base_dir)
        # Drush URL
        drush_url = self.options.get('url', None)
        if drush_url:
            installer.drush_url = drush_url
        # Drush commands
        drush_commands = self.options.get('commands', None)
        if drush_commands:
            installer.drush_commands = drush_commands
        # Path to PHP
        php = self.options.get('php', None)
        if php:
            installer.php = php
        # Drupal root
        drupal_root = os.path.join(base_dir, 'www')
        drupal_root = self.options.get('drupal-root', drupal_root)
        installer.www_dir = drupal_root
        # Drupal URI
        drupal_uri = self.options.get('drupal-uri', '')
        installer.drupal_uri = drupal_uri
        # Run installer
        installer()

    def update(self):
        pass
