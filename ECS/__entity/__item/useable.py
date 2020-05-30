class Useable:
    def __init__(self, name, image, use_function=None, targeting=False, targeting_message=None, **kwargs):
        self.name = name
        self.image = image
        self.use_function = use_function
        self.function_kwargs = kwargs
        self.targeting = targeting
        self.targeting_message = targeting_message
