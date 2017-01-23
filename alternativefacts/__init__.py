__all__ = ['alternativefacts']

class AlternativeFacts(object):
    def __bool__(self):
        return False

    def __nonzero__(self):
        return False

alternativefacts = AlternativeFacts()
