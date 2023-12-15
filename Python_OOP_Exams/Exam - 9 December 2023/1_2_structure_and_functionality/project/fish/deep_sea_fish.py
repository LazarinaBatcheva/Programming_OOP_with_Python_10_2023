from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    def __init__(self, name: str, points: float):
        super().__init__(name, points, 180)

    @property
    def get_fish_type(self) -> str:
        return self.__class__.__name__
