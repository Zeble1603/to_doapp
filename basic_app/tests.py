from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class TestsTask(TestCase):

    @classmethod
    def setUp(self):
        self.credentials = {
            'username': 'CristoCanyon',
            'password': 'Lastman'}
        user = User.objects.create_user(**self.credentials)
        Task.objects.create(name='Gagner la coupe', author=user)


    def test_task_creation(self):
        task = Task.objects.get(id=1)
        expected_name = task.name
        self.assertEquals(expected_name,'Gagner la coupe')

    def test_task_create_view(self):
        response = self.client.get(reverse('basic_app:create'))
        self.assertEquals(response.status_code, 302)

    def test_task_list_view(self):
        log = self.client.post(reverse('accounts:login'), self.credentials, follow=True)
        self.assertTrue(log.context['user'].is_active)
        response = self.client.get(reverse('basic_app:home'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Gagner la coupe')

    def test_task_update_view(self):
        log = self.client.post(reverse('accounts:login'), self.credentials, follow=True)
        self.assertTrue(log.context['user'].is_active)
        task = Task.objects.get(id=1)
        post_response = self.client.post(reverse('basic_app:update',kwargs={'pk':task.id}),
                                        {'name' : 'Gagner le tournoi',
                                         'due_date' : timezone.now(),
                                         'created_date' : timezone.now() ,  
                                         'author' : log})
        self.assertEquals(post_response.status_code, 302)     
        task.refresh_from_db()
        self.assertEquals(task.name, "Gagner le tournoi")                            

    def test_task_get_delete_view(self):
        self.client.post(reverse('accounts:login'), self.credentials, follow=True)
        task = Task.objects.get(id=1)
        get_response = self.client.get(reverse('basic_app:delete', kwargs={'pk':task.id}), follow=True)
        self.assertContains(get_response, "Are you sure you want to delete this task :")
        self.assertEquals(get_response.status_code, 200)

    def test_task_post_delete_view(self):
        self.client.post(reverse('accounts:login'), self.credentials, follow=True)
        task = Task.objects.get(id=1)
        post_response = self.client.post(reverse('basic_app:delete', kwargs={'pk':task.id}), follow=True)
        self.assertRedirects(post_response, reverse('basic_app:home'), status_code=302)  
        task_count = Task.objects.all().count()
        self.assertEquals(task_count, 0)    
