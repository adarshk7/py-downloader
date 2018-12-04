import requests

from concurrent.futures import as_completed, ThreadPoolExecutor


__version__ = '0.0.1'


class Downloader():
    def __init__(self, url):
        self.url = url
        self._fetch_download_information()

    def _fetch_download_information(self):
        response = requests.head(self.url)
        file_size = response.headers.get('Content-Length')
        self.file_size = int(file_size) if file_size else None
        self.supports_ranged_download = (
            response.headers.get('Accept-Ranges', 'none') == 'bytes'
        )

    def _download_chunk(self, start, end):
        if end >= self.file_size:
            end = self.file_size - 1
        return requests.get(
            self.url, headers={
                'Range': 'bytes={start}-{end}'.format(start=start, end=end),
            }
        ).content

    def _download_in_chunks(self, chunk_count=8):
        chunk_size = int(self.file_size / chunk_count)
        with ThreadPoolExecutor(max_workers=chunk_count) as executor:
            future_map = {
                executor.submit(
                    self._download_chunk, start, start + chunk_size - 1
                ): start for start in range(0, self.file_size, chunk_size)
            }
        data_chunks = {}
        for future in as_completed(future_map):
            start = future_map[future]
            data_chunks[start] = future.result()
        return data_chunks

    def _build_file_from_chunks(self, chunks, chunk_count=8):
        return b''.join([
            chunks[start] for start in range(
                0, self.file_size, int(self.file_size / chunk_count)
            )
        ])

    def download(self, chunk_count=8):
        if (self.file_size and self.supports_ranged_download):
            return self._build_file_from_chunks(
                self._download_in_chunks(chunk_count=chunk_count)
            )
        return requests.get(self.url).text
