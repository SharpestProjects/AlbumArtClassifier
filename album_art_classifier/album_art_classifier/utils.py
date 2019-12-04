import os


def count_files_in_dir(dir):
	total = 0
	for root, dirs, files in os.walk(dir):
		total += len(files)
	return total
