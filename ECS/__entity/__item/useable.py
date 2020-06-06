class Useable:
    def __init__(self, name, images, use_function=None, targeting=False, targeting_message=None, **kwargs):
        self.name = name
        self.images = images
        self.use_function = use_function
        self.function_kwargs = kwargs
        self.targeting = targeting
        self.targeting_message = targeting_message
