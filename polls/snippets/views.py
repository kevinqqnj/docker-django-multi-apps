from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly
from .models import Snippet
from .serializers import SnippetSerializer

# app_name = 'snippets'
app_name = __package__.split('.')[-1]

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
