from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'Method': 'GET',
            'body':None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'Method': 'GET',
            'body':None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create',
            'Method': 'POST',
            'body':{'body':""},
            'description': 'creates a new note with data sent in post req'
        },
        {
            'Endpoint': '/notes/id/update',
            'Method': 'PUT',
            'body': {'body':""},
            'description': 'Creates an existing note with data sent in'
        },
        {
            'Endpoint': '/notes/id/delete',
            'Method': 'DELETE',
            'body':None,
            'description': 'Deletes an existing note'
        }
    ]
    return Response(routes)