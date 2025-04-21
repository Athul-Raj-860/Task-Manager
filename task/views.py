from rest_framework.decorators import api_view
from rest_framework.response import Response

from .Serializer import PostTask
from .models import Task


@api_view(['GET'])
def ViewAll(request): #View all tasks
    try:
        view = Task.objects.all()
        TaskSerializer = PostTask(view,many=True)
        return Response(TaskSerializer.data)
    except:
        return Response("Task list is Empty")

@api_view(['POST'])
def AddTask(request): #Add a new task
   Add = PostTask(data=request.data)
   if Add.is_valid():
       Add.save()
       return Response(Add.data)
   else:
        return Response("Data not Added")

@api_view(['PUT'])
def UpdateTask(request,id): #Update the already created task
   try:
       T = Task.objects.get(Id=id)
       TaskSerializer = PostTask(instance=T,data=request.data,partial=True)
       if TaskSerializer.is_valid():
           TaskSerializer.save()
           return Response(TaskSerializer.data)
       else:
           return Response("Data is not Updated")
   except T.DoesNotExist:
       return Response("Data not Found")

@api_view(['DELETE'])
def DeleteTask(request,id): #Delete the task
    try:
        T = Task.objects.get(Id=id)
        T.delete()
        return Response("Data Deleted")
    except T.DoesNotExist:
        return Response("Data is not Deleted")

@api_view(['GET'])
def FilterTask(request,status):#filter task according to status
    try:
        T = Task.objects.filter(Status=status)
        if T.exists():
            TaskSerializer = PostTask(T,many=True)
            return Response(TaskSerializer.data)
        else:
            return Response("Data not Found")
    except:
        return Response("Error!!!")

# Create your views here.
