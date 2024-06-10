class Figure:
    def __init__(self):
        pass

    def generate_points(self):
        pass


class FigureBuilder:
    def __init__(self, *args):
        self.check_succes = None
        # self.argument = argument
        self.__check_args()

    def __check_args(self):
        """
        default functionality example
        """
        check_success = True
        if check_success:
            self.check_succes = True
            return 1
        else:
            import warnings
            warnings.warn("Check failed")
            self.check_succes = False
            return 0

    def get_figure(self):
        """
        default functionality example
        """

        if self.check_succes is None:
            import warnings
            warnings.warn("Check has not been completed yet")
            return 0
        if self.check_succes:
            figure = Figure()

            def generate_points():
                return [["x"], ["y"]]

            figure.generate_points = generate_points
            return figure
        else:
            import warnings
            warnings.warn("Chack has failed")
            return 0
