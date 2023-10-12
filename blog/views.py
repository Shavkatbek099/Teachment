from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .models import Post, Student
from rest_framework.response import Response
from .serializer import PostSerializer, StudentSerializer
from rest_framework import status, permissions, mixins
from django.http import Http404
from rest_framework import generics
from django_filters import rest_framework as filters


class PostAPIView(APIView):
    def get(self, request, format=None):
        teacher_objs = Post.objects.all()
        serializer = PostSerializer(teacher_objs, many=True)
        data = serializer.data
        return Response(data)

    def post(self, request, format=None, *args, **kwargs):
        request_data = request.data
        serializer = PostSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TeacherDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            teacher_obj = Post.objects.get(pk=pk)
            return teacher_obj
        except Post.DoesNotExist as ex:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = PostSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        teacher_obj = self.get_object(pk)
        teacher_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        teacher_obj = self.get_object(pk)
        request_data = request.data
        serializer = PostSerializer(teacher_obj, request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            error = serializer.errors
            return Response(f"Xato ma'lumotlar kiritilgan {list(error.keys())[0]} "
                            f"{list(error.values())[0]}", status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        teacher_obj = self.get_object(pk)
        request_data = request.data
        serializer = PostSerializer(teacher_obj, request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            error = serializer.errors
            return Response(f"Xato ma'lumotlar kiritilgan {list(error.keys())[0]} "
                            f"{list(error.values())[0]}", status=status.HTTP_400_BAD_REQUEST)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 6


class StudentListCreateAPIView(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["id", ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)


class StudentRetrieveAPIView(mixins.RetrieveModelMixin,
                               generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    pagination_class = []

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
