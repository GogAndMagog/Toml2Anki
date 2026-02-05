import html

import genanki
import markdown
import re

from picture_loader import PictureHandler

class DeckGenerator:

    @staticmethod
    def get_deck_model() -> genanki.model.Model:
        return genanki.Model(
            1607392319,
            'Simple Model',
            fields=[
                # {'name': 'Id'},
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

    @staticmethod
    def replace_figure_tag(text_data: str) -> str:
        pattern = re.compile(r'\{\{<\s*figure\s+[^>]*src="([^"]+)"[^>]*>\}\}')
        return pattern.sub(r'<img src="\1"/>', text_data)

    @staticmethod
    def upload_images(destination: str, text_data: str):
        DeckGenerator.replace_figure_tag(text_data)
        pattern = r'<img[^>]+src=["\']([^"\']+)["\']'
        matches = re.findall(pattern, text_data)
        for match in matches:
            PictureHandler.download_picture_from_internet(destination, match)

    @staticmethod
    def generate_deck(destination: str, raw_data: dict):

        items = raw_data['items']
        model = DeckGenerator.get_deck_model()

        deck_name = raw_data['section'].get('title')
        deck = genanki.Deck(2059400110, deck_name)

        for item in items:
            identifier = item['id']
            question = html.escape(item['question'])
            answer = html.escape(DeckGenerator.replace_figure_tag(item['answer']))

            html_answer = html.unescape(markdown.markdown(answer, extensions=['markdown.extensions.tables']))
            DeckGenerator.upload_images(destination, html_answer)

            note = genanki.Note(model=model,
                                fields=[question, html_answer], )
            deck.add_note(note)

        genanki.Package(deck).write_to_file(f'{destination}\\{deck_name}.apkg')
