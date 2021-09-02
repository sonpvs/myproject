from django.urls import path
from . import views

app_name = "news"
urlpatterns = [
    path('', views.index, name="index"),
    path('chart/', views.chart, name="chart"),
    path('chart01/', views.chart_01, name="chart01"),
    path('add/', views.add_post, name="add"),
    path('save/', views.save_news, name="save"),
    path('addbb/', views.add_baby, name="addbb"),
    path('savebb/', views.save_baby, name="savebb"),
    path('addks/', views.add_khaosat, name="addks"),
    path('saveks/', views.save_khaosat, name="saveks"),
    path('viewks/', views.view_khaosat, name="viewks"),
    path('viewch/', views.chuanhoa, name="viewch"),
    path('viewdes/', views.view_describe, name="viewdes"),
    path('chrt/', views.chart_select_view, name="chrt"),
]
