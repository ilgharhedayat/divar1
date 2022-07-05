from ..models import Category

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'children',)

    def get_children(self, obj):
        return CategorySerializer(obj.children.all(), many=True).data


class CategoryWantSerializer(CategorySerializer):
    wants = serializers.SerializerMethodField()

    class Meta(CategorySerializer.Meta):
        model = CategorySerializer.Meta.model
        fields = CategorySerializer.fields
    #
    # def get_wants(self, obj):
    #