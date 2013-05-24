tvnplayer
=========

Tiny helper for playing http://tvnplayer.pl/ content in Linux.


Usage
-----

	Usage: tvnplayer [-p COMMAND] [--hd] [URL]

	  -h --help            Show this help
	  -p --player COMMAND  Pass stream URL to player
	  --hd                 Request a high definition stream (if available)

Example
-------

    HTTP_PROXY=127.0.0.1:8080 ./tvnplayer -p mplayer \
        http://tvnplayer.pl/bajki-dla-dzieci-online/popeye-odcinki,731/odcinek-1,krysztalowa-kula,S00E01,12402.html
