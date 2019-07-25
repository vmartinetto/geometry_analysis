"""
geometry_analysis
An example python package from the MoLSSI Software Summer School
"""

# Add imports here
from .molecule import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
