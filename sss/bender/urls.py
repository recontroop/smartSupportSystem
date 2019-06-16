from django.urls import path
from . import views

urlpatterns = [
	path('test', views.test, name='test'),
	path('receiveTranscript', views.receive_transcript, name='receive_Transcript'),
	path('customerQuery', views.customer_query, name='customer_query'),
]