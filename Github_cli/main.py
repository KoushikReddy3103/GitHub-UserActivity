import argparse
import json
from useractivity import get_user_activity

def main():
    parser = argparse.ArgumentParser(description="GitHub User Activity")
    parser.add_argument("username", help="Github username")
    args = parser.parse_args()
    # Function call to perform the api request
    user_activity = json.loads(get_user_activity(args.username))
    

if __name__ == "__main__":
    main()