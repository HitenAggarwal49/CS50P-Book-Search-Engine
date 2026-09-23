# BOOK RESEARCHER
### Video Demo:  <https://youtu.be/KOxN-0_KS2Y>

#### Description:

    This project is called Book Researcher. I can talk a lot about this project but let's keep this short.
    ##### Purpose:
    The purpose of this project is to search for books. This is not the only functionality it offers, however. You can search for books, search for works by an author and even get a book recommendation.

###### Search:
    The purpose of this function is to search for a book that the user inputs. There's many ways this could be done but I chose to do it with APIs, which we were taught how to use in the 5th lecture of CS50P. We retrieve the title of the book the user wants to search for. For retrieving any information by the user case insensitively, I had further defined a function called get_response() which will make its experience in the later features as well. What get_response() does is that it takes the user's input, verifies that the user has actually inputted something and turns everything into lower case. The choice of lowercasing was based on the API which will be using shortly.
    After retrieving the title, we pass the title into a function called special_string(), which takes two arguments. The purpose of this function is take input and convert that input into the special forms the API's query require. special_string("the silent patient", "+") will output "the+silent+patient". This is the syntax in which the API accepts a book query.
    Here comes the use of API. I chose to use the openlibrary API because of convenience. I had first made this program using openlibrary, then switched to googlebooks and finally realised that openlibrary was more convenient to use and had direct results.
    We send in a request for the special title to openlibrary and after scouring for results, we display the one with the most editions because that usually is proportional to popularity as the openlibrary API iteself doesn't have a popularity filter, which the googlebooks API does have.
    Title, Authors and the Release year of the book is then shown. Optionally ratings are also shown if we are able to find them. This was a delibrate design choice to not show ratings if we cannot find them because ratings do exist but the API may only optionally contain them and so I thought it would be better to just hide them if they are not present.

###### Recommend:
    The purpose of this function is to recommend a list of books to the user based on the genre the user likes. I chose to recommend on the basis of genre because if I recommend books from some random genre, the user may not like that genre. You don't expect a Fantasy lover to enjoy a Science Fiction book to the same extent. The program then basically displays the top 10 books in that genre. These are already sorted by openlibrary in terms of quality and relevance so I did not have to sort them myself.

###### View Author:
    The purpose of this function is to search for an Author. This displays the biography of the author and the works done by the author. I chose to make the biography part optional with reasons very similar to why I chose to make the ratings of books in search() optional. Openlibrary does not always provide the biography. You may notice that this part of the program is coded differently compared to the rest. This is because biography, if provided by the API, can be of either of 2 types. It can be returned as a string which is the bio or it could be a dict which has a key called value which is what further contains the bio.
    Next come the works by the author. This just displays all of the works the Author has created or participated in.


### Other Information for CS50P Project and My Experience:
    It took me longer to code "test_project" as I had to learn how to mock testing while also writing the code. This was necessary as my functions give an output instead of returning a value so the simple assert statements were not valid.

    Another choice I would like to talk about is which I chose to wrote "we" at some places in this README and the project itself. This was just because it sounded more professional to the user that a team worked on this project even though the entire team consisted of 1 person.

    Anyways, it was really fun for me to undertake this project. I am sure it could have been bigger in scale but I chose to only use the main functionality offered by the API.
    This was CS50.
