from django.urls import path, include
import main_app
import csgo_app.views


urlpatterns = [
    path('', csgo_app.views.MainCSGO, name="csgo"),
    path('key_check/', csgo_app.views.CheckKey),
    path('forum/', csgo_app.views.ForumMain),
    path('cobalt/', csgo_app.views.Cobalt),
    path('forum/topic/', csgo_app.views.Topic),
    path('forum/new_post/', csgo_app.views.NewPost),
    path('forum/new_topic/', csgo_app.views.NewTopic),
    path('forum/themes_list/', csgo_app.views.ThemesList),
    path('forum/search_topic/', csgo_app.views.SearchTopic),
    path('cobalt/pay_r30/', csgo_app.views.CobaltPayR30),
    path('cobalt/pay_r90/', csgo_app.views.CobaltPayR90),
    path('cobalt/pay_d30/', csgo_app.views.CobaltPayR30),
    path('cobalt/pay_d90/', csgo_app.views.CobaltPayR90),
    path('cobalt/pay/success/', csgo_app.views.CobaltSuc),
    path('cobalt/pay/hook', csgo_app.views.PayHook),
]

