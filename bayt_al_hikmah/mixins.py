""" Mixins """


# Create your mixins here.
class OwnerMixin:
    """Add the owner of the object"""

    def perform_create(self, serializer):
        """Save the object with owner"""

        serializer.save(user=self.request.user)
