#!/usr/bin/env python
"""Helper to download and install Drush in a project's environment."""

from drupal.drush.generator.generator import DrushInstaller


if __name__ == "__main__":
    installer = DrushInstaller(sys.argv[:])
    installer()
