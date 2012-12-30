# cf -- A CLI to Cloud Files

 *Requires*: python-cloudfiles

 Installation of requires:
   $ sudo pip install python-cloudfiles
       OR
   $ sudo easy_install python-cloudfiles

 BEWARE: Haven't tested on Windows, and os module includes are not Windows-safe!

 Author's Notes: Basic implementation of features: We can get, put, list, and delete stuff.
 There's a lot left to be desired in this prog, but it fills a gap.  I couldn't find a
 CLI to object storage, so I made one.  Numerous features have been left out at this time,
 notably the ability to publish objects and get their URLs. Fixes will come sooner or later.
