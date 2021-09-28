# jmorjsm.github.io
- [jmorjsm.github.io](#jmorjsmgithubio)
  - [Overview](#overview)
  - [Running locally](#running-locally)
  - [Updating github-pages gem](#updating-github-pages-gem)

## Overview

This project is a github-pages project using jekyll to power [my personal website](https://jonmorgan.dev/).

I've added a readme so I don't have to re-learn how to setup ruby and jekyll to run this site locally when I next need to update a dependency manually 🥱

## Running locally
- Install Ruby, then bundler, as documented [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll#prerequisites).
- Run `bundle install`
- Run `bundle exec jekyll serve`
- Navigate to http://localhost:4000

## Updating github-pages gem
Occasionally it's required to manually bump the version of the `github-pages` gem.

The version currenlty used by github-pages can be found [here](https://pages.github.com/versions/).

This can be upgraded by manually editing the version specified in the gemfile, or by following the steps documented [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll#updating-the-github-pages-gem).
