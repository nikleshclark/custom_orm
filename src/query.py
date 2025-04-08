class Query:
    def __init__(self, model):
        self.model = model
        self.filters = []
    def filter(self, **kwargs):
        """
        Add filter conditions to the query.
        """
        for key, value in kwargs.items():
            self.filters.append((key, value))
        return self
    # def filter(self, **kwargs):
    #     self.filters.append(kwargs)
    #     return self

    def all(self):
        # This method would interact with the database to retrieve all records
        # based on the filters applied. For now, it returns a placeholder.
        return f"Retrieving all records for {self.model.__name__} with filters: {self.filters}"

    def first(self):
        # This method would interact with the database to retrieve the first record
        # based on the filters applied. For now, it returns a placeholder.
        return f"Retrieving the first record for {self.model.__name__} with filters: {self.filters}"