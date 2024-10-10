from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, SnippetCategory
from django.contrib.auth.models import User

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField()
    linenos = serializers.IntegerField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

class SnippetSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'category']

class SnippetCategorySerializer(serializers.ModelSerializer):
    snippet_set = SnippetSerializer(many=True, read_only=True)

    class Meta:
        model = SnippetCategory
        fields = ['id', 'name', 'snippet_set']

class UserSerializer(serializers.ModelSerializer):
    # เพิ่ม snippets ซึ่งจะแสดง list ของ PK ของ snippets ที่ user นั้นๆ เป็นเจ้าของ
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
