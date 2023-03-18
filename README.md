# GPT-3.5-Turbo Git Commit
Automatically generate meaningful commit messages using ChatGPT for your Git repositories.

## Overview
gpt-3.5-turbo-git-commit is a simple and effective tool that leverages the power of OpenAI's ChatGPT to generate relevant commit messages for your code changes. Save time and effort while maintaining clear and informative commit logs.

## Features
<!-- Create a list in MD -->
- Automatically generates commit messages based on your code changes
- Leverages the power of OpenAI's ChatGPT
- Integrates seamlessly with your Git workflow
- Easy to set up and use

Usage
-----
1. Install the package
```
cp .git.example/hooks/prepare-commit-msg .git/hooks/prepare-commit-msg
chmod +x .git/hooks/prepare-commit-msg
```

2. Update your prepare-commit-msg with your API key
3. Commit your changes
```
git commit -m "Blah blah blah"
```
4. Enjoy your rewritten high quality GPT commit message!
