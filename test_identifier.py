from identifier import Identifier


class TestIdentifier:

    def setup_method(self):
        self.validator = Identifier()
    
    def test_ct01_empty_string(self):
        assert not self.validator.validate_identifier("")
    
    def test_ct02_minimum_valid_length(self):
        assert self.validator.validate_identifier("A")
    
    def test_ct03_length_two(self):
        assert self.validator.validate_identifier("AB")
    
    def test_ct04_medium_length_letters_digits(self):
        assert self.validator.validate_identifier("ABC12")
    
    def test_ct05_length_five(self):
        assert self.validator.validate_identifier("ABCDE")
    
    def test_ct06_maximum_valid_length(self):
        assert self.validator.validate_identifier("A12345")
    
    def test_ct07_exceeds_maximum_length(self):
        assert not self.validator.validate_identifier("A123456")
    
    def test_ct08_very_long_string(self):
        assert not self.validator.validate_identifier("stringmuitogrande")
    
    def test_ct09_lowercase_boundary(self):
        assert self.validator.validate_identifier("z")
    
    def test_ct10_uppercase_boundary(self):
        assert self.validator.validate_identifier("Z123")
    
    def test_ct11_starts_with_digit(self):
        assert not self.validator.validate_identifier("1")
    
    def test_ct12_only_digits(self):
        assert not self.validator.validate_identifier("123456")
    
    def test_ct13_starts_with_special_char(self):
        assert not self.validator.validate_identifier("@abc")
    
    def test_ct14_contains_special_char_at(self):
        assert not self.validator.validate_identifier("A@B")
    
    def test_ct15_contains_special_char_hyphen(self):
        assert not self.validator.validate_identifier("A-B")
    
    def test_ct16_lowercase_with_digit(self):
        assert self.validator.validate_identifier("a1")
    
    def test_ct17_maximum_lowercase(self):
        assert self.validator.validate_identifier("abc123")
    
    def test_ct18_contains_space(self):
        assert not self.validator.validate_identifier("A ")
        
    def test_boundary_first_uppercase_letter(self):
        assert self.validator.validate_identifier("A")
    
    def test_boundary_last_uppercase_letter(self):
        assert self.validator.validate_identifier("Z")
    
    def test_boundary_first_lowercase_letter(self):
        assert self.validator.validate_identifier("a")
    
    def test_mixed_case_valid(self):
        assert self.validator.validate_identifier("AaBbC1")
    
    def test_all_digits_after_letter(self):
        assert self.validator.validate_identifier("a12345")
    
    def test_starts_with_zero(self):
        assert not self.validator.validate_identifier("0abc")
    
    def test_starts_with_nine(self):
        assert not self.validator.validate_identifier("9abc")
    
    def test_contains_underscore(self):
        assert not self.validator.validate_identifier("A_B")
    
    def test_contains_dot(self):
        assert not self.validator.validate_identifier("A.B")
    
    def test_original_table_case_1(self):
        assert self.validator.validate_identifier("A1234")

    
