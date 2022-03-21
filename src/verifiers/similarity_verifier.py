# Copyright 2022, Alvin Kuruvilla <alvineasokuruvilla@gmail.com>

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

import statistics
from rich.traceback import install

install()

# TODO: We need to addd the dictionaries of the data back into here
class SimilarityVerifier:
    def __init__(self, template_file_path: str, verification_file_path: str, threshold):
        self.template_file_path = template_file_path
        self.verification_file_path = verification_file_path
        self.THRESHOLD = threshold

    __slots__ = (
        "template_file_path",
        "verification_file_path",
        "THRESHOLD",
    )

    def class_name(self) -> str:
        return "Similarity Verifier"

    def template_path(self):
        return self.template_file_path

    def set_threshold(self, threshold):
        self.threshold = threshold

    def get_threshold(self):
        return self.THRESHOLD

    def verification_path(self):
        return self.verification_file_path

    def set_template_file_path(self, new_template_file_path: str):
        self.template_file_path = new_template_file_path

    def set_verification_file_path(self, new_verification_file_path: str):
        self.verification_file_path = new_verification_file_path

    def calculate_standard_deviation(self, data: list):
        sdev = statistics.pstdev(data)
        return sdev
