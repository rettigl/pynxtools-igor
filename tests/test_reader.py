#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
Basic example based test for the igor reader
"""

from pathlib import Path

from pynxtools.testing.nexus_conversion import ReaderTest


def test_ibw_to_nexus_conversion(caplog, tmp_path):
    """
    Tests the conversion of multiple ibw files into nexus.
    """
    caplog.clear()
    dir_path = Path(__file__).parent / "data"
    test = ReaderTest(
        nxdl="NXroot",
        reader_name="igor",
        files_or_dir=[
            str(dir_path / "config_file.json"),
            str(dir_path / "Norm_0057.ibw"),
            str(dir_path / "Norm_0059.ibw"),
            str(dir_path / "example_ibw.nxs"),
        ],
        tmp_path=tmp_path,
        caplog=caplog,
    )
    test.convert_to_nexus(caplog_level="WARNING", ignore_undocumented=False)
    test.check_reproducibility_of_nexus()


def test_ibw_to_nexus_conversion_w_entry(caplog, tmp_path):
    """
    Tests the conversion of multiple ibw files into nexus with entry file.
    """
    caplog.clear()
    dir_path = Path(__file__).parent / "data"
    test = ReaderTest(
        nxdl="NXroot",
        reader_name="igor",
        files_or_dir=[
            str(dir_path / "config_file.json"),
            str(dir_path / "Norm_0057.ibw"),
            str(dir_path / "Norm_0059.ibw"),
            str(dir_path / "Norm57.yaml.entry"),
            str(dir_path / "example_ibw_entry.nxs"),
        ],
        tmp_path=tmp_path,
        caplog=caplog,
    )
    test.convert_to_nexus(caplog_level="WARNING", ignore_undocumented=False)
    test.check_reproducibility_of_nexus()


def test_pxp_to_nexus_conversion(caplog, tmp_path):
    """
    Tests the conversion of multiple ibw files into nexus with entry file.
    """
    caplog.clear()
    dir_path = Path(__file__).parent / "data"
    test = ReaderTest(
        nxdl="NXroot",
        reader_name="igor",
        files_or_dir=[
            str(dir_path / "config_file.json"),
            str(dir_path / "Fig2a.pxp"),
            str(dir_path / "Scan57_59.yaml.entry"),
            str(dir_path / "example_pxp.nxs"),
        ],
        tmp_path=tmp_path,
        caplog=caplog,
    )
    test.convert_to_nexus(caplog_level="WARNING", ignore_undocumented=False)
    test.check_reproducibility_of_nexus()
