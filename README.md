#### usage: 
`python3 filter_chrome_cache.py --path PATH`

The script returns the source url of every file with cached data from google
chrome. The format is "FILENAME URL" Keep in mind, that the url may have some
trash appended. Suggested usage is grepping the tested domain and reviewing
the cache manually.

#### optional arguments:
-  -h, --help   show this help message and exit
-  --path PATH  usually something like ~/.cache/google-chrome/Profile 1/Cache/
               for chrome
