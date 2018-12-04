py-downloader
=============

Simple Python downloader that downloads files in chunks to try to enable faster and
resumable downloads.

- Resumable download not yet implemented


Usage
-----

    Usage: downloader.py [OPTIONS]

    Options:
      --url TEXT
      --filename TEXT   Filename
      --chunks INTEGER  In how many parallel chunks to download the file.
      --help            Show this message and exit.


Example
-------

    python downloader.py --url 'https://tools.ietf.org/html/rfc7540' --filename something.pdf --chunks 8
