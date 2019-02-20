SLY35
=====

This is a Python 3.5 compatible fork of
`David Beazley's sly <https://github.com/dabeaz/sly>`_.
To install it, make sure you have git and pip, and then run this:

$ python3.5 -m pip install git+https://github.com/Akuli/sly35

If you want me to upload this thing to PyPI so that you can do
``pip install sly35`` or something, let me know by creating an issue on
GitHub.


How does it work?
-----------------

The only Python 3.6 only features that sly uses seem to be f-strings and
dicts that are ordered by default. I forked dabeaz's repo, ran
`f2format <https://pypi.org/project/f2format/>`_ on it and changed all
dicts to ``collections.OrderedDict``.
