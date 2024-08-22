from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ensure you have a valid view called 'home'
    path('collections', views.collections, name='collections'),
    path("collections/<str:slug>",views.collectionsview,name="collectionsview"),
    path("collections/<str:cate_slug>/<str:prod_slug>",views.productview,name="productview"),
    path('features/', views.feature, name='Features'),  # Ensure you have a valid view called 'home'
    path('About/', views.Aboutus, name='Aboutus'),
    path('Contact/', views.Contactus, name='Contact'),
    path('Feedback/', views.FeedbackView, name='Feedback'),
    path('Complaint1/', views.Complaint, name='Complaint'),
    path('Login/', views.Login, name='Login'),
    path('Signup/', views.Signup, name='Signup'),
    
    
    path('Cart/', views.cart, name='Cart'),
    path('add-to-cart/', views.Cart2, name='addtocart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('delete-cart-item/', views.delete_cart_item, name='delete_cart_item'),
    path('placeOrder/', views.placeorder2, name='placeorder'),
    path('Pay/', views.Pay, name='Pay'),
    
    
    
    
    path('Wishlist/', views.Wishlists, name='Wishlist'),
    path('add-to-Wishlist/', views.addWishlist, name='addtoWishlist'),
    path('delete-list-item/', views.delete_list_item, name='delete_list_item'),
    path('product-list/', views.productlist, name='product-list'),
    path('search-product/', views.searchproduct, name='searchproduct'),
    path('search-results/', views.search_results, name='search_results'),
    
    

    # all urls releted a Messages.....
    path('Checkout/', views.Check, name='Checkout'),
    path('Booking/', views.Book, name='Booking'),
    path('Logout3/',views.Logout, name="logout"),
    path('already/', views.already, name='log'),
    path('Incorrect/',views.Incorrect, name="wrong"),
    path('NotResponse/',views.Password, name="notmatch"),
    path('SendMessage/', views.Send, name='success'),
    path('Feed/', views.Feed, name='Feedback'),
    




# Email Integration Urls ###
  path('activate/<uidb64>/<token>/', views. activate, name='activate'),




#Dashborad Url ##
path('Dashboard/' , views.Dash ,name='Dashboard'),
path('Compl/' , views.Compl ,name='Dashboard'),
path('Customer/' , views.Customer ,name='Customer'),
path('Billing/' , views.Bill ,name='Billing'),
path('contact-list/', views.contact_list_view, name='contact_list'),
path('feedback3/', views. Feedback2, name='feedback_list'),






]
