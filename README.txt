###################
Drupal distribution
###################

This project deals with the directory structure of a Drupal distribution.
It is experimental.

Goals:

* the "project" contains stuff related to the application. It focuses on
  functionality, not on environment or deployment.
* the "project" is intended to be deployed on an environment through a
  distribution.
* the "distribution" focuses on deployment, compatibility and performance on
  a given environment. An environment is composed of hardware, system software,
  external services...

Use cases:

* the "distribution" contains tests on environment setup and compatibility,
  such as the SQL server availability (assert that the SQL configuration
  is ok) or cron jobs.

Synopsys
========

* checkout/download the distribution on your local filesystem
* cd to the distribution root directory
* customize configuration at etc/distribution.conf
* bin/bootstrap => initializes distribution tools, downloads and installs drush
* bin/install =>  deploys the distribution and the project on your system
* source bin/activate => overrides some shell commands (drush, php) so that
  you are sure to use the ones included in the distribution.

TODO
====

* Create a proof-of-concept distribution. Install procedure works.
* Create templates and tools to generate brand new distributions.
