# Affiliates

This folder contains an extract of information collected from the [Internet Archive WayBack Machine](https://archive.org/web/)

Archived versions of pages were downloaded using the [wayback-machine-scraper](https://github.com/sangaline/wayback-machine-scraper)
written by Evan Sangaline.

Contains three CSV files:

### 01-internetarchive-domain-to-forwarded.csv

This is the initial extraction of the forwarded to locations of domains.

Schema is as follows:

* initial domain - The domain that was requested from wayback, either domain or domain plus /*
* forwarded url - The URL that we were forwarded to, through JS redirection.
* snapshotname - The wayback snapshot name
* snapshot_date - The date of the wayback snapshot.

### 02-internetarchive-unique-urls.csv

We iterated on the above data file to get a list of affiliate ids.

* forwarded url - the Url we were forwarded to
* has a unique id? - Boolean if we see anything that might be an affiliate id
* Id - What we determine to be an affiliate id
* Domain - FQDN of the forwared url.
* Pairing domain to Affiliate ID - pairing of domain to id

### 03-final-pairing-domain-to-affiliate-id.txt

Final list of domains mapped to affiliate ids.  

The other additions to the final table were items that were previously reported in the OONI report or which 
we manually visited.

For example for the Coinhive URL: http://cnhv[ . ]co/fmwi  This was because the domain http://ads[ . ]vidz4fun[ . ]com/vad1.html
which we see in the OONI data forwards to this, but wayback machine did not retain this snapshot.  The details of this
redirect can be seen in ```coinhive-redir.txt```