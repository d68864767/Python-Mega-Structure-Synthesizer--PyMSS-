# Contributing to Python Mega Structure Synthesizer (PyMSS)

First off, thank you for considering contributing to PyMSS. It's people like you that make PyMSS such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, make sure to check our [Issues](https://github.com/your-username/PyMSS/issues) page to see if someone else in the community has already created a ticket. If not, go ahead and make one!

## Fork & create a branch

If this is something you think you can fix, then fork PyMSS and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```shell
git checkout -b 325-add-japanese-localisation
```

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first.

## Get the code

The first thing you'll need to do is get the PyMSS code. To do this, you'll need to fork the repository.

## Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with PyMSS's master branch:

```shell
git remote add upstream git@github.com:your-username/PyMSS.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master and push it!

```shell
git checkout 325-add-japanese-localisation
git rebase master
git push --set-upstream origin 325-add-japanese-localisation
```

Go to the PyMSS repo and press the "Compare & pull request" button.

## Wait for the review

Once you've submitted a pull request, everyone can see your proposed changes and review them. They can suggest changes, ask questions, or endorse the changes with a nice comment.

## What's next?

Once your pull request is merged, you can delete your branch. Don't worry, the Internet has a copy of your changes, so you won't lose anything!

```shell
git checkout master
git push origin --delete 325-add-japanese-localisation
git branch -d 325-add-japanese-localisation
```

Again, thank you for your contribution!

