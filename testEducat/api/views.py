from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskItemSerializer
from .models import TaskItem
from django.shortcuts import get_object_or_404

class TaskItemViews(APIView):
    def post(self, request):
        serializer = TaskItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, id=None):
        if id:
            item = TaskItem.objects.get(id=id)
            serializer = TaskItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = TaskItem.objects.all()
        serializer = TaskItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = TaskItem.objects.get(id=id)
        serializer = TaskItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(TaskItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})