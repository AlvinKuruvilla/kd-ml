# Copyright 2020-2021, Alvin Kuruvilla <alvineasokuruvilla@gmail.com>

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

from rich.traceback import install

install()

# TODO: We need to addd the dictionaries of the data back into here
class AbsoluteVerifier:
    def __init__(
        self, template_file_path: str, verification_file_path: str, threshold: float
    ):
        self.THRESHOLD = threshold
        self.template_file_path = template_file_path
        self.verification_file_path = verification_file_path

    def class_name() -> str:
        return "Absolute Verifier"

    def set_template_file_path(self, new_path: str) -> None:
        self.template_file_path = new_path

    def set_verification_file_path(self, new_path: str) -> None:
        self.verification_file_path = new_path

    def template_path(self):
        return self.template_file_path

    def verification_path(self):
        return self.verification_file_path

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
