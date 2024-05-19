import uuid


class Guid:
    @staticmethod
    def guid(upper=False):
        uid = str(uuid.uuid4())
        return uid.upper() if upper else uid


if __name__ == '__main__':
    print(Guid.guid())
