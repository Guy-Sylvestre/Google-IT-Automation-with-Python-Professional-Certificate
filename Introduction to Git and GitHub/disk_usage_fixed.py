#!/usr/bin/env python3

import shutil
import sys
def check_disk_usage(disk, min_absolte, min_percent):
	"""Return True if there is enough tree disk space, false otherwise"""
	du = shutil.disk_usage(disk)
	#Calculate the percentage of free space
	percent_free = 100 * du.free / du.total
	#Calculate how many free gigatebyte
	gigatebyte_free = du.free / 2**30
	if percent_free < min_percent or gigatebyte_free < min_absolte:
		return False
	return True

#Chock for at least 2GB and 10% free
if not check_disk_usage("/", 2, 10):
	print("ERREUR: Not enough disk space")
	sys.exit(1)

print("Everything ok")
sys.exit(0)