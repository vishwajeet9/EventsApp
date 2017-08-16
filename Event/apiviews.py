from bson.json_util import loads
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from Event.models import Details


class GetDetails(APIView):
    def get(self, request, id):
        detail = Details.objects.get(id=id)
        detail = serializers.serialize('json', [ detail ])
        detail = loads(detail)
        return Response({"data": detail})


#class GetDetailsByDate(APIView):
 #   def get(self, request):
  #      data = request.GET["date"]
   #     detail1 =Details.objects.filter(date=data)
    #    detail1=serializers.serialize('json',detail1)
     #   detail1 = loads(detail1)
        # return render(request,'search.html',{'data1':detail1})
      #  return Response({"data1": detail1},template_name='search.html', content_type='text/html; charset=utf-8')
        # return Response(html_data,content_type='html')