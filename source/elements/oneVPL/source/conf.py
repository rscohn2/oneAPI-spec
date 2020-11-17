# SPDX-FileCopyrightText: 2019-2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import json

# Add this conf and the shared conf files to the path
sys.path.insert(0, os.path.abspath(os.path.join('..','..','..','conf')))
sys.path.insert(0, os.path.abspath('.'))

with open('../../../../oneapi-doc.json') as fin:
    cfg = json.load(fin)

project = 'oneVPL'

# import these will populate conf namespace
import element_conf
import common_conf

cpp_id_attributes = ['MFX_CDECL']

c_id_attributes = ['MFX_CDECL']

setup = common_conf.setup

import traceback

traceback.print_stack()
print('Here:', __file__)
print('Extensions:', extensions)
