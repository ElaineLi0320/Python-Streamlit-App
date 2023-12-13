'''
Yini Li
CS 5001, Fall 2023
Final Project

This is the period class for the final project
This class is used to fetch the artwork's period data
This class will be applied to the data visualization features
'''

# Constants
ANCIENT_CLASSICAL = 260
MEDIEVAL = 1300
RENAISSANCE = 1780
ROMANTICISM = 1860
MODERN = 1945
CONTEMPORARY = 2023


class Period:
    """
    A class to represent period data

    Attributes:
        ids (list of int): A list to store the selected sample's ids
        year_list (list of int): A list to store the years of artworks being created
        period_counts (dict of {str: int}): A dictionary to store the count of each art period.

    Methods:
        add_id(object_id): Adds an artwork ID to the list of IDs.
        add_data(year): Adds a completion year to the list of artwork completion years.
        count_periods(): Counts the occurrences of each art period based on the completion years of artworks.
    """
    def __init__(self):
        """
        Initializes a new instance of the Period
        """
        self.ids = []
        self.artwork_completed_year_list = []
        self.art_period_counts = {
            "Ancient_Classical": 0,
            "Medieval": 0,
            "Renaissance": 0,
            "Romanticism": 0,
            "Modern": 0,
            "Contemporary": 0
            }

    def add_sample_artworks_ids(self, object_id):
        """
        Adds an artwork ID to the list of IDs.

        Args:
            object_id (int): The ID of the artwork to be added.

        Raises:
            TypeError: If 'object_id' is not an integer.

        Returns:
            None
        """
        if not isinstance(object_id, int):
            raise TypeError("Object ID must be an integer")
        self.ids.append(object_id)

    def add_sample_artworks_data(self, artwork_completed_year):
        """
        Adds a completion year to the list of artwork completion years.

        Args:
            artwork_completed_year (int): The year in which an artwork was completed.

        Raises:
            TypeError: If 'artwork_completed_year' is not an integer.

        Returns:
            None
        """
        if not isinstance(artwork_completed_year, int):
            raise TypeError("Artwork completion year must be an integer")
        self.artwork_completed_year_list.append(artwork_completed_year)

    def count_sample_art_periods(self):
        """
        Counts the occurrences of each art period based on the completion years of artworks.

        Returns:
            dict: A dictionary where each key is a historical art period and its value is the count of its occurrences.
        """
        for year in self.artwork_completed_year_list:
            if ANCIENT_CLASSICAL <= year < MEDIEVAL:
                self.art_period_counts["Ancient_Classical"] += 1
            elif MEDIEVAL <= year < RENAISSANCE:
                self.art_period_counts["Medieval"] += 1
            elif RENAISSANCE <= year < ROMANTICISM:
                self.art_period_counts["Renaissance"] += 1
            elif ROMANTICISM <= year < MODERN:
                self.art_period_counts["Romanticism"] += 1
            elif MODERN <= year < CONTEMPORARY:
                self.art_period_counts["Modern"] += 1
            elif year >= CONTEMPORARY:
                self.art_period_counts["Contemporary"] += 1
        return self.art_period_counts
