# Dev Ops Project 2
Simple Repo to Explore DevOps workflow


<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#illustrations">Illustrations</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


A simple image captioning web app that allows you to caption images from a URL or a file upload. 

This project attempts to utilise various GitHub Action Workflows like Pylint, Dockerization and Deployment to Google Cloud.



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Set up conda environment
* Create conda environment
  ```sh
  conda create --name <env_name> python=<python_version>
  ```
  * Python Version >= 3.8
* Activate conda environment
  ```sh
  conda activate <env_name>
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/timljj/devops_project2.git
   ```
3. Install python packages
   ```sh
   pip install -r requirements.txt
   ```

<!-- Diagrams to Illustrate How the App Works -->
## Illustrations

App Flow
![image info](https://github.com/timljj/devops_project2/blob/main/static/app_flow.PNG)

Image Captioning Flow
![image info](https://github.com/timljj/devops_project2/blob/main/static/image_captioning_flow.PNG)

<!-- USAGE EXAMPLES -->
## Usage

* Caption Image From URL
  
  ![image info](https://github.com/timljj/devops_project2/blob/main/static/front_page.PNG)
  
  
  ![image info](https://github.com/timljj/devops_project2/blob/main/static/caption_from_url.PNG)


  ![image info](https://github.com/timljj/devops_project2/blob/main/static/caption_url_result.PNG)

<!-- ROADMAP -->
## Roadmap

- [DONE] Add Webhook Call from GitHub to Discord 
- [ONGOING] Add GitHub Actions
    - [ONGOING] Pylint
    - [ONGOING] Docker
    - [ONGOING] Google Cloud Run
- [DONE] Add Flask App
- [DONE] Add Image Captioning Model to Flask App
- [DONE] Caption Image from URL
  - [DONE] Display Image
  - [DONE] Display Caption
- [DONE] Caption Image from File Upload
