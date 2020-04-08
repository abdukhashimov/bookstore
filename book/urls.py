from django.urls import path
from book.views import BookApiView

urlpatterns = [
    path('book/', BookApiView.as_view(), name='testbook'),
]
