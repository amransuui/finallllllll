from django.urls import path
from . import views


urlpatterns = [
    path('register/',  views.UserRegistrationViews.as_view(), name='register'),
    path('login/',  views.Userloginviews.as_view(), name='login'),
    path('logout/',  views.userlogoutview.as_view(), name='logout'),
    path('profile/',  views.profileview, name='profile'),
    path('seeBook/',  views.seeBookview, name='seeBook'),
    path('category/<slug:category_slug>/', views.seeBookview, name='category_slug'),
    path('deposit/', views.deposit_money, name='deposit_money'),

    path('details/<int:pk>/', views.BookDetailsView.as_view(), name='book_details'),
    
    path("borrow/<int:id>", views.Borrowed_Book, name="borrow_book"), 
   
    path('return/<int:id>', views.Return_book, name='returnbook'),
    
    path('comments/<int:pk>/', views.Comment_views.as_view(), name='comment_views'),

    
    
]
