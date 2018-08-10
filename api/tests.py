from django.test import TestCase
from catalog.models import Temple, Religion, God
# Create your tests here.

class TempleTestCase(TestCase):
    """This class defines the test suite for the temple model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.name = "Test TempleName"
        self.summary = "some details"
        self.address = "some address"
        self.temple = Temple(name=self.name, summary=self.summary, religion=self.religion, address=self.address)

    def test_model_can_create_a_temple(self):
        """Test the temple model can create a temple."""
        old_count = Temple.objects.count()
        self.temple.save()
        new_count = Temple.objects.count()
        self.assertNotEqual(old_count, new_count)
