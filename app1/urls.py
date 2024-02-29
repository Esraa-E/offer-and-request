from django.urls import path
from . import views

urlpatterns = [
    
   path('offerr',views.offerr.as_view(),name='user'),
   path('offer',views.offer.as_view()),
   path('addofferr',views.Addofferr.as_view()),
   path('addoffer',views.Addoffer.as_view()),
   path('requestt',views.requestt.as_view()),
   path('request',views.request.as_view()),
   path('commentt',views.commentt.as_view()),
   path('comment',views.comment.as_view()),
]