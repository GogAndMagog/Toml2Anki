import html

import genanki
import markdown
import re

from picture_loader import download_picture

def generate_test_deck():
    model = genanki.Model(
        1607392319,
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
    )

    deck = genanki.Deck(
        2059400110,
        'My Deck'
    )

    note = genanki.Note(
        model=model,
        fields=['Что такое Python?', 'Язык программирования']
    )

    deck.add_note(note)

    genanki.Package(deck).write_to_file('my_deck.apkg')

def get_deck_model() -> genanki.model.Model:
   return genanki.Model(
        1607392319,
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
    )

def replace_figure_tag(text_data: str):
    pattern = re.compile(r'\{\{<\s*figure\s+[^>]*src="([^"]+)"[^>]*>\}\}')
    return pattern.sub(r'<img src="\1"/>', text_data)

def check_for_images(text_data: str):
    replace_figure_tag(text_data)
    pattern = r'<img[^>]+src=["\']([^"\']+)["\']'
    matches = re.findall(pattern, text_data)
    for match in matches:
        download_picture(match, )

def generate_deck(raw_data: dict):

    items = raw_data['items']
    model = get_deck_model()

    deck_name = raw_data['section'].get('title')
    deck = genanki.Deck(2059400110, deck_name)

    for item in items:
        question = html.escape(item['question'])
        answer = html.escape(replace_figure_tag(item['answer']))
        html_answer = html.unescape(markdown.markdown(answer, extensions=['markdown.extensions.tables']))
        note = genanki.Note(model=model,
                            fields=[question, html_answer],)
        deck.add_note(note)

    genanki.Package(deck).write_to_file(f'{deck_name}.apkg')