========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |codecov|
    * - package
      - | |version| |supported-versions| |commits-since|

.. |docs| image:: https://readthedocs.org/projects/data-from-url/badge/?style=flat
    :target: https://data-from-url.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/MaartendeRuyter/data-from-url/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/MaartendeRuyter/data-from-url/actions

.. |codecov| image:: https://codecov.io/gh/MaartendeRuyter/data-from-url/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/MaartendeRuyter/data-from-url

.. |version| image:: https://img.shields.io/pypi/v/data-from-url.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/data-from-url

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/data-from-url.svg
    :alt: Supported versions
    :target: https://pypi.org/project/data-from-url

.. |commits-since| image:: https://img.shields.io/github/commits-since/MaartendeRuyter/data-from-url/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/MaartendeRuyter/data-from-url/compare/v0.0.1...main

.. end-badges

Package to manage data requests to urls

* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

Installation
============

::

    pip install data-from-url

You can also install the in-development version with::

    pip install https://github.com/MaartendeRuyter/data-from-url/archive/main.zip


Documentation
=============


https://data-from-url.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
