import argparse


def main():
    parser = argparse.ArgumentParser(description="GitHub User Activity")
    parser.add_argument("USERNAME", help="Github username")
    args = parser.parse_args()



if __name__ == "__main__":
    main()