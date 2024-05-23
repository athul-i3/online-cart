from django.urls import path
from user import views
urlpatterns=[
  path('',views.userhome,name='userhome'),  
  path('shop',views.shop,name='shop'),
  path('cart/<int:product2id>',views.cart,name='cart'),
  path('viewcart',views.viewcart,name='viewcart'),
  path('removeitem/<int:removeid>',views.removeitem,name='removeitem'),
  path('checkout',views.checkout,name='checkout'),
  path('confirm_checkout',views.confirm_checkout,name='confirm_checkout'),
  path('addwishlist/<int:productid>',views.addwishlist,name='addwishlist'),
  path('wishlist',views.wishlist,name='wishlist'),
  path('remove_wishlist/<int:delete_wishlist>',views.remove_wishlist,name='remove_wishlist'),
  path('blog',views.blog,name='blog'),
  path('review/<int:product_id>',views.review,name='review'),
  path('subblog',views.subblog,name='subblog'),
  path('about',views.about,name='about'),
  path('contact',views.contact,name='contact'),
  path('home2',views.home2,name='home2'),  
  path('usersign',views.usersign,name='usersign'),  
  path('signin',views.signin,name='signin'), 
  path('logout',views.logout,name='logout'), 
  path('details/<int:productid>',views.details,name='details'),  
  path('userproduct/<int:catid>',views.userproduct,name='userproduct'),  
  path('userproduct2/<int:cat2id>',views.userproduct2,name='userproduct2'),  
  path('search',views.search,name='search'), 



 ]