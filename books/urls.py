from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('add/',views.add),
    path('many/',views.books),
    # path('book/<str:query>/',views.single),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),
    path('all/',views.work.as_view()),
    # path('list/',views.listss.as_view()),
]