import wikipedia
x = input("Enter Search Query:: ")
query = wikipedia.page(x)
print(query.summary) # you can get your options for more tabs by simply writing query. and you will get the list of tabs