# import pytest
# from django.urls import reverse
#
# from pyalexis.django_assertions import assert_contains
#
#
# @pytest.fixture
# def resp(client):
#     return client.get(reverse('videos:video', args=('treino1',)))
#
#
# def test_status_code(resp):
#     assert resp.status_code == 200
#
#
# def test_titulo_video(resp):
#     assert_contains(resp, '<h1>Treino 1</h1>')
#
#
# def test_conteudo_video(resp):
#     assert_contains(resp, 'iframe src="https://player.vimeo.com/video/479683301"')
