'''pytest fixtures for all apps'''
import pytest
from django.urls import reverse

def assert_view_renders_template(client, user, view_name, param, template):
    '''
    reusable function that checks if the template has been rendered
    '''
    client.force_login(user)
    if param is None:
        path = reverse(view_name)
    else:
        path = reverse(view_name, kwargs=param)
    response = client.get(path)
    template = template
    assert template in (t.name for t in response.templates)


@pytest.fixture
def user(django_user_model):
    '''
    pytest fixture creating mock user for the tests
    '''
    # django_user_model.objects.all().delete()
    test_user = django_user_model.objects.filter(username='test')
    if not test_user.count():
        test_user = django_user_model.objects.create(username='test', password='test')
    return test_user
