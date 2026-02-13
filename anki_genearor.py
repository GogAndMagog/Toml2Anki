import html

import genanki
import markdown
import re
import unicodedata
import hashlib

from picture_loader import PictureHandler

class DeckGenerator:

    @staticmethod
    def get_deck_model() -> genanki.model.Model:
        model_name = 'Spimple Model'
        model_id = DeckGenerator.__stable_id(model_name)
        return genanki.Model(
            model_id,
            model_name,
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

    @staticmethod
    # Генерирует десятизначный ID для имени
    def __stable_id(name: str) -> int:
        return int(hashlib.sha1(name.encode("utf-8")).hexdigest(), 16) % (10 ** 10)

    @staticmethod
    def __replace_figure_tag(text_data: str) -> str:
        pattern = re.compile(r'\{\{<\s*figure\s+[^>]*src="([^"]+)"[^>]*>\}\}')
        return pattern.sub(r'<img src="\1"/>', text_data)

    @staticmethod
    def __upload_images(destination: str, text_data: str):
        DeckGenerator.__replace_figure_tag(text_data)
        pattern = r'<img[^>]+src=["\']([^"\']+)["\']'
        matches = re.findall(pattern, text_data)
        for match in matches:
            PictureHandler.download_picture_from_internet(destination, match)

    @staticmethod
    def generate_deck(destination: str, raw_data: dict):

        items = raw_data['items']
        model = DeckGenerator.get_deck_model()

        deck_name = raw_data['section'].get('title')
        deck_id = DeckGenerator.__stable_id(deck_name)
        deck = genanki.Deck(deck_id, deck_name)

        for item in items:
            question = html.escape(item['question'])
            answer = html.escape(DeckGenerator.__replace_figure_tag(item['answer']))

            # Переводим из markdown-разметки в HTML
            html_tmp_answer = markdown.markdown(answer, extensions=['markdown.extensions.tables'])
            # Т.к. мы заменяли тэг картинки на <img/>, перевод из markdown преобразовал < и > в &lt; и &gt; соответственно
            # Необходимо преобразовать это обратно, для этого вызывается unescape(), при сохранении Anki-колоды могут возникнуть
            # предупреждения
            html_answer = html.unescape(html_tmp_answer)

            DeckGenerator.__upload_images(destination, html_answer)

            note = genanki.Note(model=model,
                                fields=[question, html_answer], )
            deck.add_note(note)

        # Нормализуем путь, нужно для корректного отображения имени колоды, в разеных ОС
        normalized_destination = unicodedata.normalize("NFC", f'{destination}\\{deck_name}.apkg')

        genanki.Package(deck).write_to_file(normalized_destination)
