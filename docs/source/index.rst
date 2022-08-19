.. pyminifier documentation master file, created by
   sphinx-quickstart on Sat May 24 14:25:46 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyminifier - Minify, obfuscate, and compress Python code
========================================================

.. moduleauthor:: Dan McDougall <daniel.mcdougall@liftoffsoftware.com>

Modules
-------

.. toctree::

    pyminifier.rst
    analyze.rst
    compression.rst
    minification.rst
    obfuscate.rst
    token_utils.rst

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
names of things like variables and functions to the smallest possible size, with:

.. code-block:: sh

    pyminifier --obfuscate tests/files/tumult.py

We will get:

.. code-block:: python

      #!/usr/bin/env python3
      撐=ImportError
      ﬡ=print
      ഭ=False
      �=object
      try:
       import demiurgic
      except 撐:
       ﬡ("Warning: You're not demiurgic. Actually, I think that's normal.")
      try:
       import mystificate
      except 撐:
       ﬡ("Warning: Dark voodoo may be unreliable.")
      ڹ=ഭ
      class �(�):
       def __init__(self,*args,**kwargs):
        pass
       def ߨ(self,dactyl):
        ݘ=demiurgic.palpitation(dactyl)
        �=mystificate.dark_voodoo(ݘ)
        return �
       def �(self,whatever):
        ﬡ(whatever)
      if __name__=="__main__":
       ﬡ("Forming...")
       f=�("epicaricacy","perseverate")
       f.test("Codswallop")
      # Created by pyminifier (https://github.com/dzhuang/pyminifier3)


That's all fine and good but pyminifier can go the extra mile and also
*compress* your code using gzip, bz2, or even lzma using a special container:

