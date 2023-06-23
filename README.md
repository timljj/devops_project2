# devops_project2
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
![image info](./static/app_flow.png)

Image Captioning Flow
![image info](./static/image_captioning_flow.png)

<!-- USAGE EXAMPLES -->
## Usage


Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_


<!-- ROADMAP -->
## Roadmap

- [DONE] Add Webhook Call from GitHub to Discord 
- [ONGOING] Add GitHub Actions
    - [ONGOING] Pylint
    - [ONGOING] Docker
    - [ONGOING] Google Cloud Run
- [DONE] Add Flask App
- [DONE] Add Image Captioning Model to Flask App
- [ONGOING] Caption Image from URL
  - [ONGOING] Display Image
  - [DONE] Display Caption
- [DONE] Caption Image from File Upload
