from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

import color

player = Actor(
    char="@",
    color=color.white,
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),    
    fighter=Fighter(hp=30, base_defense=1, base_power=2),    
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),    
)

orc = Actor(
    char="o",
    color=color.green,
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),    
    fighter=Fighter(hp=10, base_defense=0, base_power=3),    
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),    
)
troll = Actor(
    char="T",
    color=color.light_green,
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),    
    fighter=Fighter(hp=16, base_defense=1, base_power=4),    
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),    
)

confusion_scroll = Item(
    char="~",
    color=color.purple,
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=color.red,
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)
health_potion = Item(
    char="!",
    color=color.light_purple,
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),    
)
lightning_scroll = Item(
    char="~",
    color=color.amber,
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(
    char="/",
    color=color.light_blue,
    name="Dagger",
    equippable=equippable.Dagger()
)

sword = Item(
    char="/",
    color=color.light_blue,
    name="Sword",
    equippable=equippable.Sword())

leather_armor = Item(
    char="[",
    color=color.brown,
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[",
    color=color.brown,
    name="Chain Mail",
    equippable=equippable.ChainMail()
)

# end of entity_factories.py
