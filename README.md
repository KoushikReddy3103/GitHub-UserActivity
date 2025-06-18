# GitHub-UserActivity

This project makes use of GitHub REST API to fetch and display the user activity for the prescribed username. The username is given as an input.

## Getting Started

To setup the project, clone the forked repository on your local
```bash
git clone https://github.com/<username>/GitHub-UserActivity.git
cd GitHub-UserActivity
```

## Installation
For installing all the required packages and dependencies, execute the setenv file
`source setenv`

## Configuration
To store the GitHub REST API key, create a .env file and declare API key as shown below:
```bash
API_KEY=<API KEY>
```

For creating the API key, please refer the documentation given below:
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic

## Usage
```bash
    github-activity <username>
```