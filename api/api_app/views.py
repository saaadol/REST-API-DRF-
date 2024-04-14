from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import Data
from .serializers import DataSerializer, TodoSerializer
from rest_framework.exceptions import NotFound


@api_view(["GET"])
def getTodos(request, pk):
    try:
        data = Data.objects.get(pk=pk)
    except Data.DoesNotExist:
        raise NotFound("key not found")
    todos = data.todos.all()
    todos_list = []
    for todo in todos:
        print("BLABLA")
        todo_values = {
            'todoName': todo.todoName,
            'description': todo.description,
            'isCompleted': todo.isCompleted,
        }
        todos_list.append(todo_values)
    return Response(todos_list)

def getData(request):
    data = Data.objects.all()
    serializer = DataSerializer(data, many = True)
    return Response(serializer.data)

@api_view(["POST"])   
def PostData(request): 
    serializer = DataSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

#Todo
@api_view(["POST"])   
def PostTodo(request): 
    serializer = TodoSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["GET","PUT"])   
def PostDataId(request, pk):
    olddata = Data.objects.get(id = pk) 
    serializer = DataSerializer(olddata, data = request.data)
    
    if serializer.is_valid():
        if (olddata.check_pass(serializer.initial_data["password"])):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response("Not correct Password",  status=403)
    return Response(serializer.errors, status=400)


@api_view(["GET","DELETE"])
def DeleteAll(request):
    allusers = Data.objects.all()
    allusers.delete()
    return Response("Ressources Deleted", 201)


@api_view(["GET", "DELETE"])
def DeleteDataId(request, pk):
    try:
        userdata = Data.objects.get(id = pk)
        userdata.delete()
        return Response("Deleted", status=200)
    except:
        return Response("id not available", status=400)


# Create your views here.
