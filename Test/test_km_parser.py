# Copyright 2022, Alvin Kuruvilla <alvineasokuruvilla@gmail.com>

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

import os
from parsers.km_parser import KM_Parser


def test_get_bbmas_dir():
    parser = KM_Parser()
    assert parser.get_bbmas_dir() == os.path.join(os.getcwd(), "gen", "km")


def test_get_bbmas_dir_with_param():
    pass


def test_get_threshold():
    pass


def test_set_template_file_path():
    pass


def test_set_verification_file_path():
    pass
