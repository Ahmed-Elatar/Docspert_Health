import uuid
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Account, CsvFiles, Transfer

class YourAppTests(TestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create some test accounts with valid UUIDs
        self.account1 = Account.objects.create(id=uuid.uuid4(), name='Account1', balance=1000.00)
        self.account2 = Account.objects.create(id=uuid.uuid4(), name='Account2', balance=2000.00)

        # Create a client to simulate browser
        self.client = Client()

    def test_index_view_get(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')



    def test_make_transfer_view_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('make_transfer'), {
            'accounts_from': self.account1.id,
            'accounts_to': self.account2.id,
            'amount': 500.00
        })
        self.assertEqual(response.status_code, 302)  
        self.account1.refresh_from_db()
        self.account2.refresh_from_db()
        self.assertEqual(self.account1.balance, 500.00)
        self.assertEqual(self.account2.balance, 2500.00)




    def test_list_accounts_view(self):
        response = self.client.get(reverse('list_accounts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_accounts.html')
        self.assertContains(response, self.account1.name)
        self.assertContains(response, self.account2.name)





    def test_list_transfers_view(self):
        Transfer.objects.create(accounts_from=self.account1, accounts_to=self.account2, amount=100.00)
        response = self.client.get(reverse('list_transfers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_transfers.html')
        self.assertContains(response, '100.00')

