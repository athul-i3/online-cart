from django.urls import path
from adminapp import views

urlpatterns=[
    path('home1',views.home1,name='home1'),
    path('logout1',views.logout1,name='logout1'),
    path('categories',views.categories,name='categories'),
    path('viewcat',views.viewcat,name='viewcat'),
    path('delete/<int:deleteid>',views.deletecat,name='delete'),
    path('add_product',views.add_product,name='add_product'),
    path('viewprod',views.viewprod,name='viewprod'),
    path('edit/<int:runid>',views.edit,name='edit'),
    path('update/<int:updateid>',views.update,name='update'),
    path('deleteprod/<int:deleteprodid>',views.deleteprod,name='deleteprod'),
    path('notification',views.addnotification,name='notification'),
    path('viewnotification',views.viewnotification,name='viewnotification'),
    path('notdelete/<int:notdeleteid>',views.notdelete,name='notdelete'),
    path('complaints',views.complaints,name='complaints'),
    path('delcomplaints/<int:delcomplaintsid>',views.delcomplaints,name='delcomplaints'),
    path('viewsign',views.viewsign,name='viewsign'),
    path('deletesign/<int:signdeleteid>',views.deletesign,name='deletesign'),

    






]