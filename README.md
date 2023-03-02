# Shoostarter Project

Welcome to the capstone-project-shootstarter wiki! This is a small project which is a clone of Kickstarter website, I worked on this as a proof for all my knowledge and experiences that I gained at AppAcademy.

Deployed Live Link: https://shootstarter.onrender.com

## Major Feature
- There are 2 major features right now which have full CRUD (Create, Read, Update, Delete) in this project:
  - Projects
  - Backing projects and reward (Pledges)
  - Comments

## Future Feature
- These are list of future feature that are coming:
  - Payment Methods
  - Likes
  - Search
  - User Profile

## Techonology
All technologies I used in this project are:
  - Backend: Python, Flask Server
  - Frontend: JavaScript, React, Redux, HTML, CSS 

## Landing Page
![image](https://user-images.githubusercontent.com/112263162/222582314-b688344a-864e-43de-b1d8-47b05d3117e1.png)


## Project Detail Page
![image](https://user-images.githubusercontent.com/112263162/222581942-eca53d3b-9e6b-4316-b3de-ea7b83f5e088.png)
![image](https://user-images.githubusercontent.com/112263162/222575339-37fd30b0-2387-4e72-8c13-6605ade47bb3.png)



## Getting started
1. Clone this repository (only this branch)

2. Install dependencies

      ```bash
      pipenv install -r requirements.txt
      ```

3. Create a **.env** file based on the example with proper settings for your
   development environment

4. Make sure the SQLite3 database connection URL is in the **.env** file

5. This starter organizes all tables inside the `flask_schema` schema, defined
   by the `SCHEMA` environment variable.  Replace the value for
   `SCHEMA` with a unique name, **making sure you use the snake_case
   convention**.

6. Get into your pipenv, migrate your database, seed your database, and run your Flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

7. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.


Contact Info: nednguyen1110@gmail.com
