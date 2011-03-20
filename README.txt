##############
Drupal project
##############

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
