=======================
librarian-notifications
=======================

Provides an API for creating notifications that can be targeted at a single
user, a group of users, or everyone, using either automatic or explicit
expiration, but also with the possibility to make them non-dismissable. Along
with the API, a simple interface is included for viewing and dismissing
notifications.

Installation
------------

The component has the following dependencies:

- librarian-core_

To enable this component, add it to the list of components in librarian_'s
`config.ini` file, e.g.::

    [app]
    +components =
        librarian_notifications

Configuration
-------------

``notifications.default_expiry``
    Notifications that have no explicit expiration specified will be
    automatically deleted if they are older than the here provided value
    (specified in seconds). Example::

        [notifications]
        default_expiry = 86400

Development
-----------

In order to recompile static assets, make sure that compass_ and coffeescript_
are installed on your system. To perform a one-time recompilation, execute::

    make recompile

To enable the filesystem watcher and perform automatic recompilation on changes,
use::

    make watch

.. _librarian: https://github.com/Outernet-Project/librarian
.. _librarian-core: https://github.com/Outernet-Project/librarian-core
.. _compass: http://compass-style.org/
.. _coffeescript: http://coffeescript.org/
