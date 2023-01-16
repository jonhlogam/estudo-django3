
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from produtos.api.viewsets import ProdutoViewSet
from clientes.api.viewsets import ClienteViewSet
from pedidos.api.viewsets import PedidosViewSet
from destaque.api.viewsets import DestaqueViewSet
from estoque.api.viewsets import EstoqueViewSet
from meta_gestores.api.viewsets import Metas_Gestores_ViewSet
from pedidos_item.api.viewsets import Item_pedidos_ViewSet
from banner.api.viewsets import BannerViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'todo/v1/banner', BannerViewSet, basename='Banner')
router.register(r'todo/v1/produto', ProdutoViewSet, basename='Produto')
router.register(r'todo/v1/destaque', DestaqueViewSet, basename='Destaque')
router.register(r'todo/v1/pedidos', PedidosViewSet, basename='pedidos')
router.register(r'todo/v1/estoque', EstoqueViewSet, basename='estoque')
router.register(r'todo/v1/item_pedidos', Item_pedidos_ViewSet, basename='itempedidos')
router.register(r'todo/v1/cliente', ClienteViewSet)
router.register(r'todo/v1/metas_gestor', Metas_Gestores_ViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
   # import debug_toolbar
 ##   urlpatterns=[
   ##  ]
