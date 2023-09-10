from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logic_api.services.logic_expresion_service as le

@api_view(['GET', 'POST'])
def test_api_request(request):
    response = le.get_true_table(request.data["expresion"])
    if request.method == 'GET':
        return Response(response)

    elif request.method == 'POST':
        return Response(response, status=status.HTTP_202_ACCEPTED)