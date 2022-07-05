from .serializers import WandAdSerializers, BookmarkSerializer, NoteSerializer
from rest_framework import generics, status
from ..models import WantAd, Note
from rest_framework.response import Response


class HomeApiView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        # try:
        queryset = WantAd.objects.all()
        serializer = WandAdSerializers(instance=queryset, many=True)
        context = {
            'is_done': True,
            'message': 'لیست تمام محصولان',
            'data': serializer.data
        }
        return Response(data=context, status=status.HTTP_200_OK)
    #     # except:
    #
    #     contex = {
    #     'is_done': False,
    #     'message': 'خطا در انجام عملیات'
    #     }
    # return Response(data=contex, status=status.HTTP_400_BAD_REQUEST)


#
# class WantAdRetrieveAPI(generics.GenericAPIView):
#     serializer_class =
#
#     def get(self, request, *args, **kwargs):
#         want_id = kwargs.get('id')
#         try:


class BookmarkApiView(generics.GenericAPIView):
    serializer_class = BookmarkSerializer

    def get(self, request, *args, **kwargs):
        queryset = request.user.wantsads_bookmark.all()
        serializer = self.serializer_class(instance=queryset, many=True)
        context = {
            'is_done': True,
            'message': 'bookmark های کاربر',
            'data': serializer.data
        }
        return Response(data=context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            context = {
                'is_done': True,
                'message': 'با موفقیت به bookmark ها اضافه شد',
                'data': serializer.data
            }
            return Response(data=context, status=status.HTTP_200_OK)
        context = {
            'is_done': False,
            'message': 'خطا در انجام عملیات',
            'data': serializer.errors
        }
        return Response(data=context, status=status.HTTP_400_BAD_REQUEST)


class NoteApiView(generics.GenericAPIView):
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        queryset = request.user.wantsads_note.all()
        serializer = self.serializer_class(instance=queryset, many=True)
        context = {
            'is_done': True,
            'message': 'یادداشت های کاربر',
            'data': serializer.data
        }
        return Response(data=context, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        note = Note.objects.filter(user=request.user.id, want=serializer.validated_data['want'])
        if note.exists():
            serializer = self.serializer_class(data=request.data, instance=note, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            context = {
                'is_done': True,
                'message': 'عملیات با موفقیت انجام شد',
                'data': serializer.data
            }
            return Response(data=context, status=status.HTTP_200_OK)
        context = {
            'is_done': True,
            'message': 'خطا دز انجام عملیات',
            'data': serializer.errors
        }
        return Response(data=context, status=status.HTTP_400_BAD_REQUEST)
