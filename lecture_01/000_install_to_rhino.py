from collections import namedtuple

import compas_rhino
from compas_rhino.install import install

args = namedtuple("args", ["version"])
args.version = "7.0"
compas_rhino.INSTALLATION_ARGUMENTS = args

install()
