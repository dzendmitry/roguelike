from __future__ import annotations

from components.base_component import BaseComponent
from input_handlers import GameOverEventHandler
from render_order import RenderOrder

from entity import Actor

class Fighter(BaseComponent):
    entity: Actor

    def __init__(self, hp: int, defence: int, power: int) -> None:
        super().__init__()
        self.max_hp = hp
        self._hp = hp
        self.defence = defence
        self.power = power

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.entity.ai:
            self.die()

    def die(self) -> None:
        if self.engine.player is self.entity:
            death_message = "You died!"
            self.engine.event_handler = GameOverEventHandler(self.engine)
        else:
            death_message = f"{self.entity.name} is dead!"

        self.entity.char = "%"
        self.entity.color = (191, 0, 0)
        self.entity.block_movement = False
        self.entity.ai = None
        self.entity.name = f"remains of {self.entity.name}"
        self.entity.render_order = RenderOrder.COPRSE

        print(death_message)