.. code-block:: sh

    $ pyminifier --obfuscate --gzip tests/files/tumult.py
    #!/usr/bin/env python3
    import zlib, base64
    exec(zlib.decompress(base64.b64decode('eJx9kb1u1EAUhXs/xcUUcVYrb0EXaQoERMoTIKrRrH13M9nxzOjO9S7u6PhrUlCiKKKjoKAMUsSrIEVCULGPwB2bn9BQ2LJmvnvOPcd37yz6RIul9Qv0W4gDnwZ/r9iff3ipTroYiB8RBSq+vr1QkaznYn/x7rU6Ni6hUJefVVieYcMF03BUgB1HoMXO9rS2T
    YFPG4wMWU+uRaUqHxvy1q+P4EnoDwjBh1sDNdxvuDfODXM4AT61fiNvwwdJOOqMq8vDf726IbFd2cYw/tftoaENbENoQ4DODLBE6D2hs2bpMKt+uXymcriicSYluPn0osoBD0WpxRVobb1lrauEbjWfGVqn+Wy22eWPzECUqQn9cfVxolrT8ODG22+v3qu/KaNx0bJhG3z1CxJm/+b8Wt3KU7eys552rkQgM4Tck
    x/Ryez78+vJbCc14RZptMvZ/xwUNq/vTYdaK1Vq3RnrtS5/d3QszUpHdZ1rgJXK0UuMsgPJ0wzlvIxIKWuJ4sjUjImr8kFo007+Vohy+hM5TN3z')))
    # Created by pyminifier (https://github.com/dzhuang/pyminifier3)


That created a 696 byte file...  Not much saved over basic minification
which producted a 700 byte file.  This is because the input file was so small
to begin with.  There's potential to save a lot more space with larger scripts.
Why the heck would you ever want to use such a strange method of compressing
Python code?  Only one reason:

    * You can still import it from other Python code.

That's an important thing to remember when I reveal **the penultimate form of
compression**:  The ``--pyz`` option.

The ``--pyz`` method of compression uses the zip file container format specified
in PEP 441 (http://legacy.python.org/dev/peps/pep-0441/).  This format is
basically a zip file that also happens to be an executable Python script.
Here's an example of how to use it:

.. code-block:: sh

    $ pyminifier --obfuscate --pyz=/tmp/tumult.pyz /tmp/tumult.py
    /tmp/tumult.py saved as compressed executable zip: tumult.pyz
    The following modules were automatically included (as automagic dependencies):


    Overall size reduction: 61.71% of original size
    $

In this case the resulting file is 838 bytes...  The opposite of space savings!
This is of course due to the *original size* of our test script.  The tumult.py
code is simply too small for the .pyz container format to be effective.

Another important aspect of the .pyz container format is the fact that it
requires all local imports be included in the same container.  For this reason
pyminifier will automatically find locally-imported modules and include them in
the container (more on this below).

To properly demonstrate the effectiveness of each minification, obfuscation,
and compression method we'll minify the pyminifier.py code itself.  Here's the
results:

    ================ =========   ===========
    Method           File Size   % Reduction
    ================ =========   ===========
    pyminifier.py    17987       0%
    minification     8403        53.28%
    plus obfuscation 6699        62.76%
    with gzip        3480        80.65%
    with bz2         3782        78.97%
    with lzma        3572        80.14%
    ================ =========   ===========

.. note::

    The sizes of these files may change over time.  The sizes used here were
    taken at the time this documentation was written.

For the .pyz comparison we'll need to add up the total sum of pyminifier.py
plus all it's sister modules (since it imports them all at some point):

    =============== =====
    File            Bytes
    =============== =====
    analyze.py      12259
    compression.py  11293
    minification.py 18639
    obfuscate.py    26474
    pyminifier.py   17987
    token_utils.py  1175
    =============== =====

The total sum of all files is 87827 bytes.  In order to properly compare the
various output options we'll need to perform the same test we performed above
but for all those files.  To do things like this pyminifier includes the
``--destdir`` option.  It will save all minified/obfuscated/compressed files
to the given directory if you provide more than one (e.g. ``*.py``).  Let's do
that:

Pyminifier can also work on a whole directory of Python scripts:

.. code-block:: sh

    $ pyminifier --destdir=/tmp/minified_pyminifier pyminifier/*.py
    pyminifier/analyze.py (12259) reduced to 7009 bytes (57.17% of original size)
    pyminifier/compression.py (11293) reduced to 4880 bytes (43.21% of original size)
    pyminifier/__init__.py (284) reduced to 193 bytes (67.96% of original size)
    pyminifier/minification.py (18639) reduced to 8586 bytes (46.06% of original size)
    pyminifier/obfuscate.py (26474) reduced to 13582 bytes (51.3% of original size)
    pyminifier/pyminifier.py (17987) reduced to 8439 bytes (46.92% of original size)
    pyminifier/token_utils.py (1175) reduced to 604 bytes (51.4% of original size)
    Overall size reduction: 49.13% of original size
    $ du -hs /tmp/minified_pyminifier/
    64K     /tmp/minified_pyminifier/

Not bad!  Not bad at all--for defaults!

Let's see what we get using some other compression options:

**GZIP**

.. code-block:: sh

    $ rm -rf /tmp/minified_pyminifier # Clean up after ourselves first
    $ pyminifier --destdir=/tmp/minified_pyminifier --gzip pyminifier/*.py
    pyminifier/analyze.py (12259) reduced to 2773 bytes (22.62% of original size)
    pyminifier/compression.py (11293) reduced to 2165 bytes (19.17% of original size)
    pyminifier/__init__.py (284) reduced to 289 bytes (101.76% of original size)
    pyminifier/minification.py (18639) reduced to 2829 bytes (15.18% of original size)
    pyminifier/obfuscate.py (26474) reduced to 3924 bytes (14.82% of original size)
    pyminifier/pyminifier.py (17987) reduced to 3652 bytes (20.3% of original size)
    pyminifier/token_utils.py (1175) reduced to 497 bytes (42.3% of original size)
    Overall size reduction: 18.31% of original size

**BZIP2**

.. code-block:: sh

    $ rm -rf /tmp/minified_pyminifier # Clean up after ourselves first
    $ pyminifier --destdir=/tmp/minified_pyminifier --bzip2 pyminifier/*.py
    pyminifier/analyze.py (12259) reduced to 2951 bytes (24.07% of original size)
    pyminifier/compression.py (11293) reduced to 2435 bytes (21.56% of original size)
    pyminifier/__init__.py (284) reduced to 327 bytes (115.14% of original size)
    pyminifier/minification.py (18639) reduced to 2995 bytes (16.07% of original size)
    pyminifier/obfuscate.py (26474) reduced to 3986 bytes (15.06% of original size)
    pyminifier/pyminifier.py (17987) reduced to 3926 bytes (21.83% of original size)
    pyminifier/token_utils.py (1175) reduced to 555 bytes (47.23% of original size)
    Overall size reduction: 19.49% of original size

.. note::

    To self:  Wow, bzip2 kinda sucks in comparsion.  Why do we need it again?

**LZMA**

.. code-block:: sh

    $ rm -rf /tmp/minified_pyminifier # Clean up after ourselves first
    $ pyminifier --destdir=/tmp/minified_pyminifier --lzma pyminifier/*.py
    pyminifier/analyze.py (12259) reduced to 2801 bytes (22.85% of original size)
    pyminifier/compression.py (11293) reduced to 2273 bytes (20.13% of original size)
    pyminifier/__init__.py (284) reduced to 361 bytes (127.11% of original size)
    pyminifier/minification.py (18639) reduced to 2881 bytes (15.46% of original size)
    pyminifier/obfuscate.py (26474) reduced to 3904 bytes (14.75% of original size)
    pyminifier/pyminifier.py (17987) reduced to 3720 bytes (20.68% of original size)
    pyminifier/token_utils.py (1175) reduced to 601 bytes (51.15% of original size)
    Overall size reduction: 18.77% of original size

Now let's try that .pyz container format.  It can't be that much better, right?
WRONG:

.. code-block:: sh

    $ pyminifier --pyz=/tmp/pyminifier.pyz pyminifier.py
    pyminifier.py saved as compressed executable zip: /tmp/pyminifier.pyz
    The following modules were automatically included (as automagic dependencies):

            obfuscate.py
            minification.py
            token_utils.py
            compression.py
            analyze.py

    Overall size reduction: 16.64% of original size
    $ # NOTE: Resulting file is 14617 bytes

Now that's some space-savings!  But does it actually work?  Let's test out that
pyminifier.pyz by re-minifying tumult.py...

.. note:: Remember, the more code there is the more space will be saved.

.. code-block:: sh

    $ /tmp/pyminifier.pyz /tmp/tumult.py
    #!/usr/bin/env python
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
    # Created by pyminifier.py (https://github.com/liftoff/pyminifier)

It works!

Special Sauce
-------------
So let's pretend for a moment that your intentions are not pure; that you
totally want to mess with the people that look at your minified code.  What you
need is Python 3 and the ``--nonlatin`` option...

.. code-block:: sh

    #!/usr/bin/env python3
    ﵛ=ImportError
    ࡅ=print
    㮀=False
    搓=object
    try:
     import demiurgic
    except ﵛ:
    ࡅ("Warning: You're not demiurgic. Actually, I think that's normal.")
    try:
     import mystificate
    except ﵛ:
    ࡅ("Warning: Dark voodoo may be unreliable.")
    ﵩ=㮀
    class רּ(搓):
     def __init__(self,*args,**kwargs):
      pass
     def 𐨱(self,dactyl):
      ﱲ=demiurgic.palpitation(dactyl)
      ꁁ=mystificate.dark_voodoo(ﱲ)
      return ꁁ
     def 𨠅(self,whatever):
      ࡅ(whatever)
    if __name__=="__main__":
     ࡅ("Forming...")
     녂=רּ("epicaricacy","perseverate")
     녂.𨠅("Codswallop")
    # Created by pyminifier.py (https://github.com/liftoff/pyminifier)

Yes, that code actually works *but only using Python 3*.  This is because Python
3 supports coding in languages that use non-latin character sets.

.. note::

    Most text editors/IDEs will have a hard time with code generated using the
    ``--nonlatin`` option because it will be a random mix of left-to-right
    and right-to-left characters.  Often the result is some code appearing on
    the left of the screen and some code appearing on the right.  This makes it
    *really* hard to figure out things like indentation levels and whatnot!

Let's have some more fun by using the ``--replacement-length`` option.  It tells
pyminifier to use name replacements of the given size.  So instead of trying to
minimize the amount of characters used for replacements let's make them HUGE:

.. code-block:: sh

    $ pyminifier --nonlatin --replacement-length=50 /tmp/tumult.py
    #!/usr/bin/env python3
    ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲמּ=ImportError
    ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ燱=print
    ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ巡=False
    ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ澨=object
    try:
     import demiurgic
    except ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲמּ:
     ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ燱("Warning: You're not demiurgic. Actually, I think that's normal.")
    try:
     import mystificate
    except ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲמּ:
     ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ燱("Warning: Dark voodoo may be unreliable.")
    ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲﺬ=ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ巡
    class ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ𐦚(ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ澨):
     def __init__(self,*args,**kwargs):
      pass
     def ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ클(self,dactyl):
      ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ퐐=demiurgic.palpitation(dactyl)
      ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ𠛲=mystificate.dark_voodoo(ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ퐐)
      return ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ𠛲
     def ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ𐠯(self,whatever):
      ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ燱(whatever)
    if __name__=="__main__":
     ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ燱("Forming...")
     ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲﺃ=ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ𐦚("epicaricacy","perseverate")
     ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲﺃ.ﺭ异𞸐𐤔ﭞﰣﺁں𝕌𨿩𞸇뻛𐬑𥰫嬭ﱌ𢽁𐡆𧪮Ꝫﴹ뙫𢤴퉊ﳦﲣפּܟﺶ𐐤ﶨࠔ𐰷𢡶𧐎𐭈𞸏𢢘𦘼ﶻ𩏃𦽨𞺎𠛘𐠲䉊ﰸﭳᣲ𐠯("Codswallop")
    # Created by pyminifier (https://github.com/liftoff/pyminifier)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

