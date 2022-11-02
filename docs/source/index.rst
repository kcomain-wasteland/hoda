.. dpextras documentation master file, created by
   sphinx-quickstart on Wed Feb 24 22:22:16 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

HKO Weather (async) API wrapper
=======================================

.. image:: https://readthedocs.org/projects/hwa/badge/?version=latest
    :target: http://hoda.soopy.moe/en/latest/?badge=latest
    :alt: Documentation Status

.. .. image:: https://github.com/kcomain-wasteland/hwa/actions/workflows/codeql-analysis.yml/badge.svg
..     :target: https://github.com/kcomain-wasteland/hwa/actions/workflows/codeql-analysis.yml
..     :alt: CodeQL
.. doesn't actually exist anymore lol

hoda is a wrapper of the Hong Kong Observatory's Open Data API
(`reference <https://www.hko.gov.hk/en/weatherAPI/doc/files/HKO_Open_Data_API_Documentation.pdf>`_)

Currently, this wrapper targets ``v1.7`` of the api, last updated ``May 2022``

Installation
-------------
If you use ``pip``, you can do

.. code:: bash

    $ pip install hoda
    # alternatively, if you want speedups
    # pip install hoda[speedups]

If you use ``poetry`` (recommended)

.. code:: bash

    poetry add hoda
    # alternatively if you want speedups
    # poetry add hoda -E speedups

Extras
~~~~~~~
- ``speedups``: dependencies for speedups
- ``map``: dependencies for map plotting

Guides
-------

.. toctree::
    :maxdepth: 3
    :titlesonly:

    examples/index.rst

Other documents
----------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   reference.rst
   faq.rst

.. toctree::
    :caption: Development
    :hidden:

    Main Repository <https://patchy.soopy.moehoda>
    GitHub Repository <https://github.com/kcomain-wasteland/hoda>

Indices and tables
-------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
