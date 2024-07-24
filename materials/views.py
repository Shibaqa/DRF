from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.paginators import MaterialsPaginator
from materials.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer, LessonDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    default_serializer = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MaterialsPaginator
    serializers_choice = {
        'retrieve': CourseDetailSerializer,
    }

    def get_serializer_class(self):
        """определяем сериализатор с учетом запрашиваемого действия
           (self.action = list, retrieve, create, update,delete).
           Если действие не указано в словарике serializers_choice -
           используется default_serializer"""
        return self.serializers_choice.get(self.action, self.default_serializer)


    def perform_create(self, serializer):
        """Привязываем текущего пользователя к создаваемому объекту"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        """Привязываем текущего пользователя к создаваемому объекту"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = MaterialsPaginator


class LessonRetrieveView(generics.RetrieveAPIView):
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()