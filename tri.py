#!/usr/bin/env python
# coding: utf8

import os
import locale
from datetime import datetime

# Set locale to FR since datetime will interprete FR month names
locale.setlocale(locale.LC_TIME, 'fr_FR')

U_CIRC='u\xcc\x82'
O_CIRC='o\xcc\x82'
E_CIRC='e\xcc\x82'
E_AIGU='e\xcc\x81'
E_GRAVE='e\xcc\x80'
A_CIRC='a\xcc\x82'

REPLACEMENT = {
	U_CIRC: 'û',
	O_CIRC: 'ô',
	E_CIRC: 'ê',
	A_CIRC: 'â',
	E_AIGU: 'é',
	E_GRAVE:'è'
}

for filename in os.listdir(os.getcwd()):
	old_filename = filename

	# Replace accents
	for pattern in REPLACEMENT:
		filename = filename.replace(pattern, REPLACEMENT[pattern])

	# Explode fields
	fields = filename.split()
	if len(fields) < 3:
		continue

	strdate = ' '.join(fields[-3:])
	moment = ' '.join(fields[:-3])

	# Rewrite date
	newdate = datetime.strptime(strdate, '%d %B %Y')
	newfields = [newdate.strftime('%Y-%m-%d')]

	# Construct new name
	if len(moment) > 0:
		newfields.append(moment)
	newname = ' - '.join(newfields)

	print (newname)
	os.rename(old_filename, newname)
