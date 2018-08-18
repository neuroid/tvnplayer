#!/usr/bin/env python
"""Usage: tvnplayer [-o FILE | -p COMMAND] [--debug] [URL]

  -h --help            Show this help
  -o --output FILE     Write stream to FILE; if - is used as FILE,
                       stream will be written to standard output
  -p --player COMMAND  Pass stream URL to player
  --debug              Show HTTP responses

The default action is to print the stream URL to standard output.
"""
from __future__ import print_function
from collections import OrderedDict
import contextlib
import json
import os
import re
import subprocess
import sys

try:
    from urlparse import urlsplit
except ImportError:
    from urllib.parse import urlsplit

from docopt import docopt
import requests

try:
    input = raw_input
except NameError:
    pass

api_url = 'http://api.tvnplayer.pl/api/'

api_params = {
    'authKey': '453198a80ccc99e8485794789292f061',
    'format': 'json',
    'platform': 'ConnectedTV',
    'terminal': 'Samsung2',
    'v': '3.6',
}

api_headers = {
    'User-Agent':
        'Mozilla/5.0 (SmartHub; SMART-TV; U; Linux/SmartTV; Maple2012) '
        'AppleWebKit/534.7 (KHTML, like Gecko) SmartTV Safari/534.7',
}

http_max_retries = 3
http_content_chunk_size = 4096

profiles = ('hd', 'bardzo wysoka', 'wysoka', 'sd', 'standard')
video_id_re = re.compile(r',([0-9]+)$')


def print_status(message):
    print('[tvnplayer] {}'.format(message), file=sys.stderr)


def response_callback(response, *args, **kwargs):
    print_status('[{}|{}] {}'.format(response.request.method.lower(),
                                     response.status_code, response.url))


def assert_response(response, status_code=requests.codes.ok, debug=False):
    if debug:
        headers = json.dumps(dict(response.headers), sort_keys=True, indent=2)
        print_status('[headers]\n' + headers)
        try:
            body = json.dumps(response.json(), sort_keys=True, indent=2)
        except ValueError:
            body = response.text
        print_status('[body]\n' + body)

    if response.status_code != status_code:
        print_status('Request returned {} (expected {})'.format(
                     response.status_code, status_code))
        sys.exit(1)


@contextlib.contextmanager
def open_output(name):
    if name == '-':
        output_file = os.fdopen(sys.stdout.fileno(), 'wb', 0)
    else:
        output_file = open(name, 'wb')
    try:
        yield output_file
    finally:
        if name != '-':
            output_file.close()


def readable_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return '{:.1f} {}'.format(bytes, unit)
        bytes /= 1024.0
    return '{:.1f} TB'.format(bytes)


def main():
    args = docopt(__doc__)

    url = args['URL'] or input('Video URL: ')
    debug = args['--debug']

    match = video_id_re.search(urlsplit(url).path)
    if not match:
        print_status('This URL seems to be invalid...')
        sys.exit(1)

    session = requests.Session()
    session.headers.update(api_headers)
    session.hooks.update({'response': response_callback})
    session.mount('http://',
                  requests.adapters.HTTPAdapter(max_retries=http_max_retries))

    params = {'m': 'getItem', 'id': int(match.group(1))}
    params.update(api_params)

    response = session.get(api_url, params=params)
    assert_response(response, debug=debug)

    video = response.json().get('item')
    if not video:
        print_status('Video not available')
        sys.exit(1)

    streams = video['videos']['main']['video_content']
    if not streams:
        print_status('No video streams available')
        sys.exit(1)

    streams = OrderedDict([(stream['profile_name'].lower(),
                            stream.get('url') or stream['src'])
                           for stream in streams])

    print_status('Found {} video stream(s)'.format(len(streams)))

    for profile in profiles:
        try:
            stream_url = streams[profile]
        except KeyError:
            pass
        else:
            break
    else:
        stream_url = streams.values()[0]

    if stream_url.startswith('http://tvnplayer.pl'):
        response = session.get(stream_url)
        assert_response(response, debug=debug)
        stream_url = response.text

    output = args['--output']
    player = args['--player']

    if output:
        response = session.get(stream_url, stream=True)
        assert_response(response)

        with open_output(output) as output_file:
            size = int(response.headers['content-length'])
            print_status("Downloading {} to '{}'".format(readable_size(size),
                                                         output))

            for chunk in response.iter_content(http_content_chunk_size):
                if not chunk:
                    break
                output_file.write(chunk)
    else:
        response = session.head(stream_url, allow_redirects=True)
        assert_response(response, debug=debug)

        if player:
            print_status("Launching '{}'".format(player))
            subprocess.call([player, response.url])
        else:
            print(response.url)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
