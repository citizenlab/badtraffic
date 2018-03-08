This folder contains analysis of [OONI](https://ooni.torproject.org/) data in Egypt where we see HTTP 307 responses.

OONI is a project that provides free and open source software for observation of network interference and measurement. It is a project where users run software thats tests the accessibility of URLs and network services.  These results are uploaded back to OONI and shared with the community.  We parsed [OONI measurement files](https://measurements.ooni.torproject.org/) to find all HTTP/307 redirections within Egypt.

Main output here is the ```egypt-307.csv``` which is the result of parsing OONI JSONs from Egypt from 2016-08-01 to 2018-02-01.

* Columns in CSV are:
    * URL - The URL that was tested by an OONI user.
    * DATETIME - Timestamp of when the test was done.
    * OONI_URL - Permalink to the OONI JSON file where this was seen.
    * FIRST307HEADERS - The header of the first response seen.

For more information about analyzing and accessing OONI data [see this post by OONI](https://ooni.torproject.org/post/mining-ooni-data/)