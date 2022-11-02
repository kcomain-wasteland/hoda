Frequently envisioned questions
================================
*also: frequently questioned answers, faq*

This document contain questions that I think people would ask.

What are the ``Optional`` and ``Union`` types?
--------------------------------------------------
They are helper types essentially. :class:`typing.Optional` means that that method or 
function returns or accepts either the item(s) in ``[]`` s or :data:`None`. 

:class:`typing.Union` means that that method accepts or returns types listed in the ``[]`` s

Example:

.. code:: python

    typing.Union[int, float]
    # or
    Union[float, int]

means one of ``float`` or ``int`` or their subclasses is required.

You can read more about them in the :mod:`typing` docs.

My question isn't documented here!
-----------------------------------
You can contact me on Discord and other methods. Contact methods are listed on `this page <https://soopyc.github.io>`_

This package sucks!
--------------------
I'm sorry.
