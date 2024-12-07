<!--
*********************************************************************************************
* File: index.html
* Author: Madhurima Rawat
* Date: December 07, 2024
* Description: Personal portfolio website for Madhurima Rawat, showcasing education, experience, projects, skills, achievements, and hobbies.
* Version: 1.0
* GitHub Repository: https://github.com/madhurimarawat/Portfolio-Website
* Issues/Bugs: For any issues or bugs, please visit the GitHub repository issues section.
* Comments: This HTML file serves as the main structure for Madhurima Rawat's portfolio. It includes sections such as Objective, Education, Experience, Projects, Skills, Achievements, and Hobbies. It also features a dynamic color-changing dropdown menu using JavaScript.
* Dependencies:
    - Font Awesome 5.15.3: External CSS for icons.
    - Bootstrap 4.5.2: External CSS for responsive design (used in other stylesheets).
    - JavaScript file (index.js): Manages the dynamic color-changing functionality.
    - CSS file (index.css): Contains styles for this portfolio.
* Design Notes:
    - The layout is designed with responsive web design principles in mind, adapting seamlessly to different screen sizes and devices.
    - A central theme of user interaction is incorporated through dynamic color-changing options, adding a personalized touch to the user experience.
    - The social links wheel section includes interactive icons that rotate to highlight different social media profiles, with specific behaviors tailored for various screen sizes and user interactions.
*********************************************************************************************
-->

<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />

    <!-- Bootstrap CSS  CDN-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css"
        integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous" />
    <link rel="stylesheet" href="css/index.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" />
    <link href="https://fonts.googleapis.com/css2?family=Times+New+Roman:wght@400;700&display=swap" rel="stylesheet" />

    <link rel="icon" href="images/Title Logo.png" type="image/jpeg">
    <title>Portfolio Website</title>

</head>

