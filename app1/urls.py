from django.urls import path
from . import views

urlpatterns = [
    
   path('offerr',views.offerr.as_view(),name='user'),
   path('offer/<int:id>',views.offer.as_view()),
   path('addofferr',views.Addofferr.as_view()),
   path('addoffer/<int:id>',views.Addoffer.as_view()),
   path('requestt',views.requestt.as_view()),
   path('request/<int:id>',views.request.as_view()),
   path('commentt',views.commentt.as_view()),
   path('comment/<int:id>',views.comment.as_view()),
]