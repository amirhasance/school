from rest_framework import serializers
from news.models import News , last_3_news

class News_Serializers(serializers.ModelSerializer):
    class Meta :
        model = News
        fields = '__all__'
        
def serialized_news ():
    news = last_3_news()
    serialized_data = News_Serializers(news , many = True)
    return serialized_data