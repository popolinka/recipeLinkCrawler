filenames = ['food52_links.txt', 'allRecipes_links.txt', 'chefKoch_Links.txt', 'lecker_Links.txt']

with open('/Users/orkunkadioglu/PycharmProjects/recipeLinkCrawler/recipeLinks.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
