import json

from src.models import Author, Quote
from src.db import connect


with open("authors.json", "r", encoding="utf-8") as fh:
    result_author = json.load(fh)

with open("quotes.json", "r", encoding="utf-8") as fh:
    result_quotes = json.load(fh)


for author in result_author:
    author_to_add = Author(fullname=author.get("fullname"), born_date=author.get("born_date"), \
                           born_location=author.get("born_location"), description=author.get("description")).save()
    for quote in result_quotes:

        if quote.get("author") == author.get("fullname"):
            quote_for_add = Quote(tags=quote.get("tags"), author=author_to_add, quote=quote.get("quote")).save()


# Quote.objects().delete()
# Author.objects().delete()
