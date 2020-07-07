from rest_framework import serializers
from news.models import News , last_3_news , Comments

class News_Serializers(serializers.ModelSerializer):
    class Meta :
        model = News
        fields = '__all__'
        
def serialized_news ():
    news = last_3_news()
    serialized_data = News_Serializers(news , many = True)
    return serialized_data

class Comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

def serialize_comments(comments):

    comments_serialized = Comment_Serializer(comments , many = True )

    return comments_serialized