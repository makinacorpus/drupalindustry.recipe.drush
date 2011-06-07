#####################################
Packaged distribution of SimplyDrupal
#####################################

SimplyDrupal is a Drupal project developed by Makina Corpus.
This distribution will help you download and install it on a server.

Quickstart
==========

* Checkout/download the distribution on your local filesystem::

    git clone ssh://bbr@cgit.makina-corpus.net/home/users/bbr/git/drupal-simplydrupal-distribution simplydrupal-distribution

* Place yourself in the the distribution root directory::

    cd simplydrupal-distribution

* Execute bin/bootstrap => initializes distribution tools, such as drush and
  drush make.
* Execute drush make from www/::

    cd www
    ../bin/drush make ../etc/distribution.make -y
    
* Visit the www/install.php file with a browser or execute bin/install
  => configures the distribution and the project on your system

Activate script: extend current shell environment
=================================================

In some cases, you want to isolate the project environment and extend the
default shell environment with the project's one. Source bin/activate for that
purpose.

As an example, your Drupal website has some hook_install and hook_update
implementations that call system commands, such as drush, git or other tools.
Maybe the version that is installed on your system is not the adequate version,
or maybe the program is not installed on your system.
So you want to use the executable located in the distribution's bin/ directory
rather than the one provided by the system. 

Do the following:

* cd to the distribution root directory
* source bin/activate => overrides some shell commands (currently drush) so
  that you are sure to use the ones included in the distribution. Adds the
  distribution's bin/ path to the current PATH.
* work, work, work...
* Execute "deactivate" => restores the environment. Removes distribution's bin/
  from the current PATH.

Configuration
=============

Customize configuration files at distribution's etc/ directory.
Currently, the "bin/build" command uses etc/distribution.make.

Theory
======

Definitions and goals:

* the "project" contains stuff related to the application. It focuses on
  functionality, not on environment or deployment.
* the "project" is intended to be deployed on an "environment" through a
  "distribution".
* the "distribution" focuses on deployment, compatibility and performance on
  a given "environment".
* An "environment" is composed of hardware, system software, external
  services...

Use cases:

* the "distribution" contains tests on environment setup and compatibility,
  such as the SQL server availability (assert that the SQL configuration
  is ok) or cron jobs.
* a continuous integration distribution adds test components to the standard
  profile. A production distribution adds monitoring components. A development
  distribution adds developer tools...
