## cf    
#####A Command-Line Interface to Rackspace Cloud Files

It's not beautiful, or amazing, or even spectacular.  But it will will let you upload stuff to Cloud Files hosted in Rackspace.  Simple commands like `cf list all` or `cf put somecontainer file1 file2` don't suck too bad, right?  So far, you can:

* List containers
* List objects in containers
* Create and delete containers
* Delete, upload, and download objects

In the future, I hope it'll also:

* Delete containers w/ objects (override default safetys)
* Make containers public and get URLs
* Shorten CDN URLs for public files
* Enable CDN logging
* Modify CDN TTL vals


## Installation

### With git:

    $ git clone https://github.com/angstwad/cf.git
    $ cd cf/
    $ sudo python ./setup.py install

### With pip or easy_install:

Just kidding.  Not implemented yet.

### Requires
#### python-cloudfiles

The setup.py script will attempt to download and install the *python-cloudfiles* module for you, but if it doesn't, then you'll have to manually install it:
  
`$ sudo pip install python-cloudfiles`    
**OR**    
`$ sudo easy_install python-cloudfiles`

## Usage

On the first run, a config file is tossed into your home folder at `~/.cf`.  Update it with your Rackspace Cloud username and API key, and you're ready to go.

##### List all containers
`$ cf list all`
##### List all items in mycontainer:
`$ cf list mycontainer`
##### Upload some files:
`$ cf put new_container file1 file2`
##### Download some files:
`$ cf get that_old_container pic1.jpg file2.html`    
##### Or put it someplace special with the `-d` flag!    
`$ cf get that_old_container pic1.jpg file2.html -d /home/user`

## Info
 
Requires: python-cloudfiles

Installation of Requisites:  
`$ sudo pip install python-cloudfiles`    
**OR**    
`$ sudo easy_install python-cloudfiles`

**Haven't tested on Windows, and os module includes are not Windows-safe!**

