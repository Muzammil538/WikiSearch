import wikipedia as wp

query = input(" What would you like to search ? :\n")
if query != "":
    # print (wp.summary("Wikipedia"))
    wp.search(query)
    result = wp.page(query)
    line = wp.summary(query, sentences=1)
    print(line)
    print(result.url)

else:
    print("Not found")