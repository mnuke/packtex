import os
import sys


paths = {
	'afm': ['TEXMF', 'fonts', 'afm'],
	'bst': ['TEXMF', 'bibtex', 'bst', 'PACKAGE'],
	'bib': ['TEXMF', 'doc', 'PACKAGE'],
	'cls': ['TEXMF', 'tex', 'latex', 'base'],
	'def': ['TEXMF', 'tex', 'latex', 'PACKAGE'],
	'dtx': ['TEXMF', 'install'],
	'dvi': ['TEXMF', 'install'],
	'enc': ['TEXMF', 'fonts', 'enc'],
	'etx': ['TEXMF', 'install'],
	'fd':  ['TEXMF', 'tex', 'latex', 'fss'],
	'ins': ['TEXMF', 'install'],
	'ist': ['TEXMF', 'discard'],
	'log': ['TEXMF', 'discard'],
	'lox': ['TEXMF', 'tex', 'latex', 'PACKAGE'],
	'map': ['TEXMF', 'fonts', 'map'],
	'mtx': ['TEXMF', 'install'],
	'otf': ['FONT'],
	'pdf': ['TEXMF', 'doc', 'PACKAGE'],
	'pfb': ['TEXMF', 'fonts', 'type1'],
	'sty': ['TEXMF', 'tex', 'latex', 'PACKAGE'],
	'tex': ['TEXMF', 'install'],
	'tss': ['TEXMF', 'tex', 'latex', 'PACKAGE'],
	'txt': ['TEXMF', 'discard'],
	'ttf': ['TEXMF', 'fonts', 'truetype'],
	'vf':  ['TEXMF', 'fonts', 'vf'],
}

home_dir = os.path.expanduser('~')

if sys.platform == 'win32':
	font_dir = os.path.join(home_dir, 'Desktop')
	packtex_dir = os.path.join('C:', 'Program Files', 'PackTeX')
	tex_dir = os.path.join(home_dir, 'texmf')
elif sys.platform == 'darwin':
	font_dir = os.path.join(home_dir, 'Library', 'Fonts')
	packtex_dir = os.path.join(home_dir, '.packtex')
	tex_dir = os.path.join(home_dir, 'Library', 'texmf')
else:
	font_dir = os.path.join(home_dir, '.fonts')
	packtex_dir = os.path.join(home_dir, '.packtex')
	tex_dir = os.path.join(home_dir, 'texmf')

discard_dir = os.path.join(packtex_dir, 'discard')
install_dir = os.path.join(tex_dir, 'install')

metadata = os.path.join(packtex_dir, '.metadata')
log = os.path.join(packtex_dir, 'packtex.log')

if not os.path.isfile(metadata):
	if not os.path.exists(packtex_dir):
		os.mkdir(packtex_dir)
	open(metadata, 'w').close()


def get_metadata_file():
	return metadata


def get_discard_dir():
	return discard_dir


def get_install_dir():
	return install_dir


def get_path(filetype, package):
	if filetype:
		try:
			path = '/'.join(paths[filetype])
		except KeyError:
			path = 'TEXMF/extras'
	else:
		path = '/'.join(paths['sty'])
	path = path.replace('FONT', font_dir)
	path = path.replace('TEXMF', tex_dir)
	path = path.replace('PACKAGE', package)
	return path


def get_tex_dir():
	return tex_dir


def get_valid_filetypes():
	return paths.keys()
