import json

def get_data(file_path):
  with open(file_path, 'r') as f:
    return json.load(f)

def main():
  top_data = get_data('top.json')
  antibots_data = get_data('antibots.json')

  for user_id, user_data in top_data.items():
    for friend_id, friend_data in user_data.items():
      if friend_id in antibots_data:
        if antibots_data[friend_id]['onoff'] == 'On':
          print(f"User {user_id} is friends with {friend_id}, who has antibots enabled.")

if __name__ == "__main__":
  main()
