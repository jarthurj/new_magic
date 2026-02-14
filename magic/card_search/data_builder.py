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
"set_id",
"color_indicator",
"rarity",
"keywords",
"oracle_text",
"set_name",
"color_identity",
"legalities",
"lang",
"power",
"oracle_id",
"name",
"defense",
"toughness",
"type_line",
"colors",
"mana_cost",
"set",
"image_uris",
"id",
"tcgplayer_id",
"cmc",]

english_cards = []
for c in cards:
    if c['lang'] == 'en':
        english_cards.append(c)


"released_at",
"cardmarket_id",
"set_id",
"color_indicator",
"rarity",
"keywords",
"oracle_text",
"set_name",
"color_identity",
"legalities",
"lang",
"power",
"oracle_id",
"name",
"defense",
"toughness",
"type_line",
"colors",
"mana_cost",
"set",
"image_uris",
"id",
"tcgplayer_id",
"cmc"



