# Dev.to Automated Blog Posting using OpenAI & GitHub Actions

This project automates daily/ weekly blog posts on [Dev.to](https://dev.to/) by generating unique, AI-powered content using OpenAI's ChatGPT. It utilizes GitHub Actions to schedule and automate the publishing process, requiring minimal manual effort once set up.

## Overview

With this workflow:
- A cron job triggers the GitHub Actions workflow to generate and publish a new blog post daily/ weekly.
- The blog topics are generated randomly, but they can also follow specific themes based on preferences set in the script.
- This setup leverages the Dev.to API for publishing and the OpenAI API for content generation.

## Features

- **Automated Content Generation**: Uses OpenAI's language model to create engaging blog posts.
- **Scheduled Publishing**: GitHub Actions triggers the post generation and publishing process daily/weekly at a set time.
- **Customizable Topics**: Choose to provide a set of topics or let the script generate random front-end tech topics.
- **Hands-Free Publishing**: Publish directly to Dev.to without manual intervention.

## Getting Started

### Prerequisites

- **Dev.to API Key**: Generate an API key from your Dev.to [account settings](https://dev.to/settings/account).
- **OpenAI API Key**: Get an API key from the [OpenAI API](https://platform.openai.com/).
- **GitHub Repository**: Store your code and manage the workflow.
