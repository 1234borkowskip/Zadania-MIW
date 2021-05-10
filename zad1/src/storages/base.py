class BaseStorage(object):
    EXTENSION = None

    def save(self, filename=None, data=None):
        with open(f'../results/{filename}.{self.EXTENSION}', 'w') as f:
            self.perform_save(file=f, data=data)

    def perform_save(self, file, data):
        raise NotImplemented('This method must be implemented')


