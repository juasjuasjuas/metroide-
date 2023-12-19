from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-post/', views.userPost, name='user-post'),
    path('mod/', views.Mod, name='mod'),
    path('topic/<int:pk>/', views.postTopic, name='topic-detail'),
    path('search-result/', views.searchView, name='search-result'),
    path('user-dashboard/', views.userDashboard, name='user-dashboard'),
    path('upvote/', views.upvote, name='upvote'),
    path('downvote/', views.downvote, name='downvote'),
    path('reportar/', views.reportar, name='reportar'),
    path('blog/', views.blogListView, name='blog'),
    path('article/<slug:slug>/', views.blogDetailView, name='article-detail'),
    path('rechazar_reporte/', views.rechazar_reporte, name='rechazar_reporte'),
    path('confirmar_reporte/', views.confirmar_reporte, name='confirmar_reporte'),
    
]
