This directory includes all the data related to how we looked at censorship in Turkey and Egypt 
for this report.

We tested the local list of both Turkey and Egypt available on 
the [Citizen Lab Test List repository](https://github.com/citizenlab/test-lists)

We captured packets and ran the [test-censorship.py](test-censorship.py) script against our test lists.  
We then ran the collected packet capture against the [parse-pcap-results.py](parse-pcap-results.py) script to 
get a list of packets that matched the ipid and tcp flag signature.

We then got the list of URLs that were blocked in each country.  

* [blocked-eg.txt](blocked-eg.txt)
* [blocked-tr.txt](blocked-tr.txt)