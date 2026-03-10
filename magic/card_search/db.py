import json
from card_search.models import (SetId,SetCode,SetName,Rarity,Color,
                                ColorIdentity,Keywords,ManaCostColor,
                                Type,ReleasedAt,Name,Card)

all_keys_to_remove = [
"games",
"all_parts",
"arena_id",
"artist",
"artist_ids",
"attraction_lights",
"booster",
"border_color",
"card_faces",
"collector_number",
"content_warning",
"digital",
"edhrec_rank",
"finishes",
"flavor_name",
"flavor_text",
"foil",
"frame",
"frame_effects",
"full_art",
"game_changer",
"hand_modifier",
"highres_image",
"illustration_id",
"image_status",
"layout",
"life_modifier",
"loyalty",
"mtgo_foil_id",
"mtgo_id",
"multiverse_ids",
"nonfoil",
"object",
"oversized",
"penny_rank",
"preview",
"prices",
"prints_search_uri",
"produced_mana",
"promo",
"promo_types",
"purchase_uris",
"related_uris",
"reprint",
"reserved",
"resource_id",
"rulings_uri",
"scryfall_set_uri",
"scryfall_uri",
"security_stamp",
"set_search_uri",
"set_type",
"set_uri",
"story_spotlight",
"tcgplayer_etched_id",
"textless",
"uri",
"variation",
"variation_of",
"watermark",
"card_back_id",
"printed_name",
"printed_text",
"printed_type_line",
"color_indicator",
]
cards = None
try:
    with open("all_cards.json","r",encoding='utf-8') as file:
        cards = json.load(file)
        print(type(cards))
        for card in cards:
            for key in all_keys_to_remove:
                try:
                    card.pop(key)
                except:
                    continue
        # print(type(cards))
except FileNotFoundError:
    print("not such file")
except json.JSONDecodeError:
    print("Json error")
keys_left = [
"released_at",
"cardmarket_id",
"oracle_text",
"legalities",#need to split this up
"power",
"oracle_id",
"defense",
"toughness",
"mana_cost",#need to split this up
"image_uris",
"id",
"tcgplayer_id",
"cmc",
"set_id",#start other models
"rarity",
"keywords",
"set_name",
"color_identity",
"name",
"type_line",
"colors",
"set",
]

english_cards = []
for c in cards:
    if c['lang'] == 'en':
        english_cards.append(c)

for c in english_cards:
    c.pop('lang')


for c in english_cards:
    new_card = Card.objects.create()
    try:
        scryfall_id = c["id"]
        new_card.scryfall_id = scryfall_id
        new_card.save()
        print("SCRYLFALL_ID SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")
    try:
        oracle_id = c["oracle_id"]
        new_card.oracle_id = oracle_id
        new_card.save()
        print("ORACLE_ID SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")
    # try:
    #     tcgplayer_id = c["tcgplayer_id"]
    #     new_card.tcgplayer_id = tcgplayer_id
    #     new_card.save()
    # except Exception as e:
    #     print(f"An error occured: {e} card_id:{c['id']}")
    # try:
    #     cardmarket_id = c["cardmarket_id"]
    #     new_card.cardmarket_id = cardmarket_id
    #     new_card.save()
    # except Exception as e:
    #     print(f"An error occured: {e} card_id:{c['id']}")
    try:
        image_uri = c["image_uris"]["normal"]
        new_card.image_uri = image_uri
        new_card.save()
        print("IMAGE_URI SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")
    try:
        cmc = c["cmc"]
        new_card.cmc = cmc
        new_card.save()
        print("CMC SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")
    try:
        oracle_text = c["oracle_text"]
        new_card.oracle_text = oracle_text
        new_card.save()
        print("ORACLE_TEXT SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        new_thing,created = SetId.objects.get_or_create(set_id=c['set_id'])
        new_card.set_id = new_thing
        new_card.save()
        print("SET_ID SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        new_thing,created = SetCode.objects.get_or_create(set_code=c['set'])
        new_card.set_code = new_thing
        new_card.save()
        print("SET_CODE SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        new_thing,created = SetName.objects.get_or_create(set_name=c['set_name'])
        new_card.set_name = new_thing
        new_card.save()
        print("SET_NAME SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        new_thing,created = Rarity.objects.get_or_create(rarity=c['rarity'])
        new_card.rarity = new_thing
        new_card.save()
        print("RARITY SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        new_thing,created = Type.objects.get_or_create(type=c['type_line'])
        new_card.type = new_thing
        new_card.save()
        print("TYPE SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        new_thing,created = ReleasedAt.objects.get_or_create(release_date=c['released_at'])
        new_card.released_at = new_thing
        new_card.save()
        print("RELEASED SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        new_thing,created = Name.objects.get_or_create(name=c["name"])
        new_card.name = new_thing
        new_card.save()
        print("NAME SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        for color in c['colors']:
            new_thing,created = Color.objects.get_or_create(symbol=color)
            new_card.colors.add(new_thing)
        print("COLOR SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        for color in c['color_identity']:
            new_thing,created = ColorIdentity.objects.get_or_create(symbol=color)
            new_card.color_identity.add(new_thing)
            print("COLOR_IDENTITY SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        for k in c['keywords']:
            new_thing,created = Keywords.objects.get_or_create(keyword=k)
            new_card.keywords.add(new_thing)
            print("KEYWORD SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        commander_legal = c['legalities']['commander']
        if commander_legal == 'legal':
            new_card.commander_legal = True
        else:
            new_card.commander_legal = False
        new_card.save()
        print("COMMANDER_LEGAL SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    try:
        standard_legal = c['legalities']['standard']
        if standard_legal == 'legal':
            new_card.standard_legal = True
        else:
            new_card.standard_legal = False
        new_card.save()
        print("STANDARD_LEGAL SUCCUSS")
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")

    

    try:
        mana_cost = c['mana_cost']
        if '/' not in mana_cost:
            mana_cost_color_dict = {}
            mana_cost = mana_cost.replace("}","")
            mana_cost = mana_cost.replace("{","")
            mana_cost = mana_cost[::-1]
            count = 0 #getting the numerical manacost by subtracting the mana cost color from the cmc
            for char in mana_cost:
                if char in ['U','R','B','G','W']:
                    mana_cost_color_dict[char] = mana_cost_color_dict.setdefault(char,0)+1

                    count += 1
            for key,value in mana_cost_color_dict.items():
                if value == 0:
                    continue
                else:
                    new_thing,created = ManaCostColor.objects.get_or_create(symbol=key,quantity=value)
                    new_card.mana_cost_color.add(new_thing)
            new_card.mana_cost_numeric = new_card.cmc - count
    except Exception as e:
        print(f"An error occured: {e} card_id:{c['id']}")