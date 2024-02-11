from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Todo
from .permissions import IsOwnerOrReadOnly
from .serializers import TodoSerializer
from .pagination import CustomPagination
from .filters import TodoFilter
from django.http import JsonResponse

# views.py




class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TodoFilter 

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]



# views.py
   



