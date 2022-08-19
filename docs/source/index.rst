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



That's all fine and good but pyminifier can go the extra mile and also
*compress* your code using gzip, bz2, or even lzma using a special container:

.. code-block:: sh

      $ pyminifier --obfuscate --gzip tests/files/tumult.py
      #!/usr/bin/env python3
      import zlib, base64
      exec(zlib.decompress(base64.b64decode('eJx1kT1vwjAQhnf/iqs7EFAUhm5IHqpSEDNIiMlykgu4OLZ1doD8+zpJ1Y+hgy3b99y9752fn5ZdoGWp7RLtDXwfL86+sJPYtd5RfCdyxA7Ck7aRHcVGmYBsK1z5gVVkkfoVAz2iUGOrOzrriuGjQh/hlGKHjB8VWW3PKzi5bkYI1v1iC3itYqeM6XPYQbxoe
      027irOQOGqVKfj8r0zbh6gbXamI/wmtFV3h5lztHLSqhxKhs4RGq9LgUHAtjqwyKgRosu08ZdfYgJTa6ihlFtA0+ULROeSLxfU+HAYGfEqY0M3E1KqKvRljD/HTklfG66iidjb7QhLhxC/nRZ0sysli9hjChLEjC24S2E8C9zQJvCGNEofs+8r0YNeqFqUUgkvZKm2l5NMcNmlwaQ5FMbQKjWgyjj7JUlpVz3Puk
      cJQJ1UbiWKf8TdXh3v6B+fT0ycIYrFK')))
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
and compression method we'll minify the pyminifier `__init__.py` code itself.  Here's the
results:

    ================ =========   ===========
    Method           File Size   % Reduction
    ================ =========   ===========
    \_\_init\_\_.py    15818       0%
    minification     10108       35.77%
    plus obfuscation 8692        44.89%
    with gzip        4804        69.40%
    with bzip2       4986        68.30%
    with lzma        4844        69.17%
    ================ =========   ===========

.. note::

    The sizes of these files may change over time.  The sizes used here were
    taken at the time this documentation was written.

For the .pyz comparison we'll need to add up the total sum of pyminifier `__init__.py`
plus all it's sister modules (since it imports them all at some point):

    =============== =====
    File            Bytes
    =============== =====
    analyze.py      12942
    compression.py  11564
    minification.py 15016
    obfuscate.py    31757
    \_\_main\_\_.py   6402
    token_utils.py  1283
    =============== =====

The total sum of all files is 94739 bytes.  In order to properly compare the
various output options we'll need to perform the same test we performed above
but for all those files.  To do things like this pyminifier includes the
``--destdir`` option.  It will save all minified/obfuscated/compressed files
to the given directory if you provide more than one (e.g. ``*.py``).  Let's do
that:

Pyminifier can also work on a whole directory of Python scripts:

.. code-block:: sh

      $ pyminifier --destdir=/tmp/minified_pyminifier pyminifier/*.py
      pyminifier\analyze.py (12942) reduced to 7378 bytes (57.01% of original size)
      pyminifier\compression.py (11564) reduced to 6406 bytes (55.4% of original size)
      pyminifier\minification.py (15016) reduced to 6887 bytes (45.86% of original size)
      pyminifier\obfuscate.py (31757) reduced to 16309 bytes (51.36% of original size)
      pyminifier\token_utils.py (1283) reduced to 724 bytes (56.43% of original size)
      pyminifier\__init__.py (15818) reduced to 10185 bytes (64.39% of original size)
      pyminifier\__main__.py (6402) reduced to 4551 bytes (71.09% of original size)
      Overall size reduction: 55.33% of original size

      $ du -hs /tmp/minified_pyminifier/
      64K     /tmp/minified_pyminifier/

Not bad!  Not bad at all--for defaults!

Let's see what we get using some other compression options:

**GZIP**

.. code-block:: sh

      $ rm -rf /tmp/minified_pyminifier # Clean up after ourselves first
      $ pyminifier --destdir=/tmp/minified_pyminifier --gzip pyminifier/*.py
      pyminifier\analyze.py (12942) reduced to 2828 bytes (21.85% of original size)
      pyminifier\compression.py (11564) reduced to 2668 bytes (23.07% of original size)
      pyminifier\minification.py (15016) reduced to 2404 bytes (16.01% of original size)
      pyminifier\obfuscate.py (31757) reduced to 4400 bytes (13.86% of original size)
      pyminifier\token_utils.py (1283) reduced to 572 bytes (44.58% of original size)
      pyminifier\__init__.py (15818) reduced to 4844 bytes (30.62% of original size)
      pyminifier\__main__.py (6402) reduced to 2140 bytes (33.43% of original size)
      Overall size reduction: 20.95% of original size


**BZIP2**

.. code-block:: sh

      $ rm -rf /tmp/minified_pyminifier # Clean up after ourselves first
      $ pyminifier --destdir=/tmp/minified_pyminifier --bzip2 pyminifier/*.py
      pyminifier\analyze.py (12942) reduced to 3010 bytes (23.26% of original size)
      pyminifier\compression.py (11521) reduced to 2958 bytes (25.67% of original size)
      pyminifier\minification.py (15016) reduced to 2570 bytes (17.12% of original size)
      pyminifier\obfuscate.py (31757) reduced to 4486 bytes (14.13% of original size)
      pyminifier\token_utils.py (1283) reduced to 638 bytes (49.73% of original size)
      pyminifier\__init__.py (15818) reduced to 5018 bytes (31.72% of original size)
      pyminifier\__main__.py (6402) reduced to 2318 bytes (36.21% of original size)
      Overall size reduction: 22.16% of original size


.. note::

    To self:  Wow, bzip2 kinda sucks in comparsion.  Why do we need it again?

**LZMA**

.. code-block:: sh

      $ rm -rf /tmp/minified_pyminifier # Clean up after ourselves first
      $ pyminifier --destdir=/tmp/minified_pyminifier --lzma pyminifier/*.py
      pyminifier\analyze.py (12942) reduced to 2848 bytes (22.01% of original size)
      pyminifier\compression.py (11564) reduced to 2772 bytes (23.97% of original size)
      pyminifier\minification.py (15016) reduced to 2480 bytes (16.52% of original size)
      pyminifier\obfuscate.py (31757) reduced to 4340 bytes (13.67% of original size)
      pyminifier\token_utils.py (1283) reduced to 688 bytes (53.62% of original size)
      pyminifier\__init__.py (15818) reduced to 4880 bytes (30.85% of original size)
      pyminifier\__main__.py (6402) reduced to 2272 bytes (35.49% of original size)
      Overall size reduction: 21.4% of original size


.. warning::

The pyz example does not work.


Now let's try that .pyz container format.  It can't be that much better, right?
WRONG:

.. code-block:: sh

      $ pyminifier --pyz=/tmp/pyminifier.pyz pyminifier/__main__.py
      pyminifier/__main__.py saved as compressed executable zip: /tmp/pyminifier.pyz
      The following modules were automatically included (as automagic dependencies):

              analyze.py
              compression.py
              minification.py
              obfuscate.py
              token_utils.py
              \_\_init\_\_.py

      Overall size reduction: 17.85% of original size
      $ # NOTE: Resulting file is 16911 bytes

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

      $ pyminifier --nonlatin --replacement-length=50 tests/files/tumult.py
      #!/usr/bin/env python3
      #!/usr/bin/env python3
      𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𨿱=ImportError
      𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𞸀=print
      𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𔘮=False
      𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𡓈=object
      try:
       import demiurgic
      except 𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𨿱:
       𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𞸀("Warning: You're not demiurgic. Actually, I think that's normal.")
      try:
       import mystificate
      except 𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𨿱:
       𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𞸀("Warning: Dark voodoo may be unreliable.")
      𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙ﭺ=𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𔘮
      class 𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙ﭛ(𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𡓈):
       def __init__(self,*args,**kwargs):
        pass
       def 𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𐳈(self,dactyl):
        𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𡹯=demiurgic.palpitation(dactyl)
        𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙籷=mystificate.dark_voodoo(𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𡹯)
        return 𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙籷
       def 𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𐬤(self,whatever):
        𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𞸀(whatever)
      if __name__=="__main__":
       𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𞸀("Forming...")
       𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙ﰭ=𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙ﭛ("epicaricacy","perseverate")
       𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙ﰭ.𐤈𧤐앣油𐬮𤋝ﶺ𦳾𬿔𞡃𐳨ٷ뇂噣𓌸𞤟唺얓𐡀ტ𭰩𞸂礷𪪈ᝪ𨟍𤧜ﺥ𐫆ڽดﭪ𤟨侐𤌹𨇜𨎺𐦐ﶣ𠫖𣹁ﱰඟ硖𫒓𠿩ڍ䍝𞸙𐬤("Codswallop")
      # Created by pyminifier (https://github.com/dzhuang/pyminifier3)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

