import random

def Joke():
    number = random.randint(0,25)
    jokes = [
    {"joke":"What does Santa suffer from if he gets stuck in a chimney?",
    "response":"Claustrophobia!"
    },
    {"joke":"What do they sing at a snowman's birthday party?",
    "response":"Freeze a jolly good fellow"
    },
    {"joke":"Why does Santa have three gardens?",
    "response":"So he can 'ho ho ho'!"
    },
    {"joke":"What does Miley Cyrus have at Christmas?",
    "response":"Twerky!"
    },
    {"joke":"What do vampires sing on New Year's Eve?",
    "response":"Auld Fang Syne"
    },
    {"joke":"Why did Santa's helper see the doctor?",
    "response":"Because he had low 'elf' esteem"
    },
    {"joke":"What happened to the man who stole an Advent Calendar?",
    "response":"He got 24 days!"
    },
    {"joke":"What kind of motorbike does Santa ride?",
    "response":"A Holly Davidson!"
    },
    {"joke":"What do you get if you cross Santa with a duck?",
    "response":"A Christmas Quacker!"
    },
    {"joke":"What is the best Christmas present in the world?",
    "response":"A broken drum, you just can't beat it!"
    },
    {"joke":"Who delivers presents to baby sharks at Christmas?",
    "response":"Santa Jaws"
    },
    {"joke":"Who is Santa's favorite singer?",
    "response":"Elf-is Presley!"
    },
    {"joke":"What do Santa's little helpers learn at school?",
    "response":"The elf-abet!"
    },
    {"joke":"What did Santa say to the smoker?",
    "response":"Please don't smoke, it's bad for my elf!"
    },
    {"joke":"What do reindeer hang on their Christmas trees?",
    "response":"Horn-aments!"
    },
    {"joke":"Why are Christmas trees so bad at sewing?",
    "response":"They always drop their needles!"
    },
    {"joke":"Did Rudolph go to school?",
    "response":"No. He was Elf-taught!"
    },
    {"joke":"Why did the turkey join the band?",
    "response":"Because it had the drumsticks!"
    },

    {"joke":"What do you get when you cross a snowman with a vampire?",
    "response":"Frostbite!"
    },
    {"joke":"What do snowmen wear on their heads?",
    "response":"Ice Caps!"
    },
    {"joke":"How do snowmen get around?",
    "response":"They ride an icicle!"
    },
    {"joke":"How does Good King Wenceslas like his pizzas?",
    "response":"One that's deep pan, crisp and even!"
    },
    {"joke":"What do you call a cat in the desert?",
    "response":"Sandy Claws!"
    },
    {"joke":"What did Adam say to his wife on the day before Christmas?",
    "response":"It's christmas, Eve!"
    },
    {"joke":"What carol is heard in the desert?",
    "response":"O camel ye faithful!"
    },
    {"joke":"What do angry mice send to each other at Christmas?",
    "response":"Cross Mouse Cards!"
    },
    ]
    return jokes[number]

def Trivia():
    number = random.randint(0,13)
    trivia = [
    {"trivia":"US President Franklin Pierce introduced what to White House Christmas tradition in 1856?",
    "response":"The Christmas tree"
    },
        {"trivia":"What is the chemical formula of snow?",
        "response":"H20"
        },
            {"trivia":"Which charity in 1949 was the first to produce a Christmas card?",
            "response":"UNICEF"
            },
                {"trivia":"What red-blooming Christmas plant came originally from Mexico?",
                "response":"The Poinsettia"
                },
                    {"trivia":"Brandy is made from distilling what?",
                    "response":"Wine"
                    },
                        {"trivia":"White Christmas, a cake made of coconut, crisped rice and dried fruit, is popular in which country?",
                        "response":"Australia"
                        },
                            {"trivia":"Who is the narrator in the 2000 film The Grinch Who Stole Christmas?",
                            "response":"Anthony Hopkins"
                            },
                                {"trivia":"Pine needles are said to be a good source of which vitamin?",
                                "response":"Vitamin C"
                                },
                                    {"trivia":"In which Christmas carol does this line feature: 'Bring me flesh, and bring me wine, bring me pine logs hither'",
                                    "response":"Good King Wenceslas"
                                    },
                                        {"trivia":"What is the birth sign of people born on 25 December?",
                                        "response":"Capricorn"
                                        },
                                            {"trivia":"What was the title of the first Christmas TV special Peanuts cartoon? (For a bonus, what year did it debut?)",
                                            "response":"A Charlie Brown Christmas (1965)"
                                            },
                                                {"trivia":"Which two states in the US have towns called Christmas?",
                                                "response":"Arizona and Florida"
                                                },
                                                    {"trivia":"Which hugely popular actor was born on Christmas day 1899?",
                                                    "response":"Humphrey Bogart"
                                                    },
                                                        {"trivia":"La Befana is the legendary character who delivers Christmas presents to children in which country?",
                                                        "response":"Italy"
                                                        },
    ]
    return trivia[number]
