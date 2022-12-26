from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student,Path

from .serializers import StudentSerializer, PathSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#
#GET: Sunucudan bir belge veya veri almak için kullanılır. GET isteği yalnızca veriyi okumak için kullanılmalıdır, çünkü GET isteği tarayıcı ve proxy sunucuları tarafından önbelleğe alınabilir ve bu nedenle birkaç kez çalıştırılabilir.
#HEAD: Sunucudan bir belge veya verinin üstbilgilerini almak için kullanılır. HEAD isteği, GET isteğine benzerdir, ancak sunucudan geri dönen veri yoktur. Bu, sunucudaki bir belgenin varlığını veya önbelleklenme durumunu kontrol etmek için kullanılabilir.
#POST: Sunucuya bir belge veya veri göndermek için kullanılır. POST isteği, veritabanı güncelleştirmesi gibi veri oluşturan ve değiştiren işlemler için kullanılır.
#PUT: Sunucuya bir belge veya veri yüklemek için kullanılır. PUT isteği, bir belge veya verinin tamamının yerine koyulması için kullanılır.
#DELETE: Sunucudaki bir belge veya veriyi silmek için kullanılır.
#CONNECT: Sunucuyla bir iletişim kanalı oluşturmak için kullanılır.
#OPTIONS: Sunucunun desteklediği HTTP metotlarının bir listesini almak için kullanılır.
#TRACE: Sunucudan gönderilen bir isteğin yolunu takip etmek için kullanılır.
#PATCH: Sunucudaki bir belge veya verinin bir parçasını değiştirmek için kullanılır.



@api_view(['GET'])
def students_list(req):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_student(req):
    serializer = StudentSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            'message' : f" Student {serializer.validated_data.get('first_name')} successfully saved"
        }
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def student_detail(req, id):
   #student = Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)
    serilaizer = StudentSerializer(student)
    return Response(serilaizer.data)


@api_view(['PUT'])
def student_update(req, id):
    student = get_object_or_404(Student, id=id)
    serializer = StudentSerializer(instance=student, data=req.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            'message' : f" Student {serializer.validated_data.get('first_name')} successfully updated"
        }
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(req, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    message = {
            'message' : f" Student successfully deleted"
        }
    return Response(message)