# test_payledger.py
"""
Tests for PayLedger module.
"""

import unittest
from payledger import PayLedger

class TestPayLedger(unittest.TestCase):
    """Test cases for PayLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PayLedger()
        self.assertIsInstance(instance, PayLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PayLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
