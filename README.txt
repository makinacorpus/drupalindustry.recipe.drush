###########################
Drupal deployment bootstrap
###########################
Helpers to deploy Drupal websites
#################################

This project provides 3 tools:

* drush shortcut generator: get a preconfigured drush command that acts on your
  project instance. Basically overrides some drush option such as --root or
  --include.
* bootstrap: runs bin/drush_generator and creates some directories like
  var/tmp or lib/.
* activate: extend your shell's PATH

Quickstart
==========

Let say you want to deploy a Drupal project in /WORKSPACE (obviously, adapt
this value depending on your needs).

* Download this toolchain on your local filesystem:
  ::

    git clone https://benoitbryon@github.com/benoitbryon/drupal-deployment-boostrap.git /WORKSPACE

* Place yourself in the the deployment root directory:
  ::

    cd /WORKSPACE

* Execute bin/bootstrap => initializes distribution tools, such as drush and
  drush make.

* Configure: create an etc/distribution.make and adapt setup the URL your
  Drupal installation profile. You can copy and adapt the
  etc/distribution.make.sample file to etc/distribution.make.

  Notice: make sure that your installation profile has a well-named .make file
  to take advantage of drush make's recursive includes.

* Execute drush make:
  ::

    bin/drush make etc/distribution.make www

  You got a Drupal distribution in the www/ folder.

* Visit the www/install.php file with a browser. You may have to configure
  your server for that purpose. We recommend setting the server's configuration
  in etc/.

bin/drush_generator
===================

Invoke bin/drush_generator to download and install drush.
You can configure some options in a configuration file with the -c option.
An example is given at etc/drush.cfg.sample. You can try it like this:
::

  bin/drush_generator -c etc/drush.cfg.sample

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
* source bin/activate => adds the local bin/ path to the current PATH.
  Currently it overrides drush.
* work, work, work...
* Execute "deactivate" => restores the environment. Removes local bin/
  from the current PATH.
