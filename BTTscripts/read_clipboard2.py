#!/Users/matbook/.pyenv/versions/3.8.3/envs/VQenv/bin/python
import sys, os, pyperclip


try:
	# with open(os.path.expanduser('/Users/matbook/Desktop/VitaQuest Files/clipboard.txt'), 'r') as f:
	with open(os.path.expanduser('/Volumes/~mmignin/RemoteVQ/clipboard.txt'), 'r') as f:
		cliptext = f.read()
	pyperclip.copy(cliptext)
except:
	print('')












