import pickle

availability = {
    "Before 1st Gym": [
        ["Snivy", "Servine", "Serperior"],
        ["Tepig", "Pignite", "Emboar"],
        ["Oshawott", "Dewott", "Samurott"],
        ["Patrat", "Watchog"],
        ["Lillipup", "Herdier", "Stoutland"],
        ["Purrloin", "Liepard"],
        ["Pansage", "Simisage"],
        ["Pansear", "Simisear"],
        ["Panpour", "Simipour"]
    ],
    "Before 2nd Gym": [
        ["Pidove", "Tranquill", "Unfezant"],
        ["Blitzle", "Zebstrika"],
        ["Roggenrola", "Boldore", "Gigalith"],
        ["Woobat", "Swoobat"],
        ["Drilbur", "Excadrill"],
        ["Tympole", "Palpitoad", "Seismitoad"],
        ["Timburr", "Gurdurr", "Conkeldurr"],
        ["Throh"],
        ["Sawk"],
        ["Munna", "Musharna"],
        ["Audino"]
    ],
    "Before 3rd Gym": [
        ["Sewaddle", "Swadloon", "Leavanny"],
        ["Venipede", "Whirlipede", "Scolipede"],
        ["Petilil", "Lilligant"],
        ["Cottonee", "Whimsicott"],
        ["Sandile", "Krokorok", "Krookodile"],
        ["Darumaka", "Darmanitan"],
        ["Scraggy", "Scrafty"]
    ],
    "Before 4th Gym": [
        ["Yamask", "Cofagrigus"],
        ["Sigilyph"],
        ["Maractus"],
        ["Dwebble", "Crustle"],
        ["Trubbish", "Garbodor"],
        ["Minccino", "Cinccino"],
        ["Solosis", "Duosion", "Reuniclus"],
        ["Gothita", "Gothorita", "Gothitelle"],
        ["Zorua", "Zoroark"],
        ["Tirtouga", "Carracosta"],
        ["Archen", "Archeops"]
    ],
    "Before 5th Gym": [
        ["Ducklett", "Swanna"],
        ["Vanillite", "Vanillish", "Vanilluxe"],
        ["Karrablast", "Escavalier"],
        ["Foongus", "Amoonguss"],
        ["Emolga"],
        ["Deerling", "Sawsbuck"]
    ],
    "Before 6th Gym": [
        ["Joltik", "Galvantula"],
        ["Ferroseed", "Ferrothorn"],
        ["Klink", "Klang", "Klinklang"],
        ["Tynamo", "Eelektrik", "Eelektross"],
        ["Litwick", "Lampent", "Chandelure"],
        ["Elgyem", "Beheeyem"],
        ["Cubchoo", "Beartic"]
    ],
    "Before 7th Gym": [
        ["Alomomola"],
        ["Basculin"],
        ["Stunfisk"],
        ["Frillish", "Jellicent"],
        ["Axew", "Fraxure", "Haxorus"],
        ["Larvesta", "Volcarona"],
        ["Shelmet", "Accelgor"],
        ["Mienfoo", "Mienshao"],
        ["Druddigon"],
        ["Cryogonal"],
        ["Golett", "Golurk"],
        ["Cobalion"],
        ["Virizion"]
    ],
    "Before 8th Gym": [
        ["Pawniard", "Bisharp"],
        ["Bouffalant"],
        ["Rufflet", "Braviary"],
        ["Vullaby", "Mandibuzz"]
    ],
    "Before Elite Four": [
        ["Heatmor"],
        ["Durant"],
        ["Deino", "Zweilous", "Hydreigon"],
        ["Terrakion"],
        ["Tornadus"],
        ["Thundurus"]
    ],
    "Post Elite Four": [
        ["Landorus"],
        ["Reshiram"],
        ["Zekrom"],
        ["Kyurem"],
        ["Victini"],
        ["Meloetta"],
        ["Genesect"],
        ["Keldeo"]
    ]
}


with open('availability.pkl', 'wb') as f:
    pickle.dump(availability, f)
