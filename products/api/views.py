from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer
from ..models import Product

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET api/',
        'GET api/routes',
        'GET api/routes :id'

    ]
    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, id):
    products = Product.objects.get(id=id)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)