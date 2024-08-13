pokemon_list = {
    "Bulbasaur" : ["Bulbasaur", "Ivysaur", "Venusaur"],
    "Charmander" : ["Charmander", "Charmeleon", "Charizard"],
    "Squirtle" : ["Squirtle", "Wartortle", "Blastoise"],
    "Caterpie" : ["Caterpie", "Metapod", "Butterfree"],
    "Weedle" : ["Weedle", "Kakuna", "Beedrill"],
    "Pidgey" : ["Pidgey", "Pidgeotto", "Pidgeot"],
    "Rattata" : ["Rattata", "Raticate"],
    "Spearow" : ["Spearow", "Fearow"],
    "Ekans" : ["Ekans", "Arbok"],
    "Sandshrew" : ["Sandshrew", "Sandslash"],
    "Nidoran♀" : ["Nidoran♀", "Nidorina", "Nidoqueen"],
    "Nidoran♂" : ["Nidoran♂", "Nidorino", "Nidoking"],
    "Vulpix" : ["Vulpix", "Ninetales"],
    "Zubat" : ["Zubat", "Golbat", "Crobat"],
    "Oddish" : ["Oddish", "Gloom", ("Vileplume", "Bellossom")],
    "Paras" : ["Paras", "Parasect"],
    "Venonat" : ["Venonat", "Venomoth"],
    "Diglett" : ["Diglett", "Dugtrio"],
    "Meowth" : ["Meowth", "Persian"],
    "Psyduck" : ["Psyduck", "Golduck"],
    "Mankey" : ["Mankey", "Primeape", "Annihilape"],
    "Growlithe" : ["Growlithe", "Arcanine"],
    "Poliwag" : ["Poliwag", "Poliwhirl", ("Poliwrath", "Politoed")],
    "Abra" : ["Abra", "Kadabra", "Alakazam"],
    "Machop" : ["Machop", "Machoke", "Machamp"],
    "Bellsprout" : ["Bellsprout", "Weepinbell", "Victreebel"],
    "Tentacool" : ["Tentacool", "Tentacruel"],
    "Geodude" : ["Geodude", "Graveler", "Golem"],
    "Ponyta" : ["Ponyta", "Rapidash"],
    "Slowpoke" : ["Slowpoke", "Slowbro", "Slowking"],
    "Magnemite" : ["Magnemite", "Magneton", "Magnezone"],
    "Farfetch'd" : ["Farfetch'd", "Sirfetch'd"],
    "Doduo" : ["Doduo", "Dodrio"],
    "Seel" : ["Seel", "Dewgong"],
    "Grimer" : ["Grimer", "Muk"],
    "Shellder" : ["Shellder", "Cloyster"],
    "Gastly" : ["Gastly", "Haunter", "Gengar"],
    "Onix" : ["Onix", "Steelix"],
    "Drowzee" : ["Drowzee", "Hypno"],
    "Krabby" : ["Krabby", "Kingler"],
    "Voltorb" : ["Voltorb", "Electrode"],
    "Exeggcute" : ["Exeggcute", "Exeggutor"],
    "Cubone" : ["Cubone", "Marowak"],
    "Tyrogue" : ["Tyrogue", ("Hitmonlee", "Hitmonchan", "Hitmontop")],
    "Lickitung" : ["Lickitung", "Lickilicky"],
    "Koffing" : ["Koffing", "Weezing"],
    "Rhyhorn" : ["Rhyhorn", "Rhydon", "Rhyperior"],
    "Tangela" : ["Tangela", "Tangrowth"],
    "Kangaskhan" : ["Kangaskhan"],
    "Horsea" : ["Horsea", "Seadra", "Kingdra"],
    "Goldeen" : ["Goldeen", "Seaking"],
    "Staryu" : ["Staryu", "Starmie"],
    "Mime Jr." : ["Mime Jr.", "Mr. Mime", "Mr. Rime"],
    "Scyther" : ["Scyther", "Scizor", "Kleavor"],
    "Smoochum" : ["Smoochum", "Jynx"],
    "Elekid" : ["Elekid", "Electabuzz", "Electivire"],
    "Magby" : ["Magby", "Magmar", "Magmortar"],
    "Pinsir" : ["Pinsir"],
    "Tauros" : ["Tauros"],
    "Magikarp" : ["Magikarp", "Gyarados"],
    "Lapras" : ["Lapras"],
    "Ditto" : ["Ditto"],
    "Eevee" : ["Eevee", ("Vaporeon", "Jolteon", "Flareon", "Espeon", "Umbreon", "Leafeon", "Glaceon", "Sylveon")],
    "Porygon" : ["Porygon", "Porygon2", "Porygon-Z"],
    "Omanyte" : ["Omanyte", "Omastar"],
    "Kabuto" : ["Kabuto", "Kabutops"],
    "Aerodactyl" : ["Aerodactyl"],
    "Snorlax" : ["Munchlax", "Snorlax"],
    "Articuno" : ["Articuno"],
    "Zapdos" : ["Zapdos"],
    "Moltres" : ["Moltres"],
    "Dratini" : ["Dratini", "Dragonair", "Dragonite"],
    "Mewtwo" : ["Mewtwo"],
    "Mew" : ["Mew"],
    "Chikorita" : ["Chikorita", "Bayleef", "Meganium"],
    "Cyndaquil" : ["Cyndaquil", "Quilava", "Typhlosion"],
    "Totodile" : ["Totodile", "Croconaw", "Feraligatr"],
    "Sentret" : ["Sentret", "Furret"],
    "Hoothoot" : ["Hoothoot", "Noctowl"],
    "Ledyba" : ["Ledyba", "Ledian"],
    "Spinarak" : ["Spinarak", "Ariados"],
    "Chinchou" : ["Chinchou", "Lanturn"],
    "Pichu" : ["Pichu", "Pikachu", "Raichu"],
    "Cleffa" : ["Cleffa", "Clefairy", "Clefable"],
    "Igglybuff" : ["Igglybuff", "Jigglypuff", "Wigglytuff"],
    "Togepi" : ["Togepi", "Togetic", "Togekiss"],
    "Natu" : ["Natu", "Xatu"],
    "Mareep" : ["Mareep", "Flaaffy", "Ampharos"],
    "Hoppip" : ["Hoppip", "Skiploom", "Jumpluff"],
    "Aipom" : ["Aipom", "Ambipom"],
    "Sunkern" : ["Sunkern", "Sunflora"],
    "Yanma" : ["Yanma", "Yanmega"],
    "Wooper" : ["Wooper", "Quagsire"],
    "Murkrow" : ["Murkrow", "Honchkrow"],
    "Slowking" : ["Slowpoke", "Slowking"],
    "Misdreavus" : ["Misdreavus", "Mismagius"],
    "Unown" : ["Unown"],
    "Girafarig" : ["Girafarig", "Farigiraf"],
    "Pineco" : ["Pineco", "Forretress"],
    "Dunsparce" : ["Dunsparce", "Dudunsparce"],
    "Gligar" : ["Gligar", "Gliscor"],
    "Snubbull" : ["Snubbull", "Granbull"],
    "Qwilfish" : ["Qwilfish", "Overqwil"],
    "Shuckle" : ["Shuckle"],
    "Heracross" : ["Heracross"],
    "Sneasel" : ["Sneasel", "Weavile"],
    "Teddiursa" : ["Teddiursa", "Ursaring", "Ursaluna"],
    "Slugma" : ["Slugma", "Magcargo"],
    "Swinub" : ["Swinub", "Piloswine", "Mamoswine"],
    "Corsola" : ["Corsola", "Cursola"],
    "Remoraid" : ["Remoraid", "Octillery"],
    "Delibird" : ["Delibird"],
    "Skarmory" : ["Skarmory"],
    "Houndour" : ["Houndour", "Houndoom"],
    "Phanpy" : ["Phanpy", "Donphan"],
    "Stantler" : ["Stantler", "Wyrdeer"],
    "Smeargle" : ["Smeargle"],
    "Smoochum" : ["Smoochum", "Jynx"],
    "Miltank" : ["Miltank"],
    "Raikou" : ["Raikou"],
    "Entei" : ["Entei"],
    "Suicune" : ["Suicune"],
    "Larvitar" : ["Larvitar", "Pupitar", "Tyranitar"],
    "Lugia" : ["Lugia"],
    "Ho-Oh" : ["Ho-Oh"],
    "Celebi" : ["Celebi"],
    "Treecko" : ["Treecko", "Grovyle", "Sceptile"],
    "Torchic" : ["Torchic", "Combusken", "Blaziken"],
    "Mudkip" : ["Mudkip", "Marshtomp", "Swampert"],
    "Poochyena" : ["Poochyena", "Mightyena"],
    "Zigzagoon" : ["Zigzagoon", "Linoone", "Obstagoon"],
    "Wurmple" : ["Wurmple", "Silcoon", "Beautifly"],
    "Wurmple" : ["Wurmple", "Cascoon", "Dustox"],
    "Lotad" : ["Lotad", "Lombre", "Ludicolo"],
    "Seedot" : ["Seedot", "Nuzleaf", "Shiftry"],
    "Taillow" : ["Taillow", "Swellow"],
    "Wingull" : ["Wingull", "Pelipper"],
    "Ralts" : ["Ralts", "Kirlia", ("Gardevoir", "Gallade")],
    "Surskit" : ["Surskit", "Masquerain"],
    "Shroomish" : ["Shroomish", "Breloom"],
    "Slakoth" : ["Slakoth", "Vigoroth", "Slaking"],
    "Nincada" : ["Nincada", ("Ninjask", "Shedinja")],
    "Whismur" : ["Whismur", "Loudred", "Exploud"],
    "Makuhita" : ["Makuhita", "Hariyama"],
    "Azurill" : ["Azurill", "Marill", "Azumarill"],
    "Nosepass" : ["Nosepass", "Probopass"],
    "Skitty" : ["Skitty", "Delcatty"],
    "Sableye" : ["Sableye"],
    "Mawile" : ["Mawile"],
    "Aron" : ["Aron", "Lairon", "Aggron"],
    "Meditite" : ["Meditite", "Medicham"],
    "Electrike" : ["Electrike", "Manectric"],
    "Plusle" : ["Plusle"],
    "Minun" : ["Minun"],
    "Volbeat" : ["Volbeat"],
    "Illumise" : ["Illumise"],
    "Gulpin" : ["Gulpin", "Swalot"],
    "Carvanha" : ["Carvanha", "Sharpedo"],
    "Wailmer" : ["Wailmer", "Wailord"],
    "Numel" : ["Numel", "Camerupt"],
    "Torkoal" : ["Torkoal"],
    "Spoink" : ["Spoink", "Grumpig"],
    "Spinda" : ["Spinda"],
    "Trapinch" : ["Trapinch", "Vibrava", "Flygon"],
    "Cacnea" : ["Cacnea", "Cacturne"],
    "Swablu" : ["Swablu", "Altaria"],
    "Zangoose" : ["Zangoose"],
    "Seviper" : ["Seviper"],
    "Lunatone" : ["Lunatone"],
    "Solrock" : ["Solrock"],
    "Barboach" : ["Barboach", "Whiscash"],
    "Corphish" : ["Corphish", "Crawdaunt"],
    "Baltoy" : ["Baltoy", "Claydol"],
    "Lileep" : ["Lileep", "Cradily"],
    "Anorith" : ["Anorith", "Armaldo"],
    "Feebas" : ["Feebas", "Milotic"],
    "Castform" : ["Castform"],
    "Kecleon" : ["Kecleon"],
    "Shuppet" : ["Shuppet", "Banette"],
    "Duskull" : ["Duskull", "Dusclops", "Dusknoir"],
    "Tropius" : ["Tropius"],
    "Absol" : ["Absol"],
    "Wynaut" : ["Wynaut", "Wobbuffet"],
    "Snorunt" : ["Snorunt", "Glalie", "Froslass"],
    "Spheal" : ["Spheal", "Sealeo", "Walrein"],
    "Clamperl" : ["Clamperl", "Huntail", "Gorebyss"],
    "Relicanth" : ["Relicanth"],
    "Luvdisc" : ["Luvdisc"],
    "Bagon" : ["Bagon", "Shelgon", "Salamence"],
    "Beldum" : ["Beldum", "Metang", "Metagross"],
    "Regirock" : ["Regirock"],
    "Regice" : ["Regice"],
    "Registeel" : ["Registeel"],
    "Latias" : ["Latias"],
    "Latios" : ["Latios"],
    "Kyogre" : ["Kyogre"],
    "Groudon" : ["Groudon"],
    "Rayquaza" : ["Rayquaza"],
    "Jirachi" : ["Jirachi"],
    "Deoxys" : ["Deoxys"],
    "Turtwig" : ["Turtwig", "Grotle", "Torterra"],
    "Chimchar" : ["Chimchar", "Monferno", "Infernape"],
    "Piplup" : ["Piplup", "Prinplup", "Empoleon"],
    "Starly" : ["Starly", "Staravia", "Staraptor"],
    "Bidoof" : ["Bidoof", "Bibarel"],
    "Kricketot" : ["Kricketot", "Kricketune"],
    "Shinx" : ["Shinx", "Luxio", "Luxray"],
    "Budew" : ["Budew", "Roselia", "Roserade"],
    "Cranidos" : ["Cranidos", "Rampardos"],
    "Shieldon" : ["Shieldon", "Bastiodon"],
    "Burmy" : ["Burmy", "Wormadam", "Mothim"],
    "Combee" : ["Combee", "Vespiquen"],
    "Pachirisu" : ["Pachirisu"],
    "Buizel" : ["Buizel", "Floatzel"],
    "Cherubi" : ["Cherubi", "Cherrim"],
    "Shellos" : ["Shellos", "Gastrodon"],
    "Drifloon" : ["Drifloon", "Drifblim"],
    "Buneary" : ["Buneary", "Lopunny"],
    "Glameow" : ["Glameow", "Purugly"],
    "Chingling" : ["Chingling", "Chimecho"],
    "Stunky" : ["Stunky", "Skuntank"],
    "Bronzor" : ["Bronzor", "Bronzong"],
    "Bonsly" : ["Bonsly", "Sudowoodo"],
    "Happiny" : ["Happiny", "Chansey", "Blissey"],
    "Chatot" : ["Chatot"],
    "Spiritomb" : ["Spiritomb"],
    "Gible" : ["Gible", "Gabite", "Garchomp"],
    "Munchlax" : ["Munchlax", "Snorlax"],
    "Riolu" : ["Riolu", "Lucario"],
    "Hippopotas" : ["Hippopotas", "Hippowdon"],
    "Skorupi" : ["Skorupi", "Drapion"],
    "Croagunk" : ["Croagunk", "Toxicroak"],
    "Carnivine" : ["Carnivine"],
    "Finneon" : ["Finneon", "Lumineon"],
    "Mantyke" : ["Mantyke", "Mantine"],
    "Snover" : ["Snover", "Abomasnow"],
    "Lickilicky" : ["Lickitung", "Lickilicky"],
    "Tangrowth" : ["Tangela", "Tangrowth"],
    "Probopass" : ["Nosepass", "Probopass"],
    "Rotom" : ["Rotom"],
    "Uxie" : ["Uxie"],
    "Mesprit" : ["Mesprit"],
    "Azelf" : ["Azelf"],
    "Dialga" : ["Dialga"],
    "Palkia" : ["Palkia"],
    "Heatran" : ["Heatran"],
    "Regigigas" : ["Regigigas"],
    "Giratina" : ["Giratina"],
    "Cresselia" : ["Cresselia"],
    "Phione" : ["Phione"],
    "Manaphy" : ["Manaphy"],
    "Darkrai" : ["Darkrai"],
    "Shaymin" : ["Shaymin"],
    "Arceus" : ["Arceus"],
    "Victini" : ["Victini"],
    "Snivy" : ["Snivy", "Servine", "Serperior"],
    "Tepig" : ["Tepig", "Pignite", "Emboar"],
    "Oshawott" : ["Oshawott", "Dewott", "Samurott"],
    "Patrat" : ["Patrat", "Watchog"],
    "Lillipup" : ["Lillipup", "Herdier", "Stoutland"],
    "Purrloin" : ["Purrloin", "Liepard"],
    "Pansage" : ["Pansage", "Simisage"],
    "Pansear" : ["Pansear", "Simisear"],
    "Panpour" : ["Panpour", "Simipour"],
    "Munna" : ["Munna", "Musharna"],
    "Pidove" : ["Pidove", "Tranquill", "Unfezant"],
    "Blitzle" : ["Blitzle", "Zebstrika"],
    "Roggenrola" : ["Roggenrola", "Boldore", "Gigalith"],
    "Woobat" : ["Woobat", "Swoobat"],
    "Drilbur" : ["Drilbur", "Excadrill"],
    "Audino" : ["Audino"],
    "Timburr" : ["Timburr", "Gurdurr", "Conkeldurr"],
    "Tympole" : ["Tympole", "Palpitoad", "Seismitoad"],
    "Throh" : ["Throh"],
    "Sawk" : ["Sawk"],
    "Sewaddle" : ["Sewaddle", "Swadloon", "Leavanny"],
    "Venipede" : ["Venipede", "Whirlipede", "Scolipede"],
    "Cottonee" : ["Cottonee", "Whimsicott"],
    "Petilil" : ["Petilil", "Lilligant"],
    "Basculin" : ["Basculin"],
    "Sandile" : ["Sandile", "Krokorok", "Krookodile"],
    "Darumaka" : ["Darumaka", "Darmanitan"],
    "Maractus" : ["Maractus"],
    "Dwebble" : ["Dwebble", "Crustle"],
    "Scraggy" : ["Scraggy", "Scrafty"],
    "Sigilyph" : ["Sigilyph"],
    "Yamask" : ["Yamask", "Cofagrigus"],
    "Tirtouga" : ["Tirtouga", "Carracosta"],
    "Archen" : ["Archen", "Archeops"],
    "Trubbish" : ["Trubbish", "Garbodor"],
    "Zorua" : ["Zorua", "Zoroark"],
    "Minccino" : ["Minccino", "Cinccino"],
    "Gothita" : ["Gothita", "Gothorita", "Gothitelle"],
    "Solosis" : ["Solosis", "Duosion", "Reuniclus"],
    "Ducklett" : ["Ducklett", "Swanna"],
    "Vanillite" : ["Vanillite", "Vanillish", "Vanilluxe"],
    "Deerling" : ["Deerling", "Sawsbuck"],
    "Emolga" : ["Emolga"],
    "Karrablast" : ["Karrablast", "Escavalier"],
    "Foongus" : ["Foongus", "Amoonguss"],
    "Frillish" : ["Frillish", "Jellicent"],
    "Alomomola" : ["Alomomola"],
    "Joltik" : ["Joltik", "Galvantula"],
    "Ferroseed" : ["Ferroseed", "Ferrothorn"],
    "Klink" : ["Klink", "Klang", "Klinklang"],
    "Tynamo" : ["Tynamo", "Eelektrik", "Eelektross"],
    "Elgyem" : ["Elgyem", "Beheeyem"],
    "Litwick" : ["Litwick", "Lampent", "Chandelure"],
    "Axew" : ["Axew", "Fraxure", "Haxorus"],
    "Cubchoo" : ["Cubchoo", "Beartic"],
    "Cryogonal" : ["Cryogonal"],
    "Shelmet" : ["Shelmet", "Accelgor"],
    "Stunfisk" : ["Stunfisk"],
    "Mienfoo" : ["Mienfoo", "Mienshao"],
    "Druddigon" : ["Druddigon"],
    "Golett" : ["Golett", "Golurk"],
    "Pawniard" : ["Pawniard", "Bisharp"],
    "Bouffalant" : ["Bouffalant"],
    "Rufflet" : ["Rufflet", "Braviary"],
    "Vullaby" : ["Vullaby", "Mandibuzz"],
    "Heatmor" : ["Heatmor"],
    "Durant" : ["Durant"],
    "Deino" : ["Deino", "Zweilous", "Hydreigon"],
    "Larvesta" : ["Larvesta", "Volcarona"],
    "Cobalion" : ["Cobalion"],
    "Terrakion" : ["Terrakion"],
    "Virizion" : ["Virizion"],
    "Tornadus" : ["Tornadus"],
    "Thundurus" : ["Thundurus"],
    "Reshiram" : ["Reshiram"],
    "Zekrom" : ["Zekrom"],
    "Landorus" : ["Landorus"],
    "Kyurem" : ["Kyurem"],
    "Keldeo" : ["Keldeo"],
    "Meloetta" : ["Meloetta"],
    "Genesect" : ["Genesect"],
    "Chespin" : ["Chespin", "Quilladin", "Chesnaught"],
    "Fennekin" : ["Fennekin", "Braixen", "Delphox"],
    "Froakie" : ["Froakie", "Frogadier", "Greninja"],
    "Bunnelby" : ["Bunnelby", "Diggersby"],
    "Fletchling" : ["Fletchling", "Fletchinder", "Talonflame"],
    "Scatterbug" : ["Scatterbug", "Spewpa", "Vivillon"],
    "Litleo" : ["Litleo", "Pyroar"],
    "Flabébé" : ["Flabébé", "Floette", "Florges"],
    "Skiddo" : ["Skiddo", "Gogoat"],
    "Pancham" : ["Pancham", "Pangoro"],
    "Furfrou" : ["Furfrou"],
    "Espurr" : ["Espurr", "Meowstic"],
    "Honedge" : ["Honedge", "Doublade", "Aegislash"],
    "Spritzee" : ["Spritzee", "Aromatisse"],
    "Swirlix" : ["Swirlix", "Slurpuff"],
    "Inkay" : ["Inkay", "Malamar"],
    "Binacle" : ["Binacle", "Barbaracle"],
    "Skrelp" : ["Skrelp", "Dragalge"],
    "Clauncher" : ["Clauncher", "Clawitzer"],
    "Helioptile" : ["Helioptile", "Heliolisk"],
    "Tyrunt" : ["Tyrunt", "Tyrantrum"],
    "Amaura" : ["Amaura", "Aurorus"],
    "Hawlucha" : ["Hawlucha"],
    "Dedenne" : ["Dedenne"],
    "Carbink" : ["Carbink"],
    "Goomy" : ["Goomy", "Sliggoo", "Goodra"],
    "Klefki" : ["Klefki"],
    "Phantump" : ["Phantump", "Trevenant"],
    "Pumpkaboo" : ["Pumpkaboo", "Gourgeist"],
    "Bergmite" : ["Bergmite", "Avalugg"],
    "Noibat" : ["Noibat", "Noivern"],
    "Xerneas" : ["Xerneas"],
    "Yveltal" : ["Yveltal"],
    "Zygarde" : ["Zygarde"],
    "Diancie" : ["Diancie"],
    "Hoopa" : ["Hoopa"],
    "Volcanion" : ["Volcanion"],
    "Rowlet" : ["Rowlet", "Dartrix", "Decidueye"],
    "Litten" : ["Litten", "Torracat", "Incineroar"],
    "Popplio" : ["Popplio", "Brionne", "Primarina"],
    "Pikipek" : ["Pikipek", "Trumbeak", "Toucannon"],
    "Yungoos" : ["Yungoos", "Gumshoos"],
    "Grubbin" : ["Grubbin", "Charjabug", "Vikavolt"],
    "Crabrawler" : ["Crabrawler", "Crabominable"],
    "Oricorio" : ["Oricorio"],
    "Cutiefly" : ["Cutiefly", "Ribombee"],
    "Rockruff" : ["Rockruff", "Lycanroc"],
    "Wishiwashi" : ["Wishiwashi"],
    "Mareanie" : ["Mareanie", "Toxapex"],
    "Mudbray" : ["Mudbray", "Mudsdale"],
    "Dewpider" : ["Dewpider", "Araquanid"],
    "Fomantis" : ["Fomantis", "Lurantis"],
    "Morelull" : ["Morelull", "Shiinotic"],
    "Salandit" : ["Salandit", "Salazzle"],
    "Stufful" : ["Stufful", "Bewear"],
    "Bounsweet" : ["Bounsweet", "Steenee", "Tsareena"],
    "Comfey" : ["Comfey"],
    "Oranguru" : ["Oranguru"],
    "Passimian" : ["Passimian"],
    "Wimpod" : ["Wimpod", "Golisopod"],
    "Sandygast" : ["Sandygast", "Palossand"],
    "Pyukumuku" : ["Pyukumuku"],
    "Type: Null" : ["Type: Null", "Silvally"],
    "Minior" : ["Minior"],
    "Komala" : ["Komala"],
    "Turtonator" : ["Turtonator"],
    "Togedemaru" : ["Togedemaru"],
    "Mimikyu" : ["Mimikyu"],
    "Bruxish" : ["Bruxish"],
    "Drampa" : ["Drampa"],
    "Dhelmise" : ["Dhelmise"],
    "Jangmo-o" : ["Jangmo-o", "Hakamo-o", "Kommo-o"],
    "Tapu Koko" : ["Tapu Koko"],
    "Tapu Lele" : ["Tapu Lele"],
    "Tapu Bulu" : ["Tapu Bulu"],
    "Tapu Fini" : ["Tapu Fini"],
    "Cosmog" : ["Cosmog", "Cosmoem", ("Solgaleo", "Lunala")],
    "Nihilego" : ["Nihilego"],
    "Buzzwole" : ["Buzzwole"],
    "Pheromosa" : ["Pheromosa"],
    "Xurkitree" : ["Xurkitree"],
    "Celesteela" : ["Celesteela"],
    "Kartana" : ["Kartana"],
    "Guzzlord" : ["Guzzlord"],
    "Necrozma" : ["Necrozma"],
    "Magearna" : ["Magearna"],
    "Marshadow" : ["Marshadow"],
    "Poipole" : ["Poipole", "Naganadel"],
    "Stakataka" : ["Stakataka"],
    "Blacephalon" : ["Blacephalon"],
    "Zeraora" : ["Zeraora"],
    "Meltan" : ["Meltan", "Melmetal"],
    "Grookey" : ["Grookey", "Thwackey", "Rillaboom"],
    "Scorbunny" : ["Scorbunny", "Raboot", "Cinderace"],
    "Sobble" : ["Sobble", "Drizzile", "Inteleon"],
    "Skwovet" : ["Skwovet", "Greedent"],
    "Rookidee" : ["Rookidee", "Corvisquire", "Corviknight"],
    "Blipbug" : ["Blipbug", "Dottler", "Orbeetle"],
    "Nickit" : ["Nickit", "Thievul"],
    "Gossifleur" : ["Gossifleur", "Eldegoss"],
    "Wooloo" : ["Wooloo", "Dubwool"],
    "Chewtle" : ["Chewtle", "Drednaw"],
    "Yamper" : ["Yamper", "Boltund"],
    "Rolycoly" : ["Rolycoly", "Carkol", "Coalossal"],
    "Applin" : ["Applin", "Flapple", "Appletun"],
    "Silicobra" : ["Silicobra", "Sandaconda"],
    "Cramorant" : ["Cramorant"],
    "Arrokuda" : ["Arrokuda", "Barraskewda"],
    "Toxel" : ["Toxel", "Toxtricity"],
    "Sizzlipede" : ["Sizzlipede", "Centiskorch"],
    "Clobbopus" : ["Clobbopus", "Grapploct"],
    "Sinistea" : ["Sinistea", "Polteageist"],
    "Hatenna" : ["Hatenna", "Hattrem", "Hatterene"],
    "Impidimp" : ["Impidimp", "Morgrem", "Grimmsnarl"],
    "Milcery" : ["Milcery", "Alcremie"],
    "Falinks" : ["Falinks"],
    "Pincurchin" : ["Pincurchin"],
    "Snom" : ["Snom", "Frosmoth"],
    "Stonjourner" : ["Stonjourner"],
    "Eiscue" : ["Eiscue"],
    "Indeedee" : ["Indeedee"],
    "Morpeko" : ["Morpeko"],
    "Cufant" : ["Cufant", "Copperajah"],
    "Dracozolt" : ["Dracozolt"],  # Fossil Pokémon
    "Arctozolt" : ["Arctozolt"],  # Fossil Pokémon
    "Dracovish" : ["Dracovish"],  # Fossil Pokémon
    "Arctovish" : ["Arctovish"],  # Fossil Pokémon
    "Duraludon" : ["Duraludon"],
    "Dreepy" : ["Dreepy", "Drakloak", "Dragapult"],
    "Zacian" : ["Zacian"],
    "Zamazenta" : ["Zamazenta"],
    "Eternatus" : ["Eternatus"],
    "Kubfu" : ["Kubfu", "Urshifu"],  # Introduced in The Isle of Armor DLC
    "Zarude" : ["Zarude"],
    "Regieleki" : ["Regieleki"],  # Introduced in The Crown Tundra DLC
    "Regidrago" : ["Regidrago"],  # Introduced in The Crown Tundra DLC
    "Glastrier" : ["Glastrier"],  # Introduced in The Crown Tundra DLC
    "Spectrier" : ["Spectrier"],  # Introduced in The Crown Tundra DLC
    "Calyrex" : ["Calyrex"],
    "Sprigatito" : ["Sprigatito", "Floragato", "Meowscarada"],
    "Fuecoco" : ["Fuecoco", "Crocalor", "Skeledirge"],
    "Quaxly" : ["Quaxly", "Quaxwell", "Quaquaval"],
    "Lechonk" : ["Lechonk", "Oinkologne"],
    "Tarountula" : ["Tarountula", "Spidops"],
    "Nymble" : ["Nymble", "Lokix"],
    "Rellor" : ["Rellor", "Rabsca"],
    "Greavard" : ["Greavard", "Houndstone"],
    "Flittle" : ["Flittle", "Espathra"],
    "Wiglett" : ["Wiglett", "Wugtrio"],
    "Dondozo" : ["Dondozo"],
    "Veluza" : ["Veluza"],
    "Finizen" : ["Finizen", "Palafin"],
    "Smoliv" : ["Smoliv", "Dolliv", "Arboliva"],
    "Capsakid" : ["Capsakid", "Scovillain"],
    "Tadbulb" : ["Tadbulb", "Bellibolt"],
    "Varoom" : ["Varoom", "Revavroom"],
    "Orthworm" : ["Orthworm"],
    "Tandemaus" : ["Tandemaus", "Maushold"],
    "Cetoddle" : ["Cetoddle", "Cetitan"],
    "Frigibax" : ["Frigibax", "Arctibax", "Baxcalibur"],
    "Tatsugiri" : ["Tatsugiri"],
    "Cyclizar" : ["Cyclizar"],
    "Pawmi" : ["Pawmi", "Pawmo", "Pawmot"],
    "Wattrel" : ["Wattrel", "Kilowattrel"],
    "Bombirdier" : ["Bombirdier"],
    "Squawkabilly" : ["Squawkabilly"],
    "Flamigo" : ["Flamigo"],
    "Klawf" : ["Klawf"],
    "Nacli" : ["Nacli", "Naclstack", "Garganacl"],
    "Glimmet" : ["Glimmet", "Glimmora"],
    "Shroodle" : ["Shroodle", "Grafaiai"],
    "Fidough" : ["Fidough", "Dachsbun"],
    "Maschiff" : ["Maschiff", "Mabosstiff"],
    "Bramblin" : ["Bramblin", "Brambleghast"],
    "Gimmighoul" : ["Gimmighoul", "Gholdengo"],
    "Great Tusk" : ["Great Tusk"],
    "Scream Tail" : ["Scream Tail"],
    "Brute Bonnet" : ["Brute Bonnet"],
    "Flutter Mane" : ["Flutter Mane"],
    "Slither Wing" : ["Slither Wing"],
    "Sandy Shocks" : ["Sandy Shocks"],
    "Iron Treads" : ["Iron Treads"],
    "Iron Bundle" : ["Iron Bundle"],
    "Iron Hands" : ["Iron Hands"],
    "Iron Jugulis" : ["Iron Jugulis"],
    "Iron Moth" : ["Iron Moth"],
    "Iron Thorns" : ["Iron Thorns"],
    "Ting-Lu" : ["Ting-Lu"],
    "Chien-Pao" : ["Chien-Pao"],
    "Wo-Chien" : ["Wo-Chien"],
    "Chi-Yu" : ["Chi-Yu"],
    "Roaring Moon" : ["Roaring Moon"],
    "Iron Valiant" : ["Iron Valiant"],
    "Koraidon" : ["Koraidon"],
    "Miraidon" : ["Miraidon"],
    "Ogerpon" : ["Ogerpon"],  # The Teal Mask DLC
    "Okidogi" : ["Okidogi"],  # The Teal Mask DLC
    "Munkidori" : ["Munkidori"],  # The Teal Mask DLC
    "Fezandipiti" : ["Fezandipiti"],  # The Teal Mask DLC
    "Dipplin" : ["Dipplin"],  # The Teal Mask DLC
    "Poltchageist" : ["Poltchageist", "Sinistcha"],  # The Teal Mask DLC
    "Archaludon" : ["Archaludon"],  # The Indigo Disk DLC
    "Raging Bolt" : ["Raging Bolt"],  # The Indigo Disk DLC
    "Iron Crown" : ["Iron Crown"],  # The Indigo Disk DLC
    "Terapagos" : ["Terapagos"]  # The Indigo Disk DLC
}

# pokemon_shapes