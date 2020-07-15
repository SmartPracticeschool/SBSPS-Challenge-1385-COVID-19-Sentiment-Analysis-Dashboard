# IBM Hack Challenge 2020
# COVID-19-Sentiment-Analysis-Dashboard

![Mockup](https://github.com/SmartPracticeschool/SBSPS-Challenge-1385-COVID-19-Sentiment-Analysis-Dashboard/blob/master/Images/mkp-1.png)


## Team: Bruteforce
An Auto-Updating Dynamic Covid-19 Sentiment Analysis Dashboard made using Django. Please visit here: [https://c19dashboard.eu-gb.mybluemix.net/](https://c19dashboard.eu-gb.mybluemix.net/)

## Table Of Contents:
- [Important Links For Judges](#important-links-for-judges)
- [About](#about)
- [Usage](#usage)
- [Features](#features)
- [Setup / Building Locally](#setup-/-building-locally)
- [Team Members](#team-members)

## Important Links For Judges:
- [Website Link](https://c19dashboard.eu-gb.mybluemix.net/)
- [YouTube Video Presentation Link](https://www.youtube.com/watch?v=YXsMKCpl7xA)
- [Project Report Link](https://github.com/SmartPracticeschool/SBSPS-Challenge-1385-COVID-19-Sentiment-Analysis-Dashboard/blob/master/Project-Report-Covid-19-Sentiment-Analysis-Dashboard-Team-Bruteforce.pdf)
- [Source Code](https://github.com/SmartPracticeschool/SBSPS-Challenge-1385-COVID-19-Sentiment-Analysis-Dashboard/tree/master/C19Dashboard)

## About:
- A dynamic auto-updating dashboard, monitoring tweets made with hashtags such as #indialockdown, #Covid19, #IndiaFightsCOVID19.
- The web application has the facility to provide Real-time visualizations for sentiments of the general public towards multiple topics such as 'Lockdown', 'Covid-19', 'UnlockIndia' and will not be limited to above topics.
- Sentiments such as Positive, Neutral and Negative are provided. The tweets are further classified into following categories:
  - Joy
  - Fear
  - Sadness
  - Analytical
  - Anger
  - Confident
- Real-time Trends of Sentiments over time, Most used Hashtags and distribution of Sentiments across India are displayed using intuitive visualizations.
- Real-time Covid-19 cases count with line charts and twitter feed by relevant handles are also displayed.
- On-demand sentiment analysis and twitter timelines of twitter handles are also displayed.
- The web application is developed using the Django Web Framework.
## Usage:

### General Page

Get instant live feed of sentiments across country towards topics related to the Covid-19 Pandemic.

![Live Feed and Pie Chart](https://github.com/SmartPracticeschool/SBSPS-Challenge-1385-COVID-19-Sentiment-Analysis-Dashboard/blob/master/Images/General-Page-crop.png)

Get the distribution of sentiments across states of India.

![India-Map distribution](https://github.com/SmartPracticeschool/SBSPS-Challenge-1385-COVID-19-Sentiment-Analysis-Dashboard/blob/master/Images/General-Page-Crop-2.jpg)

### Sentiment Graphs Page

Get the trends of distribution of sentiments over time.

![Sentiment-graph-page](https://github.com/SmartPracticeschool/SBSPS-Challenge-1385-COVID-19-Sentiment-Analysis-Dashboard/blob/master/Images/Sentiment-Graphs-Page.png)

### Covid 19 Updates Page

Get the latest count of Covid-19 cases, deaths, recovered and active patients.

![Cov19-page-1](https://github.com/SmartPracticeschool/SBSPS-Challenge-1385-COVID-19-Sentiment-Analysis-Dashboard/blob/master/Images/Covid-19-updates-Page.png)

Get state-wise count of Covid-19 cases.

![Cov19-page-2](https://github.com/SmartPracticeschool/SBSPS-Challenge-1385-COVID-19-Sentiment-Analysis-Dashboard/blob/master/Images/Covid-19-updates-Page-1.png.jpg)

### Tweet Analysis page

Get the sentiment analysis of the last 100 tweets by any twitter handle instantly.

![tweet-analysis-gif](https://github.com/SmartPracticeschool/SBSPS-Challenge-1385-COVID-19-Sentiment-Analysis-Dashboard/blob/master/Images/feature.gif)

## Features:

- Django-based backend
    - [Django](https://www.djangoproject.com/)
    - Python 3.6 or later
    
- Frontend app(webapp) with HTML, JavaScript and CSS
    - Responsive UI with [Bootstrap](https://getbootstrap.com/)
    - [Chart.js](https://www.chartjs.org/) and [HighCharts](https://www.highcharts.com/) for charts and graphs.
    
- Data Analysis Tools used
  - [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/)
  - [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)
  - [Watson Tone Analyser](https://www.ibm.com/watson/services/tone-analyzer/)
  
- Deployment
    - [IBM Cloud](https://www.ibm.com/in-en/cloud)
    - [Docker](https://www.docker.com/) integration

## Setup / Building Locally :

To clone the project: 
```bash
git clone https://github.com/SmartPracticeschool/SBSPS-Challenge-1385-COVID-19-Sentiment-Analysis-Dashboard.git
```
From your project root, you can download the project dependencies with:

```bash
pipenv install
```

To run your application locally:

```bash
python manage.py start
```

#### IBM Cloud Developer Tools

Install [IBM Cloud Developer Tools](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started) on your machine by running the following command:
```
curl -sL https://ibm.biz/idt-installer | bash
```

Create an application on IBM Cloud by running:

```bash
ibmcloud dev create
```

This will create and download a starter application with the necessary files needed for local development and deployment.

Your application will be compiled with Docker containers. To compile and run your app, run:

```bash
ibmcloud dev build
ibmcloud dev run
```
