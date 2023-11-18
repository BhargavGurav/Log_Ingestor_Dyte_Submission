<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/bhargav-gurav-380992224/)



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/BhargavGurav/Log_Ingestor_Dyte_Submission">
     <img src="LOG_29710.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Log Ingestor</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/BhargavGurav/Log_Ingestor_Dyte_Submission"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="[https://github.com/github_username/repo_name](https://github.com/BhargavGurav/Log_Ingestor_Dyte_Submission)">View Demo</a>
    ·
    <a href="[https://github.com/github_username/repo_name](https://github.com/BhargavGurav/Log_Ingestor_Dyte_Submission)/issues">Report Bug</a>
    ·
    <a href="[https://github.com/github_username/repo_name](https://github.com/BhargavGurav/Log_Ingestor_Dyte_Submission)/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot](https://github.com/BhargavGurav/Log_Ingestor_Dyte_Submission/blob/main/Screenshot%20(252).png)
This Django project is designed to ingest and manage logs of the following format:
```
{
	"level": "error",
	"message": "Failed to connect to DB",
    "resourceId": "server-1234",
	"timestamp": "2023-09-15T08:00:00Z",
	"traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
        "parentResourceId": "server-0987"
    }
}

```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Django][djangoproject.com]](https://www.djangoproject.com/)
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

1. Python (3.x)
2. Pip (Python package manager)


### Installation

1. Clone the repo
   ```
   git clone https://github.com/BhargavGurav/Log_Ingestor_Dyte_Submission.git
   ```
2. Create a virtual environment:
   ```
   python -m venv env
   ```
3. Activate the virtual environment:
  On Windows:
   ```
   .\env\Scripts\activate
   ```

On macOS and Linux:
```
source env/bin/activate
```

4. Install dependencies from requirements.txt:
```
pip install -r requirements.txt
```

5. Apply migrations to set up the database:
```
python manage.py makemigrations
python manage.py migrate
```

6. Start the development server:
```
python manage.py runserver
```

Access the Django admin panel at http://localhost:3000/admin/ to manage logs.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project provides an endpoint to ingest logs of the specified JSON format. Logs can be ingested via HTTP POST requests to the designated endpoint. Ensure the provided JSON log payload matches the specified format for successful ingestion.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Bhargav Gurav - [Email me](guravbhargav09@gmail.com)

Project Link: [Github](https://github.com/BhargavGurav/Log_Ingestor_Dyte_Submission)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/BhargavGurav/Log_Ingestor_Dyte_Submission.svg?style=for-the-badge
[contributors-url]: https://github.com/BhargavGurav

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username


[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[djangoproject.com]: https://img.shields.io/badge/Django-1d3b0c?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
