# PyProjects
A couple fun projects to work with using Python.
_______________________________________________

<b><i>Cipher.py</i></b> -> This a simple implementation of Caesar's cipher(Shift cipher, Caesar's code or Caesar shift). It's a simple encryption technique based on substitution, each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. There are several possible variations that greatly increase the level on encryption and thus increase the security.

<b><i>PoemFinder.py</i></b> -> This a webscrapping project. It asks what is the topic you want and then searches the website(You can change that) for quotes, poems and more about that topic. After scanning one page it'll ask if the user wants to scan more pages or if one is good enough. In the end, a file will be written with the scanned quotes, texts and poems.

<b><i>WordCloudScrapping</i></b> -> You've probably seen a wordcloud, it's basically an image with the words changing their size based on the frequency they appear in the input text. The code simply scans news headlines from a newspaper I choosed(same webscrapping technique used before) for the number of times specified in the code, after having this information we need to clean the text, otherwise it'd be very polluted with "if"'s, "and"'s etc(I'm scanning a Brazillian journal, if you want to scan something in another language make sure to change the stop words). After cleaning the text up I call a function to make a graph and after that the wordcloud is made(I'm using a mask with the shape of Brazil.)