<body>

    <!-- Navigation Bar -->
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark">
        <a class="navbar-brand" href="index.html">
            <img src="images/Programmer Illustration.jpg" width="80" height="80" alt="Logo" loading="eager" />
        </a>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownProfile" role="button"
                        data-toggle="dropdown" aria-expanded="false">
                        Profile
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdownProfile">
                        <a class="dropdown-item" href="#About_me">About Me</a>
                        <a class="dropdown-item" href="#Education">Education</a>
                        <a class="dropdown-item" href="#skills">Skills</a>
                        <a class="dropdown-item" href="#hobbies-and-interests">Hobbies</a>
                        <a class="dropdown-item dev" href="https://madhurima-devfolio.streamlit.app/" target="_blank"
                            rel="noopener noreferrer">Devfolio</a>
                        <a class="dropdown-item" href="#social-links">Socials</a>
                    </div>
                </li>
                <li class="nav-item Experience">
                    <a class="nav-link" href="#experience">Experience</a>
                </li>

                <li class="nav-item Projects">
                    <a class="nav-link" href="#projects">Projects</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link"
                        href="https://drive.google.com/file/d/1EYrjwt8p55lhdj78in0dio0IwTDdsPAL/view?usp=sharing">Resume</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="career-highlights.html">Career Highlights</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#About me" id="navbarDropdown" role="button"
                        data-toggle="dropdown" aria-expanded="false">
                        Theme
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="#" onclick="changeColor('autumn')"><i
                                class="fas fa-leaf"></i>&nbsp;Autumn</a>
                        <a class="dropdown-item" href="#" onclick="changeColor('summer')"><i
                                class="fas fa-sun"></i>&nbspSummer</a>
                        <a class="dropdown-item" href="#" onclick="changeColor('rainy')"><i
                                class="fas fa-cloud-showers-heavy"></i>&nbspRainy</a>
                        <a class="dropdown-item" href="#" onclick="changeColor('winter')"><i
                                class="fas fa-snowflake"></i>&nbspWinter</a>
                    </div>
                </li>

            </ul>

            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="mailto:rawatmadhurima@gmail.com">
                        <i class="fa fa-envelope"></i> Email
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="tel:+9407959924">
                        <i class="fa fa-phone"></i> 9407959924
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://github.com/madhurimarawat" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://linkedin.com/in/madhurima-rawat" target="_blank">
                        <i class="fab fa-linkedin"></i> LinkedIn
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://linktr.ee/madhurima_rawat" target="_blank"><i
                            class="fa fa-link"></i>LinkTree</a>
                </li>
            </ul>
        </div>
    </nav>
    <br />
    <br /><br />

    <!---------------------    Slider Section Starts From Here----------------->

    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        </ol>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="images/Programmer Illustration Infinity Sign.jpg" height="500px" class="d-block w-100"
                    alt="Slider Image 1" />
                <div class="custom-caption heading_1">
                    <h5 class="custom-caption">Welcome to My Portfolio!</h5>
                </div>
            </div>
            <div class="carousel-item">
                <img src="https://miro.medium.com/v2/resize:fit:1400/1*2I6VKSpzBDEdpMiOGIDgFA.jpeg" height="500px"
                    class="d-block w-100" alt="Slider Image 1" />
            </div>
            <div class="carousel-item">
                <img src="images/Frame Image.png" height="500px" class="d-block w-100" alt="Slider Image 1" />
                <div class="custom-caption heading_1">
                    <h5 class="custom-caption">Interests!</h5>
                </div>
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-target="#carouselExampleIndicators" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-target="#carouselExampleIndicators" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </button>
    </div>

    <!---------------------  Slider Section Ends From Here  ----------------->

    <!---------------------  Header  Section Starts From Here  ----------------->
    <section id="About_me">
        <br />
        <p style="text-align: center;">
            <a href="https://git.io/typing-svg" style="text-align: center;">
                <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Passionate+About+Technology"
                    alt="Typing SVG" loading="lazy" />
            </a>
        </p>
        <h1 class="heading">👩‍💻 &nbsp;About Me</h1>
        <br />
        <div class="container">
            <div class="row justify-content-center">
                <!-- Left Column for Photo and Name -->
                <div class="col-md-4 text-center">
                    <!-- Placeholder for Photo -->
                    <div class="photo-container">
                        <img src="images/Profile Image.png" class="rounded-circle" alt="Photo"
                            style="width: 200px; height: 200px" loading="eager" />
                    </div>
                    <div class="name-container">
                        <img src="images/Designed Name.png" width="250px" height="50px" class="responsive-name">
                    </div>
                    <p>
                        <a href="https://git.io/typing-svg">
                            <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Data+Science+Enthusiast+🇮🇳"
                                alt="Typing SVG" loading="lazy" class="responsive-tagline" />
                        </a>
                    </p>
                    <p class="heading_1">
                        With a passion for learning and exploring new horizons, I'm
                        committed to self-improvement, continually expanding my knowledge
                        and skills, both in the world of technology and beyond. As a
                        confident public speaker with strong communication skills and a
                        knack for effective reading and writing, I enjoy sharing insights
                        and connecting with people from diverse backgrounds.
                    </p>
                </div>

                <!-- Right Column for Description -->
                <div class="col-md-8">
                    <ul style="list-style-type: none; padding-left: 0; margin: 0">
                        <li style="margin-bottom: 15px">👋 I’m Madhurima Rawat 🧑‍🎓</li>
                        <li style="margin-bottom: 15px">
                            👀 I’m interested in data structures and programming languages
                        </li>
                        <li style="margin-bottom: 15px">
                            <img src="https://cdn.dribbble.com/users/226424/screenshots/1187861/media/6a76be08e6f01699b9a3bd47bedae88f.gif"
                                height="100" />
                        </li>
                        <li style="margin-bottom: 15px">
                            🏛️ Pursuing B.Tech(Hons.) in Data Science from CSVTU
                            <img src="https://github.com/madhurimarawat/madhurimarawat/assets/105432776/d9fceaeb-aea5-4954-823b-ce90ceb6ef0b"
                                height="35" width="35" />
                        </li>
                        <li style="margin-bottom: 15px">
                            🌱 I’m currently learning Artificial Intelligence 🤖🧠, Data
                            Science 📊📈, and Machine Learning 🛠📚
                        </li>
                        <li style="margin-bottom: 15px">
                            👯 I’m looking to collaborate on Python
                            <img src="https://cdn.freebiesupply.com/logos/large/2x/python-5-logo-png-transparent.png"
                                title="Python" alt="Python Language" width="35" height="35" />
                        </li>
                        <li style="margin-bottom: 15px">
                            💬 Ask me about programming languages 😀
                        </li>
                        <li style="margin-bottom: 15px">
                            📫 How to reach me: &nbsp;
                            <a href="https://www.linkedin.com/in/madhurima-rawat/" target="_blank">
                                <img src="https://img.shields.io/badge/-madhurima-blue?style=flat&logo=Linkedin&logoColor=white"
                                    alt="Linkedin Badge" />
                            </a>
                            &nbsp; &nbsp;
                            <a href="mailto:rawatmadhurima@gmail.com">
                                <img src="https://github.com/madhurimarawat/Machine-Learning-Using-Python/assets/105432776/b6a0873a-e961-42c0-8fbf-ab65828c961a"
                                    title="Mail Illustration" alt="Mail Illustration📫" height="35" width="30" />
                            </a>
                        </li>
                        <li style="margin-bottom: 15px">😄 Pronouns: She/Her.</li>
                        <li style="margin-bottom: 15px">
                            ⚡ Fun fact: In my free time I read stories 📚 and explore
                            new technologies 💻
                        </li>
                        <li style="margin-bottom: 15px">
                            💡 Feel free to share any good story or article resources with
                            me! 📚✨
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    <!---------------------  Header  Section Ends From Here ----------------->

    <!---------------------  Education Section Starts From Here ----------------->

    <section id="Education">
        <br />
        <p style="text-align: center;">
            <a href="https://git.io/typing-svg" style="text-align: center;">
                <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Knowledge+Empowers+the+Future"
                    alt="Typing SVG" loading="lazy" /></a>
        </p>
        <h1 class="heading">🧑‍🎓 &nbsp;Education</h1>
        <br />
        <div class="card">
            <table>
                <tr>
                    <th>Degree/Certificate</th>
                    <th>Institute/Board</th>
                    <th>CGPA</th>
                    <th>Year</th>
                </tr>
                <tr>
                    <td>B.Tech.</td>
                    <td>CSVTU, Bhilai</td>
                    <td>8.23 (Current)/10</td>
                    <td>2021 - Present</td>
                </tr>
                <tr>
                    <td>Senior Secondary</td>
                    <td>CBSE Board</td>
                    <td>First Division</td>
                    <td>2021</td>
                </tr>
                <tr>
                    <td>Secondary</td>
                    <td>CBSE Board</td>
                    <td>Distinction</td>
                    <td>2019</td>
                </tr>
            </table>
        </div>
    </section>

    <!---------------------  Skills Section Starts From Here ----------------->

    <section id="skills">
        <br />
        <p style="text-align: center;">
            <a href="https://git.io/typing-svg" style="text-align: center;">
                <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Diverse+Technical+Skills+Acquired"
                    alt="Typing SVG" loading="lazy" />

            </a>
        </p>
        <div class="languages-and-tools">
            <summary>
                <h1 class="heading">🛠 &nbsp;Languages and Tools</h1>
            </summary>
            <br>
            <p class="heading_1">Click on the icon to see the associated repository.</p>
            <br />

            <details open>
                <summary>📚 &nbsp;Languages :</summary>
                <br />
                <p>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Data-structure-using-C">C</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Object-oriented-programming-with-c-plus-plus">C++</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Analysis-and-Design-of-Algorithm-using-python">Python</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/R-for-Datascience">R</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Website-Frontend-Developement">CSS</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Website-Frontend-Developement">HTML</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Website-Frontend-Developement">JavaScript</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Programming-in-PHP">PHP</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Ruby-Programming">Ruby</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Scratch-Programming">Scratch</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Java-Programming">Java</a>
                </p>
            </details>

            <details open>
                <summary>📑 &nbsp;Frameworks & Libraries :</summary>
                <br />
                <p>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Python-for-Datascience">Numpy</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Python-for-Datascience">Pandas</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Python-for-Datascience">Matplotlib</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Data-Visualization-using-python">Seaborn</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Machine-Learning-Using-Python">Scikit
                        Learn</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Machine-Learning-Using-Python">Mlxtend</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Machine-Learning-Projects-In-Python">Pickle</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Machine-Learning-Projects-In-Python">Joblib</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/R-Projects">ggplot2</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Library-Management-System">Bootstrap</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Natural-Language-Processing-in-Python">NLTK</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Web-Scrapper-Functions">Requests</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Software-Engineering">PyTest</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Software-Engineering">Sphinx</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Software-Engineering">MkDocs</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Software-Engineering">PDoc</a>
                </p>
            </details>

            <details open>
                <summary>💻 &nbsp;Databases :</summary>
                <br />
                <p>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Semester-Notes/tree/main/3%20SEMESTER/Database%20Management%20System">MySQL</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Stock-Market-Prediction">InfluxDB</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Big-Data-Analytics">Hive</a>
                </p>
            </details>

            <details open>
                <summary>🌟 &nbsp;Technology and Tools :</summary>
                <br />
                <p>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Learning-Programming-Concepts-With-C">GCC</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Python-for-Datascience">Jupyter</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Python-for-Datascience">Anaconda</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Data-Visualization-using-python">Google
                        Colab</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/R-for-Datascience">R Studio</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Machine-Learning-Using-Python">PyCharm</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Programming-in-PHP">Visual Studio
                        Code</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Library-Management-System">Notepad++</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Ruby-Programming">Komodo IDE</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Stock-Market-Prediction">Grafana</a>
                    <a class="tool-button"
                        href="https://madhurimarawat.github.io/Semester-Notes/Astyle-Commands.html">Astyle</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Learning-Git">Git</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Learning-GitHub-Actions-CI">GitHub
                        Actions</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Learning-Travis-CI">Travis
                        CI</a>
                    <a class="tool-button"
                        href="https://madhurimarawat.github.io/Semester-Notes/Hadoop-Commands.html">Hadoop</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Big-Data-Analytics">Kafka</a>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Big-Data-Analytics">Spark</a>
                </p>
            </details>

            <details open>
                <summary>🌐 &nbsp;Web Servers :</summary>
                <br />
                <p>
                    <a class="tool-button" href="https://github.com/madhurimarawat/Programming-in-PHP">XAMPP Server</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Machine-Learning-Projects-In-Python">Flask
                        API</a>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/ML-Model-Datasets-Using-Streamlits/tree/main">Streamlit</a>
                </p>
            </details>

            <details open>
                <summary>📊 &nbsp;Web Services :</summary>
                <br />
                <p>
                    <a class="tool-button"
                        href="https://github.com/madhurimarawat/Library-Management-System">Netlify</a>
                </p>
            </details>
        </div>
    </section>

    <!---------------------  Internship Section Starts From Here ----------------->

    <section id="experience">
        <br />
        <p style="text-align: center;">
            <a href="https://git.io/typing-svg" style="text-align: center;">
                <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Hands-on+Experience+Gained"
                    alt="Typing SVG" loading="lazy" />
            </a>
        </p>
        <h1 class="heading">📑🌟 &nbsp; Experience</h1>
        <br /><br />
        <div class="card">
            <table class="experience-table">
                <tr>
                    <th>Company</th>
                    <th>Role</th>
                    <th>Duration</th>
                    <th>Projects and Achievements</th>
                </tr>
                <tr>
                    <td>IIT Roorkee and Diginique Techlabs</td>
                    <td>Student Intern - AI, ML, and DS using Python | <a
                            href="https://github.com/madhurimarawat/Machine-Learning-Using-Python"><i
                                class="fab fa-github"></i>
                            GitHub</a></td>
                    <td>July 2023 - Sep 2023</td>
                    <td>
                        Developed ML model web app for optimizing accuracy with hyperparameter tuning on real-world
                        datasets.
                        Managed GitHub repository for organizing and sharing project codes.
                    </td>
                </tr>
                <tr>
                    <td>Uptricks Services Pvt. Ltd</td>
                    <td>Data Science Intern | <a
                            href="https://github.com/madhurimarawat/Credit-Card-Prediction-Analysis"><i
                                class="fab fa-github"></i> GitHub</a>
                    </td>
                    <td>Feb 2024 - Mar 2024</td>
                    <td>
                        Focused on retail sales forecasting and credit card prediction, demonstrating proficiency in
                        data analysis and predictive modeling. Received a Letter of Recommendation for outstanding
                        performance.
                    </td>
                </tr>
                <tr>
                    <td>Mentorness</td>
                    <td>Machine Learning Intern| <a href="https://github.com/madhurimarawat/Mentorness"><i
                                class="fab fa-github"></i> GitHub</a></td>
                    <td>Mar 2024 - Apr 2024</td>
                    <td>
                        Developed a churn analysis application, conducted World Cup data analysis, and authored an
                        insightful
                        article on hyperparameter tuning techniques.
                    </td>
                </tr>
                <tr>
                    <td>IIT Bhilai</td>
                    <td>Project Intern - Data Science using Python</td>
                    <td>Feb 2024 - June 2024</td>
                    <td>
                        Contributed to the 'BSP Pre-Failure Alert Generation' project by using matrix profiling to
                        discern motifs
                        and
                        discords in time series data of PLC signals, enabling the
                        identification of normal and anomalous patterns with precision. Enhanced Grafana dashboards for
                        more
                        effective
                        visualization of BSP mill server data.
                    </td>
                </tr>
            </table>
        </div>
    </section>

    <!---------------------  Projects Section Starts From Here ----------------->

    <section id="projects">
        <br />
        <p style="text-align: center;">
            <a href="https://git.io/typing-svg" style="text-align: center;">
                <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Discover+Innovative+Projects+Developed"
                    alt="Typing SVG" loading="lazy" />
            </a>
        </p>
        <h1 class="heading">📎📚 &nbsp; Projects</h1>
        <br />
        <p class="heading_1">Click on the Thumbnail to See the Website</p>
        <div class="container mt-4">
            <div class="row">
                <!-- Library Management System Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <a href="https://library-management-website.netlify.app/">
                            <img src="https://5.imimg.com/data5/SELLER/Default/2021/12/UC/BP/KG/52242850/1-4--500x500.jpg"
                                height="200px" class="card-img-top" title="Library Management system website"
                                alt="Library Management system website" loading="lazy" />
                        </a>
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: #ff9aa2">
                                Library Website
                            </h5>
                            <br />
                            <p>
                                <a href="https://library-management-website.netlify.app/"><i
                                        class="fa fa-globe"></i>&nbsp;Website</a>
                                |
                                <a href="https://github.com/madhurimarawat/Library-Management-System"><i
                                        class="fab fa-github"></i>
                                    GitHub</a>
                            </p>

                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Website-Frontend-Developement">CSS</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Website-Frontend-Developement">HTML</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Website-Frontend-Developement">JavaScript</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Library-Management-System">Bootstrap</a>
                            <br /><br />
                            <p class="card-text">
                                Executed frontend development for a Library Management System
                                Website, enhancing book tracking, user management, and overall
                                library experience. Designed a user-friendly interface
                                facilitating efficient processes for librarians and patrons.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- ML Models Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <a href="https://ml-model-datasets-using-apps-3gy37ndiancjo2nmu36sls.streamlit.app/">
                            <img src="https://github.com/user-attachments/assets/5ad5ba7a-8227-4b7d-80a5-d043c2810383"
                                height="200px" class="card-img-top" title="Machine Learning Model Website"
                                alt="Website Image" loading="lazy" />
                        </a>
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: #ff9aa2">HyperTuneML Platform</h5>
                            <br />
                            <p>
                                <a href="https://github.com/madhurimarawat/ML-Model-Datasets-Using-Streamlits"><i
                                        class="fa fa-globe"></i>&nbsp;Website</a>
                                |
                                <a href="https://github.com/madhurimarawat/ML-Model-Datasets-Using-Streamlits"><i
                                        class="fab fa-github"></i> GitHub</a>
                            </p>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Analysis-and-Design-of-Algorithm-using-python">Python</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Machine-Learning-Using-Python">Scikit
                                Learn</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Machine-Learning-Projects-In-Python">Joblib</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/ML-Model-Datasets-Using-Streamlits/tree/main">Streamlit</a>
                            <br /><br />
                            <p class="card-text">
                                Developed HyperTuneML Platform, a comprehensive platform showcasing
                                diverse machine learning models with real-world datasets.
                                Offers practical insights to enhance understanding of
                                predictive analytics, catering to learners at all levels.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Web Scraper Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <a href="https://web-scrapper-functions-h6phqofpkjtaylwyn9uvzf.streamlit.app/">
                            <img src="https://github.com/user-attachments/assets/f935ec1b-b973-49fe-9fae-5fc9340134f1"
                                height="200px" class="card-img-top" title="Web Scrapper website"
                                alt="Web Scrapper website" loading="lazy" />
                        </a>
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: #ff9aa2">Web Scrapper</h5>
                            <br />
                            <p>
                                <a href="https://web-scrapper-functions-h6phqofpkjtaylwyn9uvzf.streamlit.app/"><i
                                        class="fa fa-globe"></i>&nbsp;Website</a>
                                |
                                <a href="https://github.com/madhurimarawat/Web-Scrapper-Functions"><i
                                        class="fab fa-github"></i>
                                    GitHub</a>
                            </p>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Analysis-and-Design-of-Algorithm-using-python">Python</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Web-Scrapper-Functions">Requests</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Web-Scrapper-Functions">bs4</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/ML-Model-Datasets-Using-Streamlits/tree/main">Streamlit</a>
                            <br /><br />
                            <p class="card-text">
                                Developed a Web Scraper Website with versatile functions for
                                efficient data extraction from diverse websites. Showcases
                                commitment to enhancing data accessibility and streamlining
                                information retrieval processes.
                            </p>
                        </div>
                    </div>
                </div>
                <!-- GitHub Repository Lister Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <a href="https://github-repository-topics-lister.netlify.app/">
                            <img src="https://github.com/madhurimarawat/GitHub-Repository-Lister/assets/105432776/8b9cade2-c861-4b88-ab72-1598745f9ce0"
                                height="200px" class="card-img-top" title="Github Repository Lister Website"
                                alt="Github Repository Lister Website" loading="lazy" />
                        </a>
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: #ff9aa2">
                                GitHub Repository Lister
                            </h5>
                            <p>
                                <a href="https://github-repository-topics-lister.netlify.app/"><i
                                        class="fa fa-globe"></i>&nbsp;Website</a>
                                |
                                <a href="https://github.com/madhurimarawat/GitHub-Repository-Lister"><i
                                        class="fab fa-github"></i>
                                    GitHub</a>
                            </p>

                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Website-Frontend-Developement">CSS</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Website-Frontend-Developement">HTML</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Website-Frontend-Developement">JavaScript</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Library-Management-System">Bootstrap</a>
                            <br /><br />
                            <p class="card-text">
                                Created a GitHub Repository Lister Website to simplify the
                                exploration of repository topics, enhancing the user
                                experience by providing a clear, organized display of relevant
                                repositories.
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Next Row Projects -->
            <div class="row">

                <!-- Semester Notes Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <a href="https://madhurimarawat.github.io/Semester-Notes/">
                            <img src="https://github.com/user-attachments/assets/f84acd1e-c09b-40e7-a76a-429359a6c222"
                                height="200px" class="card-img-top" title="Semester Notes Website"
                                alt="Semester Notes Website" loading="lazy" />
                        </a>
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: #ff9aa2">Study Materials</h5>
                            <p>
                                <a href="https://madhurimarawat.github.io/Semester-Notes/"><i
                                        class="fa fa-globe"></i>&nbsp;Website</a>
                                |
                                <a href="https://github.com/madhurimarawat/Semester-Notes"><i class="fab fa-github"></i>
                                    GitHub</a>
                            </p>
                            <a class="tool-button-1" href="https://github.com/madhurimarawat/Semester-Notes">CSS</a>
                            <a class="tool-button-1" href="https://github.com/madhurimarawat/Semester-Notes">HTML</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Semester-Notes">JavaScript</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Semester-Notes">Bootstrap</a>
                            <br /><br />
                            <p class="card-text">
                                Developed a comprehensive Semester Notes Website, offering students
                                easy access to course materials and study resources. Provides a
                                well-organized platform for efficient learning and information
                                retrieval.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- CodeCulture Daily Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <a href="https://github.com/madhurimarawat/CodeCulture-Daily">
                            <img src="https://github.com/user-attachments/assets/a3bfeab0-aa38-47ed-ad07-3a9a7b8906c7"
                                height="200px" class="card-img-top" title="CodeCulture Website"
                                alt="CodeCulture Website" loading="lazy" />
                        </a>
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: #ff9aa2">CodeCulture Daily</h5>
                            <p>
                                <a href="https://madhurimarawat.github.io/CodeCulture-Daily/"><i
                                        class="fa fa-globe"></i>&nbsp;Website</a>
                                |
                                <a href="https://github.com/madhurimarawat/CodeCulture-Daily"><i
                                        class="fab fa-github"></i>
                                    GitHub</a>
                            </p>
                            <a class="tool-button-1" href="https://github.com/madhurimarawat/CodeCulture-Daily">HTML</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/CodeCulture-Daily">GitHub</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/CodeCulture-Daily">Programming</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/CodeCulture-Daily">Bootstrap</a>
                            <br /><br />
                            <p class="card-text">
                                CodeCulture-Daily is a programming challenge repository offering daily problems to boost
                                coding skills. Solutions and
                                explanations are posted at 7 PM, fostering collaborative learning.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Stock Prediction Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <a href="https://github.com/madhurimarawat/Stock-Market-Prediction">
                            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/App_Snapshots/Streamlit_App/App_View_1.png"
                                height="200px" class="card-img-top" title="Stock Market Website"
                                alt="Stock Market Website" loading="lazy" />
                        </a>
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: #ff9aa2">Stock Prediction</h5>
                            <p>
                                <a href="https://stock-market-numerical-text-hybrid-prediction.streamlit.app/"><i
                                        class="fa fa-globe"></i>&nbsp;Website</a>
                                |
                                <a href="https://github.com/madhurimarawat/Stock-Market-Prediction"><i
                                        class="fab fa-github"></i>
                                    GitHub</a>
                            </p>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Stock-Market-Prediction">InfluxDB</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Stock-Market-Prediction">Grafana</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Stock-Market-Prediction">Streamlit</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Stock-Market-Prediction">Scikit-learn</a>
                            <br /><br />
                            <p class="card-text">
                                Developed and led a stock market prediction project using Python, NLP (NLTK, spaCy),
                                machine learning models, Grafana,
                                InfluxDB, and Streamlit for data analysis and visualization.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- NameBlock Designer Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <a href="https://github.com/madhurimarawat/NameBlock-Designer">
                            <img src="https://github.com/madhurimarawat/NameBlock-Designer/raw/main/website_view/Website_Working.gif"
                                height="200px" class="card-img-top" title="NameBlock-Designer Website"
                                alt="NameBlock-Designer Website" loading="lazy" />
                        </a>
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: #ff9aa2">NameBlock Designer</h5>
                            <p>
                                <a href="https://madhurimarawat.github.io/NameBlock-Designer/"><i
                                        class="fa fa-globe"></i>&nbsp;Website</a>
                                |
                                <a href="https://github.com/madhurimarawat/NameBlock-Designer"><i
                                        class="fab fa-github"></i>
                                    GitHub</a>
                            </p>
                            <a class="tool-button-1" href="https://github.com/madhurimarawat/Semester-Notes">CSS</a>
                            <a class="tool-button-1" href="https://github.com/madhurimarawat/Semester-Notes">HTML</a>
                            <a class="tool-button-1"
                                href="https://github.com/madhurimarawat/Semester-Notes">JavaScript</a>
                            <a class="tool-button-1" href="https://github.com/madhurimarawat/Semester-Notes">GitHub</a>
                            <br /><br />
                            <p class="card-text">
                                NameBlock-Designer is a web-based tool for creating personalized name blocks with
                                customizable colors and dynamic
                                themes. Users can download their designs as images, and the tool is fully responsive,
                                providing a seamless experience on
                                all devices.
                            </p>
                        </div>
                    </div>
                </div>


            </div>
        </div>
    </section>

    <!---------------------  Social Links Section Starts From Here ----------------->

    <section id="social-links">
        <br />
        <p style="text-align: center;">
            <a href="https://git.io/typing-svg" style="text-align: center;">
                <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Engage+Connect+and+Interact"
                    alt="Typing SVG" loading="lazy" /></a>
        </p>
        <h1 class="heading">📲 &nbsp;Socials</h1>
        <br />
        <div class="wheel card">
            <div class="center">
                <a href="#" target="_blank">
                    <img src="https://ouch-cdn2.icons8.com/7t1OP99ujxbijKLclt_j8lXv5sNR8Ob4utsa-QRFnf0/rs:fit:435:456/extend:false/wm:1:re:0:0:0.8/wmid:ouch/czM6Ly9pY29uczgu/b3VjaC1wcm9kLmFz/c2V0cy9zdmcvMTA0/L2RjMWUzN2RiLWM1/NzctNGY0Mi05ZWFj/LWVkMWRlYjJkMDAw/Yy5zdmc.png"
                        alt="Central Icon" title="Central Title">
                </a>
            </div>

            <div class="links">
                <a href="https://github.com/madhurimarawat" class="link" target="_blank" title="GitHub Profile"
                    alt="GitHub Profile"><img src="https://framerusercontent.com/images/J5QUYOJqIOxJSHHEl1IaS6Rb9S4.png"
                        title="GitHub Profile" alt="GitHub Profile"></a>
                <a href="https://madhurimarawat.github.io/Portfolio-Website/" class="link" target="_blank"
                    title="Portfolio Website" alt="Portfolio Website"><img
                        src="https://cdn.dribbble.com/users/1125518/screenshots/3597500/portfolio-icon_1x.png"
                        title="Portfolio Website" alt="Portfolio Website"></a>
                <a href="https://madhurima-devfolio.streamlit.app/" class="link" target="_blank" title="Devfolio"
                    alt="Devfolio"><img
                        src="https://cdn0.iconfinder.com/data/icons/editorial-darkmode/24/editorial_html-1024.png"
                        title="Devfolio" alt="Devfolio"></a>
                <a href="https://www.hackerrank.com/rawatmadhurima4" class="link" target="_blank"
                    title="Hackerrank Profile" alt="Hackerrank Profile"><img
                        src="https://cdn-1.webcatalog.io/catalog/hackerrank/hackerrank-icon.png"
                        title="Hackerrank Profile" alt="Hackerrank Logo"></a>
                <a href="https://www.linkedin.com/in/madhurima-rawat/" class="link" target="_blank"
                    title=" LinkedIn Profile" alt=" LinkedIn Logo"><img
                        src="https://www.freepnglogos.com/uploads/linkedin-blue-style-logo-png-0.png"
                        title=" LinkedIn Profile" alt=" LinkedIn Logo"></a>
                <a href="https://linktr.ee/madhurima_rawat" class="link" target="_blank" title="Link Tree Profile"
                    alt="Link Tree Logo"><img
                        src="https://seeklogo.com/images/L/linktree-logo-6FC3ADB679-seeklogo.com.png"
                        title="Link Tree Profile" alt="Link Tree Logo"></a>
                <a href="https://alison.com/profile/31860447" class="link" target="_blank" title='Alison Profile'
                    alt="Alison Logo"><img src="https://www.mooclab.club/showcase/alison.50/cover-image"
                        title='Alison Profile' alt="Alison Logo"></a>
                <a href="https://x.com/madhurima_47524" class="link" target="_blank" title="Twitter Profile"
                    alt="Twitter Logo"><img
                        src="https://th.bing.com/th/id/R.400dc88500c0bc5e11f6c953dedcc7ab?rik=%2fYNxOHw13exE1w&riu=http%3a%2f%2fpluspng.com%2fimg-png%2ftwitter-logo-png-twitter-logo-vector-png-clipart-library-518.png&ehk=NSZ3BC%2bUR7ur49WE4nPi5f91hxYL4r1kJXJlHeDMYik%3d&risl=&pid=ImgRaw&r=0"
                        title="Twitter Profile" alt="Twitter Logo"></a>
                <a href="https://www.facebook.com/profile.php?id=100077348301764" class="link" target="_blank"
                    title="Facebook Profile" alt="Facebook Logo"><img
                        src="https://images.vexels.com/media/users/3/223136/isolated/preview/984f500cf9de4519b02b354346eb72e0-facebook-icon-social-media-by-vexels.png"
                        title="Facebook Profile" alt="Facebook Logo"></a>
                <a href="https://instagram.com/madhurima8487" class="link" target="_blank" title="Instagram Profile"
                    alt="Instagram Logo"><img
                        src="https://th.bing.com/th/id/OIP.2spOcwGpwKFSn-ZDDhdeIgAAAA?rs=1&pid=ImgDetMain"
                        title="Instagram Profile" alt="Instagram Logo"></a>
            </div>
        </div>
    </section>

    <!---------------------  Hobbies and Interests Section Starts From Here ----------------->
    <section id="hobbies-and-interests">
        <br>
        <p style="text-align: center;">
            <a href="https://git.io/typing-svg" style="text-align: center;">
                <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=My+World+of+Interests"
                    alt="Typing SVG" loading="lazy" />
            </a>
        </p>

        <h1 class="heading">✨ &nbsp; Hobbies and Interests</h1>
        <div class="container mt-4">
            <div class="row">
                <!-- AI Arts Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <img src="https://i.pinimg.com/originals/67/c9/e5/67c9e57e96086000be0d3170be657ea1.jpg"
                            class="card-img-top" title="AI Art Illustration" alt="AI Art Illustration" height="250px"
                            width="100%" loading="lazy" />
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: orange">AI Arts 🖌️💻</h5>
                            <br>
                            <p class="card-text">“A machine’s perspective on the world.”</p>
                        </div>
                    </div>
                </div>
                <!-- Literature Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <img src="https://cdn.pixabay.com/photo/2018/09/06/16/53/book-3658687_1280.jpg"
                            class="card-img-top" title="Girl With book and Butterfly" alt="Girl With book and Butterfly"
                            height="250px" width="100%" loading="lazy" />
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: orange">Literature 📚📖</h5>
                            <br>
                            <p class="card-text">“A good book is an event in life.”</p>
                        </div>
                    </div>
                </div>
                <!-- Music Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <img src="https://yt3.googleusercontent.com/11LyoUnat70TioSwHPUOHk_cwJ7TTWci8AFOaXQ9J6gdtzChMquw4TqnioKYxlrrjVLMSlgmIA=s900-c-k-c0x00ffffff-no-rj"
                            class="card-img-top" title="Music-vector-Feature Illustration"
                            alt="Music-vector-Feature Illustration" loading="lazy" height="250px" width="100%" />
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: orange">Music 🎼🎵</h5>
                            <br>
                            <p class="card-text">
                                “Music is to Heart what Medicine is to Body.”
                            </p>
                        </div>
                    </div>
                </div>
                <!-- Nature Photography Card -->
                <div class="col-md-3">
                    <div class="card mb-4">
                        <img src="https://th.bing.com/th/id/OIP.UClnWD6Moakuq8jQh3nEiAHaFj?pid=ImgDet&rs=1"
                            class="card-img-top" title="Nature Photography Illustration"
                            alt="Nature Photography Illustration" height="250px" width="100%" loading="lazy" />
                        <div class="card-body heading_1">
                            <h5 class="card-title" style="color: orange">
                                Nature Photography 📸🏞️
                            </h5>
                            <p class="card-text">
                                “Nature always wears the colors of the spirit.”
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <br />
    <br />

    <!-- Thank You section -->

    <section id="thank-you" style="text-align: center; padding: 20px; background-color: #f1f1f1" class="heading_1">
        <h2 class="heading_1">Thank You</h2>
        <p>
            Thank you for visiting my portfolio. If you have any questions or would
            like to get in touch, please feel free to contact me.
        </p>


        <!-- Contact Links -->
        <div class="contact heading_1" style="text-align: center; padding: 10px;color: white;">
            <a href="mailto:rawatmadhurima@gmail.com" style="color: black"><i class="fas fa-envelope"></i> Email</a>
            <a class="nav-link" href="tel:+9407959924" style="color: black"><i class="fa fa-phone"></i> 9407959924</a>
            <a href="https://github.com/madhurimarawat" style="color: black"><i class="fab fa-github"></i> GitHub</a>
            &nbsp;
            &nbsp;
            <a href="https://www.linkedin.com/in/madhurima-rawat/" style="color: black"><i class="fab fa-linkedin"></i>
                LinkedIn</a> &nbsp;
            <a href="https://linktr.ee/madhurima_rawat" target="_blank" style="color: black"><i class="fa fa-link"></i>
                LinkTree</a> &nbsp;
            <a href="index.htm" style="color: black"><i class="fas fa-globe"></i> Portfolio</a>&nbsp;
            <a href="https://madhurima-devfolio.streamlit.app/" style="color: black"><i class="fas fa-code"></i>
                Devfolio</a>

        </div>
        <a class="tool-button-2" href="https://github.com/madhurimarawat/Portfolio-Website">Visit on GitHub &nbsp;<i
                class="fab fa-github"></i></a>
    </section>
    <!-- Footer -->
    <footer class="footer-section">
        &copy; 2024 Madhurima Rawat. All rights reserved.
    </footer>
</body>

<!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"
    integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
    crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF"
    crossorigin="anonymous"></script>
<script src="js/index.js"></script>
<!-- jQuery first, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

</html>
