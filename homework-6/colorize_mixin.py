class ColorizeMixin:
    repr_color_code = 31

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__str__ = cls.colorize_str(cls.__str__)

    @classmethod
    def colorize_str(cls, original_str_method):
        def colored_str_method(self):
            return f"\033[1;{cls.repr_color_code};40m {original_str_method(self)}\n"
        return colored_str_method
