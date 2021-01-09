from django.shortcuts import render, HttpResponse

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from Api.models import Api
from Api.serializers import ApiSerializer
from rest_framework.decorators import api_view

def Api_list(request):
    return HttpResponse("Hello from Api_list")
    
def Api_detail(request):
    return HttpResponse("Hello from Api_detail")

def Api_list_published(request):
    return HttpResponse("Hello from Api_list_published")


# @api_view(['GET', 'POST', 'DELETE'])
# def Api_list(request):

#     if request.method == 'GET':
#         Api = Api.objects.all()
        
#         title = request.GET.get('title', None)
#         if title is not None:
#             Api = Api.filter(title__icontains=title)
        
#         Api_serializer = ApiSerializer(Api, many=True)
#         return JsonResponse(Api_serializer.data, safe=False)

#     elif request.method == 'POST':
#         Api_data = JSONParser().parse(request)
#         Api_serializer = ApiSerializer(data=Api_data)

#         if Api_serializer.is_valid():
#             Api_serializer.save()
#             return JsonResponse(Api_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(Api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         count = Api.objects.all().delete()
#         return JsonResponse({'message': '{} Apis were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def Api_detail(request, pk):
#     try: 
#         Api = Api.objects.get(pk=pk)
#     except Api.DoesNotExist:
#         return JsonResponse({'message': 'Api does not exist'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         Api_serializer = ApiSerializer(Api)
#         return JsonResponse(Api_serializer.data)

#     elif request.method == 'PUT':
#         Api_data = JSONParser().parse(request)
#         Api_serializer = ApiSerializer(Api, data=Api_data)

#         if Api_serializer.is_valid():
#             Api_serializer.save()
#             return JsonResponse(Api_serializer.data)
#         return JsonResponse(Api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         Api.delete()
#         return JsonResponse({'message': 'Api was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def Api_list_published(request):
#     Api = Api.objects.filter(published=True)

#     if request.method == 'GET':
#         Api_serializer = ApiSerializer(Api, many=True)
#         return JsonResponse(Api_serializer.data, safe=False)