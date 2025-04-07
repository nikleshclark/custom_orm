class BaseModel:
    _instances = []

    def save(self):
        self._instances.append(self)

    def delete(self):
        self._instances.remove(self)

    @classmethod
    def query(cls):
        return cls._instances