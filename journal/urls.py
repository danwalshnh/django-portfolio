from django.urls import path
from journal import views
app_name = "journal"
urlpatterns = [
    path("",views.journal_index, name="journal_index"),
    path("<int:pk>/", views.journal_detail, name="journal_detail"),
    path("<category>/", views.journal_category, name="journal_category"),
]