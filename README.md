tvnplayer
=========

Tiny helper for playing https://player.pl/ content on Linux.


Usage
-----

    Usage: tvnplayer [-o FILE | -p COMMAND] [URL]

      -h --help            Show this help
      -o --output FILE     Write stream to FILE; if - is used as FILE,
                           stream will be written to standard output
      -p --player COMMAND  Pass stream URL to player
      --debug              Show HTTP responses

    The default action is to print the stream URL to standard output.


Examples
--------

Resolve video stream URL over a proxy and pass it to mplayer:

    HTTP_PROXY=127.0.0.1:8080 tvnplayer -p mplayer \
        https://player.pl/programy-online/kuchenne-rewolucje-odcinki,114/odcinek-14,S17E14,95168

Download video stream to a file:

    HTTP_PROXY=127.0.0.1:8080 tvnplayer -o s17e14.mpeg \
        https://player.pl/programy-online/kuchenne-rewolucje-odcinki,114/odcinek-14,S17E14,95168


Installation
------------

    pip install git+https://github.com/neuroid/tvnplayer.git
