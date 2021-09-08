from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('add/',views.addadmin,name='addadmin'),
    path('add1/',views.addprepaid,name='addprepaid'),
    path('add2/',views.addpostpaid,name='addpostpaid'),
    path('add3/',views.adddongle,name='adddongle'),

    path('pre/',views.prepaidview,name='prepaidview'),
    path('post/',views.postpaidview,name='postpaidview'),
    path('don/',views.dongleview,name='dongleview'),
    

    path('updatesearch1/',views.updatesearchapi1,name='updatesearchapi1'),
    path('updatesearch2/',views.updatesearchapi2,name='updatesearchapi2'),
    path('updatesearch3/',views.updatesearchapi3,name='updatesearchapi3'),
    path('update1/',views.preupdate,name='preupdate'),
    path('update2/',views.postupdate,name='postupdate'),
    path('update3/',views.dongleupdate,name='dongleupdate'),
    path('delete1/',views.prepaiddelete,name='prepaiddelete'),
    path('delete2/',views.postpaiddelete,name='postpaiddelete'),
    path('delete3/',views.dongledelete,name='dongledelete'),
    path('loginview/',views.loginview,name='loginview'),


    path('vie1/',views.previewss,name='previewss'),
    path('vie2/',views.postviewss,name='postviewss'),
    path('vie3/',views.dongleviewss,name='dongleviewss'),
    path('si1/',views.presearch,name='presearch'),
    path('si2/',views.postsearch,name='postsearch'),
    path('si3/',views.donglesearch,name='donglesearch'),
    
    path('update_action_api1/',views.update_data_read1,name='update_data_read1'),
    path('update_action_api2/',views.update_data_read2,name='update_data_read2'),
    path('update_action_api3/',views.update_data_read3,name='update_data_read3'),
    path('deletesearch1/',views.deletesearchapi1,name='deletesearchapi1'),
    path('deletesearch2/',views.deletesearchapi2,name='deletesearchapi2'),
    path('deletesearch3/',views.deletesearchapi3,name='deletesearchapi3'),
    


    path('viewall/',views.admin_all,name='admin_all'),
    path('viewallpre/',views.prepaid_all,name='prepaid_all'),
    path('viewallpost/',views.postpaid_all,name='postpaid_all'),
    path('viewalldongle/',views.dongle_all,name='dongle_all'),
    path('updatepre/',views.updatesearchapi1,name='updatesearchapi1'),
    path('updatepost/',views.updatesearchapi2,name='updatesearchapi2'),
    path('updatedongle/',views.updatesearchapi3,name='updatesearchapi3'),
    
    path('login/',views.login_check,name='login_check'),

    path('admin/',views.adminPage),

###############query#################################################################################
    path('updatequery/',views.updatesearchapiquery,name="updatesearchapiquery"),
    path('update_data_readquery/',views.update_data_readquery,name='update_data_readquery'),
    path('up/',views.updatequery,name='updatequery'),
    path('upa/<fetch>',views.viewquerydetails,name='viewquerydetails'),
    path('viewquery/',views.viewquery,name='viewallqueries'),
    path('viewhtmlquery/',views.queryview,name='queryview'),

 #Customer

    # path('register/',views.customer),
    # path('addcustomer/',views.addCustomer),


    path('viewplans/',views.viewplans),
    # path('view/',views.viewCustomers,name='viewUsers'),
    # path('updatecustomer/',views.updateCustomers,name='updateUser'),
    path('update_data/',views.update_data,name='update_data'),
    path('update/',views.update_search,name="update_search"),

    path('viewall/',views.viewAll,name='viewAll'),
    
    path('login1/',views.login_checkcustomer,name='login_checkcustomer'),
    path('log/',views.loginviewcustomer,name='loginviewcustomer'),
    path('home/',views.homepage,name='homepage'),
    path('rsuc/',views.registersuccess,name='registersuccess'),
    path('services/',views.customerservices,name='customerservices'),

#######customerquery##################
    path('customerquery/',views.cusquery),
    path('queryupdate/',views.update_dataquery),
    path('queryFaq/',views.custf),

 path('upload/',views.upload,name='upload'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
