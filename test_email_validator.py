import pytest
from email_validator import is_valid_email

class TestEmailValidator:
    
    # Эерэг тестүүд
    def test_valid_email(self):
        assert is_valid_email("user@example.com") == True
        assert is_valid_email("admin@company.org") == True
    
    # Сөрөг тестүүд
    def test_email_without_at_symbol(self):
        assert is_valid_email("invalidemail.com") == False
    
    def test_email_ending_with_test_domain(self):
        assert is_valid_email("user@test.com") == False
    
    # Edge cases
    def test_empty_email(self):
        assert is_valid_email("") == False
    
    def test_email_with_multiple_at_symbols(self):
        assert is_valid_email("user@@example.com") == True  # Одоогийн логик дээр
    
    def test_email_with_spaces(self):
        assert is_valid_email("user @example.com") == True
    
    def test_none_email(self):
        with pytest.raises(TypeError):
            is_valid_email(None)
