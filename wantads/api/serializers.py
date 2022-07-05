from rest_framework import serializers
from ..models import WantAd, Image, Notes, Bookmark
from categories.api.serializers import CategorySerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')


class WandAdSerializers(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField('api:home', lookup_field='id')
    # categories = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = WantAd
        fields = (
            'id',
            'user',
            'title',
            'description',
            'active_chat',
            # 'categories',
            'city',
            'zone',
            'confirmed',
            'lat',
            'long',
            'show_phone',
            'data',
            'special',
            'images'
            # 'url',
        )
        read_only_fields = ('id', 'user', 'images')

        #

    # def get_categories(self, obj):
    #     return CategorySerializer(obj.category, many=True)

    def get_images(self, obj):
        return ImageSerializer(obj.images.all(), many=True).data


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('user', 'message', 'want')


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('user', 'want')
