import argparse
from .useractivity import get_user_activity, display_event_summary

def cli():
    parser = argparse.ArgumentParser(description="GitHub User Activity")
    parser.add_argument("username", help="Github username")
    args = parser.parse_args()
    # Function call to perform the api request
    user_events = get_user_activity(args.username)
    display_event_summary(user_events)

if __name__ == "__main__":
    cli()