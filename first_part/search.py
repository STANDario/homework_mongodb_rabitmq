from src.models import Author, Quote
from src.db import connect


while True:

    input_ = input("-->")

    if input_ == "exit":
        print("Good bye :)")
        break

    user_input = input_.split(":")
    action = user_input[0]

    try:
        name_or_tag = user_input[1].strip()
        tags = name_or_tag.split(",")
    except IndexError as e:
        print("Write please 'name:...' or 'tag:...' or 'tags:...,...' or 'exit'")
        continue

    authors = Author.objects()
    quotes = Quote.objects()

    if action == "name":

        for author in authors:
            if author.to_mongo().to_dict().get("fullname") == name_or_tag:
                for quote in quotes:
                    if author.to_mongo().to_dict().get("_id") == quote.to_mongo().to_dict().get("author"):
                        print(quote.to_mongo().to_dict().get("quote"))

    elif action == "tag" or action == "tags":
        for quote in quotes:
            len_tag = len(tags)
            count_tag = 0
            for tag in tags:
                if tag in quote.to_mongo().to_dict().get("tags"):
                    count_tag += 1
            if count_tag == len_tag:
                print(quote.to_mongo().to_dict().get("quote"))
