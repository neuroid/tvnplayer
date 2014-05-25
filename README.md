tvnplayer
=========

Tiny helper for playing http://tvnplayer.pl/ content in Linux.


Usage
-----

    Usage: tvnplayer [-o FILE | -p COMMAND] [--hd] [URL]

      -h --help            Show this help
      -o --output FILE     Write stream to FILE; if - is used as FILE,
                           stream will be written to standard output
      -p --player COMMAND  Pass stream URL to player
      --hd                 Request a high definition stream (if available)

    The default action is to print the stream URL to standard output.


Examples
--------

Resolve video stream URL over a proxy and pass it to mplayer:

    HTTP_PROXY=127.0.0.1:8080 ./tvnplayer -p mplayer \
        http://tvnplayer.pl/bajki-dla-dzieci-online/popeye-odcinki,731/odcinek-1,krysztalowa-kula,S00E01,12402.html

Download video stream to a file:

    HTTP_PROXY=127.0.0.1:8080 ./tvnplayer -o popeye.mpeg \
        http://tvnplayer.pl/bajki-dla-dzieci-online/popeye-odcinki,731/odcinek-1,krysztalowa-kula,S00E01,12402.html


Requirements
------------

    pip install docopt
    pip install requests
