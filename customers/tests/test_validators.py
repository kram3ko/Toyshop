from django.core.exceptions import ValidationError
from customers.validators import (
    ExactLenValidator,
    FirstUpperLetter,
    LastDigits,
)
import unittest


class ValidatorsTestCase(unittest.TestCase):
    def test_exact_len_validator_pass(self):
        validator = ExactLenValidator(limit_value=5)
        try:
            validator("abcde")
        except ValidationError:
            self.fail("ExactLenValidator raised ValidationError unexpectedly!")

    def test_exact_len_validator_fail(self):
        validator = ExactLenValidator(limit_value=5)
        with self.assertRaises(ValidationError):
            validator("abc")

    def test_first_upper_letter_pass(self):
        validator = FirstUpperLetter(limit_value=3)
        try:
            validator("ABC1234567")
        except ValidationError:
            self.fail("FirstUpperLetter raised ValidationError unexpectedly!")

    def test_first_upper_letter_fail(self):
        validator = FirstUpperLetter(limit_value=3)
        with self.assertRaises(ValidationError):
            validator("AbC1234567")

    def test_last_digits_pass(self):
        validator = LastDigits(limit_value=4)
        try:
            validator("ABC1234")
        except ValidationError:
            self.fail("LastDigits raised ValidationError unexpectedly!")

    def test_last_digits_fail(self):
        validator = LastDigits(limit_value=4)
        with self.assertRaises(ValidationError):
            validator("ABC12AA")
