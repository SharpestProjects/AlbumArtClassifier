import tempfile
import tarfile

import wget


def download_dataset(data_url):
	with tempfile.TemporaryDirectory() as tmpdir:
		tmp_path = '{}/data.tar.gz'.format(tmpdir)

		print('Downloading', data_url)
		wget.download(data_url, tmp_path)

		print('Extracting data')
		with tarfile.open(tmp_path) as tar:
			tar.extractall()


if __name__ == '__main__':
	data_url = 'https://album-art-classifier.s3-us-west-2.amazonaws.com/album-art.tar.gz'  # noqa: E501
	download_dataset(data_url)
