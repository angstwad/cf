## cf    
#####A Command-Line Interface to Rackspace Cloud Files

It's not beautiful, or amazing, or even spectacular.  But it will will let you upload stuff to Cloud Files hosted in Rackspace.  Simple commands like `cf list all` or `cf put somecontainer file1 file2` don't suck too bad, right?  So far, you can:

* List containers
* List objects in containers
* Create and delete containers
* Delete, upload, and download objects

In the future, I hope it'll also:

* Delete containers w/ objects (override default safeties)
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

`$ sudo pip install cf`   
**OR**    
`$ sudo easy_install cf`

### Requires
#### python-cloudfiles

The setup.py script will attempt to download and install the *python-cloudfiles* module for you, but if it doesn't, then you'll have to manually install it:
  
`$ sudo pip install python-cloudfiles`    
**OR**    
`$ sudo easy_install python-cloudfiles`

## Usage

Credentials (username and API key) are supplied three ways:

* Arguments: `$ cf --username <u> --apikey <u>`
* Environment variables: **CF_USER** and **CF_APIKEY**
* Config file at `$HOME/.cf`, created by running `$ cf config --create-config`

Credentials supplied as arguments override a config file or enviroment variables -- in fact, they're prioritized in the order above.  Arguments > envvars > config file.

##### Test your credentials:
    $ cf config --test-login
    >>> Successfully authenticated to Rackspace Cloud Files.
##### List all containers
`$ cf list all`
##### List all items in mycontainer:
`$ cf list mycontainer`
##### Create container: 
`$ cf cont --create someContainer`
##### Delete container:
`$ cf cont [ --delete | -D ] someContainer`
##### Upload some files:
`$ cf put new_container file1 file2`
##### Upload whole dirs:
`$ cf put someContainer ~/Documents/*`
##### Download some files:
`$ cf get that_old_container pic1.jpg file2.html`    
##### Or put it someplace special with the `-d` flag!    
`$ cf get that_old_container pic1.jpg file2.html -d /home/user`
##### Delete remote objects
`$ cf obj someContainer file1 file2`

## Info

* **Be careful:** Files can be overwritten if they have the same name -- there is no overwrite checking in place at this time (version 0.35)
* Haven't tested on Windows.  I don't even have a clue if it'll work for you.

## License

Released under the Apache 2.0 license.


