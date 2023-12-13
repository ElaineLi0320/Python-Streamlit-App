'''
Yini Li
CS 5001, Fall 2023
Final Project

This is the highlighted artworks class for the final project
This class is used to fetch the highlighted artworks data
This class will be applied to the random display features
'''


class Gallery:
    """
    A class representing a gallery of images of highlighted artworks

    Attributes:
        ids (int): A list to store ids for each artwork in the gallery.
        gallery_images (list): A list to store the images of the artworks.

    Methods:
        add_id(object_id): Adds an highlighted artwork's ID to the list of IDs in the gallery.
        get_item(index): Retrieves the image of the artwork at the specified index in the gallery.
    """
    def __init__(self):
        """
        Initializes a new instance of the Gallery class
        Setting up lists for storing IDs and images of artworks.
        """
        self.ids = []
        self.gallery_images = []

    def add_gallery_artwork_id(self, object_id):
        """
        Add highlighted artworks' IDs to the gallery.

        Args:
            object_id (int): The id of the artwork

        Raises:
            TypeError: If the `object_id` is not an integer.

        Returns:
            None
        """
        if not isinstance(object_id, int):
            raise TypeError("object_id must be an integer")
        self.ids.append(object_id)

    def get_gallery_item(self, index):
        """
        Get the image of the artwork of given index

        Args:
            index (int): The index of the artwork image to retrieve.

        Raises:
            TypeError: If the `index` is not an integer.
            IndexError: If the `index` is out of range.

        Returns:
            The image of the artwork at the given index.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0 or index >= len(self.gallery_images):
            raise IndexError("Index is out of range.")
        return self.gallery_images[index]
