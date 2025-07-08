from polyfactory.factories.pydantic_factory import ModelFactory
from faker import Faker
from pydantic_model import (
    Appearance,
    Work,
    Superhero
)

fake = Faker()


class AppearanceFactory(ModelFactory):
    __model__ = Appearance

    @classmethod
    def gender(cls) -> str:
        return cls.__random__.choice(["Male", "Female", "Other", "-"])

    @classmethod
    def race(cls) -> str:
        races = ["Human", "Mutant", "Alien", "Robot", "God", "Demon", "Unknown"]
        return cls.__random__.choice(races)

    @classmethod
    def height(cls) -> list[str]:
        return [
            f"{cls.__random__.randint(1, 1000)}'{cls.__random__.randint(1, 1000)}",
            f"{cls.__random__.randint(1, 1000)} cm"
        ]

    @classmethod
    def weight(cls) -> list[str]:
        return [
            f"{cls.__random__.randint(1, 600)} lb",
            f"{cls.__random__.randint(1, 300)} kg"
        ]

    @classmethod
    def eye_color(cls) -> str:
        return fake.color_name()

    @classmethod
    def hair_color(cls) -> str:
        return fake.color_name()


class WorkFactory(ModelFactory):
    __model__ = Work

    @classmethod
    def occupation(cls) -> str:
        return cls.__random__.choice(["Hero", "Scientist", "Detective", "Vigilante", "Agent"])

    @classmethod
    def base(cls) -> str:
        return fake.country()


class SuperheroFactory(ModelFactory):
    __model__ = Superhero

    @classmethod
    def id(cls) -> int:
        return cls.__random__.randint(1, 10000)

    @classmethod
    def name(cls) -> str:
        return fake.name()

    @classmethod
    def appearance(cls) -> Appearance:
        return AppearanceFactory.build()

    @classmethod
    def work(cls) -> Work:
        return WorkFactory.build()


hero = SuperheroFactory.build()
with open("mock.json", "w") as f:
    f.write(hero.model_dump_json(indent=4))
