from rest_framework.generics import CreateAPIView
from .serializers import PersonasSerializer
from rest_framework.response import Response

class PersonasController(CreateAPIView):
    serializer_class=PersonasSerializer
    def post(self,request):
        print(request)
        return Response(data='Hola amigos')

# Create your views here.
