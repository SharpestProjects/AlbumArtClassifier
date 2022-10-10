import wget

import tempfile
import tarfile


def download_dataset(data_url):
	with tempfile.TemporaryDirectory() as tmpdir:
		tmp_path = '{}/data.tar.gz'.format(tmpdir)
		print('Downloading', data_url)
		wget.download(data_url, tmp_path)

		print('Extracting', tmp_path)
		with tarfile.open(tmp_path) as tar:

import os

def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(tar)


if __name__ == '__main__':
	data_url = 'https://album-art-classifier.s3-us-west-2.amazonaws.com/album-art.tar.gz'  # noqa: E501
	download_dataset(data_url)
