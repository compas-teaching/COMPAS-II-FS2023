from __future__ import print_function

import os

from compas_invocations import style
from compas_invocations import tests
from invoke import Collection

ns = Collection(
    style.check,
    style.lint,
    style.format,
    tests.test,
)
ns.configure(
    {
        "base_folder": os.path.dirname(__file__),
    }
)
