from rest_framework import generics, mixins
from .models import Student
from .serializers import StudentSerializer


class StudentsGeneralView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentsSpecificView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin, mixins.DestroyModelMixin):

    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs, partial=True)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

