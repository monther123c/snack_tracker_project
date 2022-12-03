from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class SnacksTest(TestCase):

    def test_snack_list_status(self):

        url=reverse('snacks_list')
        
        response =self.client.get(url)
        self.assertEqual(response.status_code,200)
      
    def test_snack_detail_status(self):

        url=reverse('snack_detail_1' , args=[1])
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_snack_list_template(self):

        url=reverse('snacks_list')
        
        response =self.client.get(url)
        self.assertTemplateUsed(response,'base.html')
      
    def test_snack_detail_template(self):

        url=reverse('snack_detail_1',args=[1])
        response=self.client.get(url)
        self.assertTemplateUsed(response,'snack_detail.html')