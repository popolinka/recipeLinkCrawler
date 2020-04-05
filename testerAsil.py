import requests
import time

url = "https://api.dev.kitchenstories.io/api"

"""
Login with a user
"""

# urlAuthenticate = url + "/api/authenticate/"
# email = "orkun.kadioglu+1@kitchenstories.de"
# password = "testtest"
#
# payload = "{\n\t\"email\": \"{{username}}\",\n\t\"password\": \"{{password}}\"\n}".format(email, password)
headers = {
    'Content-Type': 'application/json'
}
#
# #payload = "{\n\t\"email\": \"orkun.kadioglu+1@kitchenstories.de\",\n\t\"password\": \"testtest\"\n}"
#
# response = requests.request("POST", urlAuthenticate, headers=headers, data=payload)
# json_data = json.loads(response.text)
#
# token = json_data['access_token']

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1bHRyb24iLCJ1c2VyIjoiNGUwMmQ2NDAtMWZhYS00MTZmLWIyYTAtZmJjMWU1MDI2NDJkIn0.C9ZIXK2gYg4XxNBnNIkcnaOOq7N46r11uKycoUy17Fg"
# get it from Postman

headers['Authorization'] = "Bearer {}".format(token)  # "Bearer" redundant
headers['Accept-language'] = "en"

'''
get external recipes
'''

urlExternalRecipe = url + "/users/me/external-recipe-preview/?url={}"

with open('/Users/orkunkadioglu/PycharmProjects/recipeLinkCrawler/recipeLinks.txt') as file_in:
    # with open('/Users/orkunkadioglu/PycharmProjects/recipeLinkCrawler/kochBar_links.txt') as file_in:
    # with open('/Users/orkunkadioglu/PycharmProjects/recipeLinkCrawler/xinshipu_links.txt') as file_in:
    lines = []
    for line in file_in:
        lines.append(line)

notParsebleRecipes = []
for count, x in enumerate(lines):
    # print(x)
    r = requests.get(urlExternalRecipe.format(x), headers=headers)
    # print(r.json())
    # print(type(r.json()))
    # print(urlExternalRecipe.format(x))
    # print(r.json())
    if "errors" in r.json():
        message = " | the error is: {}".format(r.json()["errors"])
        notParsebleRecipes.append(x[:len(x) - 1] + message)  # + "the error is: " + r.json["errors"])

    if (count + 1) % 10 == 0:  # enumerate starts counting from 0
        print(str(count + 1) + " out of " + str(len(lines)) + " are complete")
    time.sleep(0.7)
    # print("last recipe was " + x + " at " + str(count + 1))

with open('notParsableRecipeLinks.txt', 'w+') as f:
    for recipes in notParsebleRecipes:
        f.write('%s\n' % recipes)
