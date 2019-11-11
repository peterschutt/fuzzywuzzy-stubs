# Copyright (C) 2019 Peter Schutt
#
# This file is part of fuzzywuzzy-stubs.
#
# fuzzywuzzy-stubs is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# fuzzywuzzy-stubs is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fuzzywuzzy-stubs.  If not, see <http://www.gnu.org/licenses/>.

# Stubs for fuzzywuzzy.string_processing (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

PY3: Any
string = str

class StringProcessor:
    regex: Any = ...
    @classmethod
    def replace_non_letters_non_numbers_with_whitespace(cls, a_string: Any): ...
    strip: Any = ...
    to_lower_case: Any = ...
    to_upper_case: Any = ...
