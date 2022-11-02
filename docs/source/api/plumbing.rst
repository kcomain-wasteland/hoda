Plumbing
=========

This page describes lower level plumbing methods of this library.

This plumbing module is basically a thin wrapper against the opendata API.

.. note:: 
    This module is still in works

.. warning::
    As this is a thin wrapper of the API, dict signatures may not be stable when the API changes.

    You should use the higher level wrappers instead of using this directly, since the function signatures and
    returned values will be at least more consistent than this. If there are features not provided by the higher level
    modules, please file a feature request over at `the main repo. <https://koakuma.soopy.moe/sophie/hoda>`_

Weather
--------

.. automodule:: hoda.plumbing.weather
    :members:

Constants
----------

.. automodule:: hoda.constants
    :members: