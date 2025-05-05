from rest_framework import serializers
from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.SerializerMethodField()

    class Meta:
        model = CinemaHall
        fields = ['id', 'name', 'rows', 'seats_in_row', 'capacity']

    def get_capacity(self, obj):
        return obj.rows * obj.seats_in_row


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'genres', 'actors']


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title')
    cinema_hall_name = serializers.CharField(source='cinema_hall.name')
    cinema_hall_capacity = serializers.IntegerField(source='cinema_hall.capacity')

    class Meta:
        model = MovieSession
        fields = ['id', 'movie_title', 'cinema_hall_name', 'cinema_hall_capacity', 'show_time']
