#!/Users/matbook/.pyenv/versions/3.8.3/envs/VQenv/bin/python
import sys, os, pyperclip


try:
	with open(os.path.expanduser('/Volumes/~mmignin/RemoteVQ/clipboard.txt'), 'r') as f:
		cliptext = f.read()
	print(cliptext)
except:
	print('')










