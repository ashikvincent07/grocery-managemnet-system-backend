from rest_framework import serializers

from django.contrib.auth.models import User

from grocery_management.models import Grocery


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password':{'write_only':True}}


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    


class GrocerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Grocery
        fields = "__all__"
        read_only_fields = ['item_id', 'owner', 'created_date', 'updated_date']

    def validate_item_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Item name cannot be empty or just whitespace.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive value greater than zero.")
        return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value

    def validate(self, attrs):
        return super().validate(attrs)
    
    