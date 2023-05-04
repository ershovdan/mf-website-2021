from django.urls import path, include
import main_app
import contacts_app.views

urlpatterns = [
    path('', contacts_app.views.ContactsPage,  name="contacts"),
]