from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.stretch import Stretch
from ..serializers.stretch_serializers import StretchSerializer

class Stretches(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = StretchSerializer
    def get(self, request):
        """Index request"""
        # Get all the stretches:
        # stretches = Stretch.objects.all()
        # Filter the stretches by owner, so you can only see your owned stretches
        stretches = Stretch.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = StretchSerializer(stretches, many=True).data
        return Response({ 'stretches': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['stretch']['owner'] = request.user.id
        # Serialize/create stretch
        stretch = StretchSerializer(data=request.data['stretch'])
        # If the stretch data is valid according to our serializer...
        if stretch.is_valid():
            # Save the created stretch & send a response
            stretch.save()
            return Response({ 'stretch': stretch.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(stretch.errors, status=status.HTTP_400_BAD_REQUEST)

class StretchDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the stretch to show
        stretch = get_object_or_404(Stretch, pk=pk)
        # Only want to show owned stretches?
        if not request.user.id == stretch.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this stretch')

        # Run the data through the serializer so it's formatted
        data = StretchSerializer(stretch).data
        return Response({ 'stretch': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate stretch to delete
        stretch = get_object_or_404(Stretch, pk=pk)
        # Check the stretch's owner agains the user making this request
        if not request.user.id == stretch.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this stretch')
        # Only delete if the user owns the  stretch
        stretch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['stretch'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['stretch'].get('owner', False):
            del request.data['stretch']['owner']

        # Locate Stretch
        # get_object_or_404 returns a object representation of our Stretch
        stretch = get_object_or_404(Stretch, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == stretch.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this stretch')

        # Add owner to data object now that we know this user owns the resource
        request.data['stretch']['owner'] = request.user.id
        # Validate updates with serializer
        data = StretchSerializer(stretch, data=request.data['stretch'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
