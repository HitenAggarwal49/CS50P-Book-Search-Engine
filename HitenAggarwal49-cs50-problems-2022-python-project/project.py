# =============
# BOOK RESEARCHER
# =============
# Project title ^^^
# Name- Hiten Aggarwal
# Github Username - HitenAggarwal49
# Edx Username - HitenAggarwal49
# I live in the city of Patiala, in Punjab, India
# Today's Date - 13th August, 2025



# This is a project to give you book recommendations and lets you search for them as well!



import requests
from re import split as sp


def main():
    while True:
        Task = get_task()
        match Task:
            case "search":
                search()
            case "recommend by genre":
                recommend_by_genre()
            case "view author":
                view_author()
            case "exit":
                print("Thank you for using our services!")
                break
            case _:
                pass


def get_response(phrase):

    while True:
        try:
            response = input(phrase).strip().lower()
        except (AttributeError, TypeError):
            print("Try Again!")
        else:
            break

    print("\n")

    return response


def special_string(args, var):

    args = sp(r"\W+", args)
    argument = None
    for arg in args:
        if (argument is not None) and arg:
            argument = argument + var + arg
        else:
            argument = arg
    return argument


def get_task():

    task = get_response(
        "\n     What would you like to do?\n \n"
        "Enter 'view author' to view works by a specific author\n"
        "Enter 'recommend by genre' to get recommendations in a specific genre\n"
        "Enter 'search' to search for a specific work\n"
        "Enter 'exit' to exit \n \n"
        ""
    )

    if task not in ["view author", "search", "recommend by genre", "exit"]:
        print("Wrong Choice! Try Again.")

    return task


def search():

    title = get_response("\n \nWhat book would you like to search?\n")
    special_title = special_string(title, "+")
    result = requests.get(
        f"https://openlibrary.org/search.json?title={special_title}"
    ).json()
    if not result["docs"]:
        print("Could not find Book")
        return
    sorted_result = sorted(
        result["docs"], key=lambda count: count.get("edition_count", 0), reverse=True
    )
    top_result = sorted_result[0]
    key = top_result["key"]

    print(f"Result: {top_result.get('title', title.title())}")
    print(f"Author(s): ", *top_result.get("author_name", ["Could not find"]))
    print(f"Release: {top_result.get('first_publish_year','Could not find')}")

    ratings = requests.get(f"https://openlibrary.org{key}/ratings.json").json()
    if ratings:
        ratings = ratings.get("summary", None)
        if ratings:
            ratings = ratings.get("average", None)
            if ratings:
                print(f"Ratings: {ratings:.2f} out of 5")


def recommend_by_genre():

    subject = get_response("\n \nWhat genre would you like to explore?\n")
    special_subject = special_string(subject, "_")
    result = requests.get(
        f"https://openlibrary.org/subjects/{special_subject}.json?details=true"
    ).json()
    works = result.get("works", None)

    if not works:
        print("No work found in genre! Try again!")
        return

    for work in works[:10]:
        print(work.get("title"))


def view_author():

    author = get_response("\n \nWho would you like to view?\n")
    special_author = special_string(author, "%20")
    result = requests.get(
        f"https://openlibrary.org/search/authors.json?q={special_author}"
    ).json()
    if not result["docs"]:
        print("Could not find Author")
        return

    author_key = result.get("docs", [{}])[0]
    if author_key:
        author_key = author_key.get("key", None)

    if not author_key:
        print("\nCould not find author")
        return

    print(f"\nAuthor: {author.title()}")

    bio = (
        requests.get(f"https://openlibrary.org/authors/{author_key}.json")
        .json()
        .get("bio", None)
    )
    if type(bio) == dict:
        bio = bio.get("value", None)
    if bio:
        print(bio)

    works = (
        requests.get(f"https://openlibrary.org/authors/{author_key}/works.json")
        .json()
        .get("entries", None)
    )
    if works:
        print("Works: \n")
        for work in works:
            if work["title"]:
                print(work["title"])


if __name__ == "__main__":
    main()
