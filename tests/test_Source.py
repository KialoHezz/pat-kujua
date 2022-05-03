import unittest
from app.models import Sources



class SourceTest(unittest.TestCase):
    '''
    to test the behavior of the source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(123,"hezron","/image/k.jpeg","Awesome",20/2/2022)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))



