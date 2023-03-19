import json

with open('savehere.json') as user_file:
  parsed_json = json.load(user_file)

print(parsed_json)