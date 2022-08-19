Note
=========================
You should consider using `python-minifier <https://github.com/dflook/python-minifier>`_
instead of this package, because there are known issues with this package,
including but not limited to:

* Does NOT working (well) with `class` members
* Does NOT support `f-string`
* Does NOT support annotations parse/remove

pyminifier3
===========

Pyminifier is a Python code minifier, obfuscator, and compressor.

.. note::

    * For the latest, complete documentation: https://pyminifier3.readthedocs.io/
    * For the latest code: https://github.com/dzhuang/pyminifier3


Supported Python Versions
=========================

This package requires Python 3.


Fork
====

This project is a fork of `pyminifier
<https://github.com/liftoff/pyminifier>`_. The original project
appears mostly dead and has a number of outstanding bugs (especially with
installation under Python 3).

Overview
--------
When you install pyminifier it should automatically add a 'pyminifier'
executable to your ``$PATH``.  This executable has a number of command line
arguments:

.. code-block:: sh

    $ pyminifier --help
    Usage: pyminifier [options] "<input file>"

    Options:
    --version             show program's version number and exit
    -h, --help            show this help message and exit
    -o <file path>, --outfile=<file path>
                          Save output to the given file.
    -d <file path>, --destdir=<file path>
                          Save output to the given directory. This option is
                            required when handling multiple files. Defaults to
                            './minified' and will be created if not present.
    --nominify            Don't bother minifying (only used with --pyz).
    --use-tabs            Use tabs for indentation instead of spaces.
    --bzip2               bzip2-compress the result into a self-executing python
                            script.  Only works on stand-alone scripts without
                            implicit imports.
    --gzip                gzip-compress the result into a self-executing python
                            script.  Only works on stand-alone scripts without
                            implicit imports.
    --lzma                lzma-compress the result into a self-executing python
                            script.  Only works on stand-alone scripts without
                            implicit imports.
    --pyz=<name of archive>.pyz
                          zip-compress the result into a self-executing python
                            script. This will create a new file that includes any
                            necessary implicit (local to the script) modules.
                            Will include/process all files given as arguments to
                            pyminifier.py on the command line.
    -O, --obfuscate       Obfuscate all function/method names, variables, and
                            classes.  Default is to NOT obfuscate.
    --obfuscate-classes   Obfuscate class names.
    --obfuscate-functions
                          Obfuscate function and method names.
    --obfuscate-variables
                          Obfuscate variable names.
    --obfuscate-import-methods
                          Obfuscate globally-imported mouled methods (e.g.
                            'Ag=re.compile').
    --obfuscate-builtins  Obfuscate built-ins (i.e. True, False, object,
                            Exception, etc).
    --replacement-length=1
                          The length of the random names that will be used when
                            obfuscating identifiers.
    --nonlatin            Use non-latin (unicode) characters in obfuscation
                            WARNING: This results in some
                            SERIOUSLY hard-to-read code.
    --prepend=<file path>
                          Prepend the text in this file to the top of our
                            output.  e.g. A copyright notice.

For the examples below we'll be minifying, obfuscating, and compressing the
following totally made-up Python script (in repository ``tests/files/tumult.py``).

.. code-block:: python

    #!/usr/bin/env python3
    """
    tumult.py - Because everyone needs a little chaos every now and again.
    """

    try:
        import demiurgic
    except ImportError:
        print("Warning: You're not demiurgic. Actually, I think that's normal.")
    try:
        import mystificate
    except ImportError:
        print("Warning: Dark voodoo may be unreliable.")

    # Globals
    ATLAS = False  # Nothing holds up the world by default


    class Foo(object):
        """
        The Foo class is an abstract flabbergaster that when instantiated
        represents a discrete dextrogyratory inversion of a cattywompus
        octothorp.
        """
        def __init__(self, *args, **kwargs):
            """
            The initialization vector whereby the ineffably obstreperous
            becomes paramount.
            """
            # TODO.  BTW: What happens if we remove that docstring? :)

        def demiurgic_mystificator(self, dactyl):
            """
            A vainglorious implementation of bedizenment.
            """
            inception = demiurgic.palpitation(dactyl)  # Note the imported call
            demarcation = mystificate.dark_voodoo(inception)
            return demarcation

        def test(self, whatever):
            """
            This test method tests the test by testing your patience.
            """
            print(whatever)


    if __name__ == "__main__":
        print("Forming...")
        f = Foo("epicaricacy", "perseverate")
        f.test("Codswallop")


By default pyminifier will perform basic minification and print the resulting
code to stdout:

.. note:: The tumult.py script is 1411 bytes.  Remember that.

Run the following command in your console:

.. code-block:: sh

    $ pyminifier tests/files/tumult.py

We will get:

.. code-block:: python

    #!/usr/bin/env python3
    try:
     import demiurgic
    except ImportError:
     print("Warning: You're not demiurgic. Actually, I think that's normal.")
    try:
     import mystificate
    except ImportError:
     print("Warning: Dark voodoo may be unreliable.")
    ATLAS=False
    class Foo(object):
     def __init__(self,*args,**kwargs):
      pass
     def demiurgic_mystificator(self,dactyl):
      inception=demiurgic.palpitation(dactyl)
      demarcation=mystificate.dark_voodoo(inception)
      return demarcation
     def test(self,whatever):
      print(whatever)
    if __name__=="__main__":
     print("Forming...")
     f=Foo("epicaricacy","perseverate")
     f.test("Codswallop")
    # Created by pyminifier (https://github.com/dzhuang/pyminifier3)

This reduced the size of tumult.py from 1411 bytes to 700 bytes.  Not bad!

Minifying by itself can reduce code size considerably but pyminifier can go
further by obfuscating the code.  What that means is that it will replace the
names of things like variables and functions to the smallest possible size.


Special Sauce
-------------
So let's pretend for a moment that your intentions are not pure; that you
totally want to mess with the people that look at your minified code.  What you
need is the ``--nonlatin`` option...

.. code-block:: python

  #!/usr/bin/env python3
  𐲄=ImportError
  餍=print
  ﴦ=False
  ﲷ=object
  try:
   import demiurgic
  except 𐲄:
   餍("Warning: You're not demiurgic. Actually, I think that's normal.")
  try:
   import mystificate
  except 𐲄:
   餍("Warning: Dark voodoo may be unreliable.")
  ﵛ=ﴦ
  class 𦵄(ﲷ):
   def __init__(self,*args,**kwargs):
    pass
   def 𞡡(self,dactyl):
    ﮉ=demiurgic.palpitation(dactyl)
    ﲽ=mystificate.dark_voodoo(ﮉ)
    return ﲽ
   def 𬇷(self,whatever):
    餍(whatever)
  if __name__=="__main__":
   餍("Forming...")
   𞸉=𦵄("epicaricacy","perseverate")
   𞸉.𬇷("Codswallop")
  # Created by pyminifier (https://github.com/dzhuang/pyminifier3)


Yes, that code actually works, because Python 3 supports coding in languages
that use non-latin character sets.

.. note::

    Most text editors/IDEs will have a hard time with code generated using the
    ``--nonlatin`` option because it will be a random mix of left-to-right
    and right-to-left characters.  Often the result is some code appearing on
    the left of the screen and some code appearing on the right.  This makes it
    *really* hard to figure out things like indentation levels and whatnot!

There's even more ways to mess with people in the
`full documentation <https://pyminifier3.readthedocs.io//>`_
