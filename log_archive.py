#!/usr/bin/env python3
import os
import tarfile
import sys
from datetime import datetime

def archive_logs(log_dir):
	# memastikan directory ada
	if not os.path.isdir(log_dir):
		print(f"Error: {log_dir} tidak ditemukan atau bukan directory. ")
		sys.exit(1)

	# buat direktori tujuan arsip
	archive_dir = os.path.expanduser("~/log_archives")
	os.makedirs(archive_dir, exist_ok=True)

	# nama file arsip berdasarkan waktu sekarang
	timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
	archive_name = f"logs_archive_{timestamp}.tar.gz"
	archive_path = os.path.join(archive_dir, archive_name)

	# compress process
	with tarfile.open(archive_path, "w:gz") as tar:
		tar.add(log_dir, arcname=os.path.basename(log_dir))

	# catat ke log aktivitas
	log_file = os.path.join(archive_dir, "archive_history.log")
	with open(log_file, "a") as f:
		f.write(f"{datetime.now()} - Archived {log_dir} -> {archive_path}\n")

	print(f" Arsip Selesai : {archive_path}")
	print(f" Riwayat disimpan di: {log_file}")

def main():
	if len(sys.argv) !=2:
		print("Usage: log-archive <log-directory>")
		sys.exit(1)

	log_dir = sys.argv[1]
	archive_logs(log_dir)

if __name__== "__main__":
	main()
