from django.http import JsonResponse
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from .serializers import TodaySerializer, WeekSerializer
from .models import Today, Week_avg

@api_view(['GET'])
def week_detail(request, update_at):
    ic(update_at)
    dbToday = Today.objects.get(pk=update_at)
    ic(dbToday)
    todaySerializer = TodaySerializer(dbToday, many=False)
    ic(todaySerializer)
    return JsonResponse(data=todaySerializer.data, safe=False)

@api_view(['GET'])
def today_detail(request, update_at):
    ic(update_at)
    dbWeek = Week_avg.objects.get(pk=update_at)
    ic(dbWeek)
    weekSerializer = WeekSerializer(dbWeek, many=False)
    ic(weekSerializer)
    return JsonResponse(data=weekSerializer.data, safe=False)
