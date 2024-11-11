# Importing Streamlit
import streamlit as st

# To show Font Awesome icons
css_example = """                                                                                                                                                    
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">   """


# Function for Displaying Objectives and about me
def display_objective():
    st.markdown(
        """
                <p style = "text-align:center"> 
                <a href="https://git.io/typing-svg">
              <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Data+Science+Enthusiast+🇮🇳"
                alt="Typing SVG" loading="lazy" />
            </a></p>
                """,
        unsafe_allow_html=True,
    )
    st.markdown("### Objective")
    st.markdown(
        """
                <p style = "text-align: justify">Passionate about continuous learning, I seek a dynamic environment to apply 
                and expand my technical skills, leveraging strong communication, attention to detail, and confidence to contribute 
                meaningfully to innovative projects.</p>""",
        unsafe_allow_html=True,
    )
    st.markdown("### Summary")
    st.markdown(
        """
                <p style = "text-align: justify">
                With a passion for learning and exploring new horizons, I'm committed to self-improvement, continually expanding my knowledge and skills, both in the world of technology and beyond. As a confident public speaker with strong communication skills and a knack for effective reading and writing, I enjoy sharing insights and connecting with people from diverse backgrounds.
                </p>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h3 style = "text-align:left"> 👩‍💻 &nbsp;About Me""", unsafe_allow_html=True
    )
    st.write("\n")
    st.markdown(
        """
            <p style = "text-align:left">👋 I’m Madhurima Rawat 🧑‍🎓</p>
            <p style = "text-align:left">
              👀 I’m interested in data structures and programming languages
            </p>
            <p style = "text-align:left">
              <img
                src="https://cdn.dribbble.com/users/226424/screenshots/1187861/media/6a76be08e6f01699b9a3bd47bedae88f.gif"
                height="100" />
            </p>
            <p style = "text-align:left">
              🏛️ Pursuing B.Tech(Hons.) in Data Science from CSVTU
              <img
                src="https://github.com/madhurimarawat/madhurimarawat/assets/105432776/d9fceaeb-aea5-4954-823b-ce90ceb6ef0b"
                height="35" width="35" />
            </p>
            <p style = "text-align:left">
              🌱 I’m currently learning Artificial Intelligence 🤖🧠, Data
              Science 📊📈, and Machine Learning 🛠📚
            </p>
            <p style = "text-align:left">
              👯 I’m looking to collaborate on Python
              <img src="https://cdn.freebiesupply.com/logos/large/2x/python-5-logo-png-transparent.png" title="Python"
                alt="Python Language" width="35" height="35" />
            </p>
            <p style = "text-align:left">
              💬 Ask me about programming languages 😀
            </p>
            <p style = "text-align:left">
              📫 How to reach me: &nbsp;
              <a href="https://www.linkedin.com/in/madhurima-rawat/" target="_blank">
                <img src="https://img.shields.io/badge/-madhurima-blue?style=flat&logo=Linkedin&logoColor=white"
                  alt="Linkedin Badge" />
              </a>
              &nbsp; &nbsp;
              <a href="mailto:rawatmadhurima@gmail.com">
                <img
                  src="https://github.com/madhurimarawat/Machine-Learning-Using-Python/assets/105432776/b6a0873a-e961-42c0-8fbf-ab65828c961a"
                  title="Mail Illustration" alt="Mail Illustration📫" height="35" width="30" />
              </a>
            </p>
            <p style = "text-align:left">😄 Pronouns: She/Her.</p>
            <p style = "text-align:left">
              ⚡ Fun fact: In my free time I read stories 📚 and explore
              new technologies 💻
            </p>
            <p style = "text-align:left">
              💡 Feel free to share any good story or article resources with
              me! 📚✨
            </p>
                """,
        unsafe_allow_html=True,
    )


# Function for displaying Education
def display_education():
    st.header("🧑‍🎓 &nbsp;Education")
    # Adding the HTML snippet
    st.markdown(
        """
    <p style="text-align:center;">
      <a href="https://git.io/typing-svg" style="text-align:left;">
        <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Knowledge+Empowers+the+Future"
          alt="Typing SVG" loading="lazy" /></a>
    </p>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
                <table style = "text-align:center; width: 100%; border-collapse: collapse;">
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
                """,
        unsafe_allow_html=True,
    )


# Function for displaying Experience
def display_experience():
    # Experience Section
    st.header("📑 &nbsp; Experience")

    st.markdown(
        """
    <p style="text-align:center;">
      <a href="https://git.io/typing-svg" style="text-align:left;">
        <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Hands-on+Experience+Gained"
          alt="Typing SVG" loading="lazy" /></a>
    </p>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
                
                <table style = "text-align:justify; width: 100%; border-collapse: collapse;">
        <tr style = "text-align:center">
          <th>Company</th>
          <th>Role</th>
          <th>Duration</th>
          <th>Projects and Achievements</th>
        </tr>
        <tr>
          <td>IIT Roorkee and Diginique Techlabs</td>
          <td>Student Intern - AI, ML, and DS using Python | <a
              href="https://github.com/madhurimarawat/Machine-Learning-Using-Python"><i class="fab fa-github"></i>
              GitHub</a></td>
          <td>July 2023 - Sep 2023</td>
          <td style = "text-align:justify">
            Developed ML model web app for optimizing accuracy with hyperparameter tuning on real-world datasets.
            Managed GitHub repository for organizing and sharing project codes.
          </td>
        </tr>
        <tr>
          <td>Uptricks Services Pvt. Ltd</td>
          <td>Data Science Intern | <a href="https://github.com/madhurimarawat/Credit-Card-Prediction-Analysis"><i
                class="fab fa-github"></i> GitHub</a>
          </td>
          <td>Feb 2024 - Mar 2024</td>
          <td style = "text-align:justify">
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
          <td style = "text-align:justify">
            Developed a churn analysis application, conducted World Cup data analysis, and authored an insightful
            article on hyperparameter tuning techniques.
          </td>
        </tr>
        <tr>
          <td>IIT Bhilai</td>
          <td>Project Intern - Data Science using Python</td>
          <td>Feb 2024 - June 2024</td>
          <td style = "text-align:justify">
            Contributed to the 'BSP Pre-Failure Alert Generation' project by using matrix profiling to discern motifs
            and
            discords in time series data of PLC signals, enabling the
            identification of normal and anomalous patterns with precision. Enhanced Grafana dashboards for more
            effective
            visualization of BSP mill server data.
          </td>
        </tr>
      </table>
      """,
        unsafe_allow_html=True,
    )


# Function for displaying Projects
def display_projects():
    st.header("📎 &nbsp; Projects")
    st.markdown(
        """
<p style="text-align: center;">
      <a href="https://git.io/typing-svg" style="text-align: center;">
        <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Discover+Innovative+Projects+Developed"
          alt="Typing SVG" loading="lazy" />
      </a>
                """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
<p style="text-align:center">Click on the Thumbnail to See the Website</p>
<table style="text-align:center; width: 100%; border-collapse: collapse;">
    <colgroup>
        <col style="width: 30%;">
        <col style="width: 20%;">
        <col style="width: 50%;">
    </colgroup>
    <thead>
        <tr>
            <th>Thumbnail</th>
            <th>Title</th>
            <th>Description with Technologies</th>
        </tr>
    </thead>
    <tbody>
        <!-- Library Management System Row -->
        <tr>
            <td>
                <a href="https://library-management-website.netlify.app/">
                    <img src="https://5.imimg.com/data5/SELLER/Default/2021/12/UC/BP/KG/52242850/1-4--500x500.jpg" height="150px" title="Library Management system website" alt="Library Management system website" loading="lazy" />
                </a>
            </td>
            <td>
                <p>Library Website</p>
                <p>
                    <a href="https://library-management-website.netlify.app/"><i class="fas fa-globe"></i> Website</a>
                    <br>
                    <a href="https://github.com/madhurimarawat/Library-Management-System"><i class="fab fa-github"></i> GitHub</a>
                </p>
            </td>
            <td style="text-align:justify">
                <p><b>Technologies:</b> CSS, HTML, JavaScript, and Bootstrap<br>
                Executed frontend development for a Library Management System Website, enhancing book tracking, user management, and overall library experience.</p>
            </td>
        </tr>
        <!-- ML Models Row -->
        <tr>
            <td>
                <a href="https://ml-model-datasets-using-apps-3gy37ndiancjo2nmu36sls.streamlit.app/">
                    <img src="https://github.com/madhurimarawat/ML-Model-Datasets-Using-Streamlits/assets/105432776/40af8454-c72a-4751-9976-863170693fb8" height="150px" title="Machine Learning Model Website" alt="Website Image" loading="lazy" />
                </a>
            </td>
            <td>
                <p>HyperTuneML Platform</p>
                <p>
                    <a href="https://ml-model-datasets-using-apps-3gy37ndiancjo2nmu36sls.streamlit.app/"><i class="fas fa-globe"></i> Website</a>
                    <br>
                    <a href="https://github.com/madhurimarawat/ML-Model-Datasets-Using-Streamlits"><i class="fab fa-github"></i> GitHub</a>
                </p>
            </td>
            <td style="text-align:justify">
                <p><b>Technologies:</b> Python, Scikit Learn, Joblib, and Streamlit<br>
                Developed HyperTuneML Platform, a comprehensive platform showcasing diverse machine learning models with real-world datasets. Offers practical insights to enhance understanding of predictive analytics, catering to learners at all levels.</p>
            </td>
        </tr>
        <!-- Web Scraper Row -->
        <tr>
            <td>
                <a href="https://web-scrapper-functions-h6phqofpkjtaylwyn9uvzf.streamlit.app/">
                    <img src="https://github.com/madhurimarawat/Web-Scrapper-Functions/assets/105432776/c70d6403-d229-4b6f-b484-4645bc3ddd6c" height="150px" title="Web Scraper website" alt="Web Scraper website" loading="lazy" />
                </a>
            </td>
            <td>
                <p>Web Scraper</p>
                <p>
                    <a href="https://web-scrapper-functions-h6phqofpkjtaylwyn9uvzf.streamlit.app/"><i class="fas fa-globe"></i> Website</a>
                    <br>
                    <a href="https://github.com/madhurimarawat/Web-Scrapper-Functions"><i class="fab fa-github"></i> GitHub</a>
                </p>
            </td>
            <td style="text-align:justify">
                <p><b>Technologies:</b> Python, Requests, bs4, and Streamlit<br>
                Developed a Web Scraper Website with versatile functions for efficient data extraction from diverse websites. Showcases commitment to enhancing data accessibility and streamlining information retrieval processes.</p>
            </td>
        </tr>
        <!-- GitHub Repository Lister Row -->
        <tr>
            <td>
                <a href="https://github-repository-topics-lister.netlify.app/">
                    <img src="https://github.com/madhurimarawat/GitHub-Repository-Lister/assets/105432776/8b9cade2-c861-4b88-ab72-1598745f9ce0" height="150px" title="Github Repository Lister Website" alt="Github Repository Lister Website" loading="lazy" />
                </a>
            </td>
            <td>
                <p>GitHub Repository Lister</p>
                <p>
                    <a href="https://github-repository-topics-lister.netlify.app/"><i class="fas fa-globe"></i> Website</a>
                    <br>
                    <a href="https://github.com/madhurimarawat/GitHub-Repository-Lister"><i class="fab fa-github"></i> GitHub</a>
                </p>
            </td>
            <td style="text-align:justify">
                <p><b>Technologies:</b> CSS, HTML, JavaScript, and Bootstrap<br>
                Explore detailed GitHub user profiles with profile images, bios, locations, followers, and up to 30 public repositories. Navigate repositories easily with intuitive pagination, and enjoy dynamic loading animations. Also explore a toolkit about GitHub.</p>
            </td>
        </tr>
        <!-- Semester Notes Row -->
        <tr>
            <td>
                <a href="https://madhurimarawat.github.io/Semester-Notes/">
                    <img src="https://github.com/user-attachments/assets/f84acd1e-c09b-40e7-a76a-429359a6c222" height="150px" title="Semester Notes Website" alt="Semester Notes Website" loading="lazy" />
                </a>
            </td>
            <td>
                <p>Study Materials</p>
                <p>
                    <a href="https://madhurimarawat.github.io/Semester-Notes/"><i class="fas fa-globe"></i> Website</a>
                    <br>
                    <a href="https://github.com/madhurimarawat/Semester-Notes"><i class="fab fa-github"></i> GitHub</a>
                </p>
            </td>
            <td style="text-align:justify">
                <p><b>Technologies:</b> CSS, HTML, JavaScript, and Bootstrap<br>
                Comprehensive repository of course materials, lecture notes, and study guides tailored to a range of subjects. A valuable resource for students seeking organized and easily accessible academic content, promoting effective learning and study practices.</p>
            </td>
        </tr>
        <!-- CodeCulture Row -->
        <tr>
            <td>
                <a href="https://github.com/madhurimarawat/CodeCulture-Daily">
                    <img src="https://github.com/user-attachments/assets/a3bfeab0-aa38-47ed-ad07-3a9a7b8906c7" height="150px" title="CodeCulture Website" alt="CodeCulture Website" loading="lazy" />
                </a>
            </td>
            <td>
                <p>CodeCulture Daily</p>
                <p>
                    <a href="https://madhurimarawat.github.io/CodeCulture-Daily/"><i class="fas fa-globe"></i> Website</a>
                    <br>
                    <a href="https://github.com/madhurimarawat/CodeCulture-Daily"><i class="fab fa-github"></i> GitHub</a>
                </p>
            </td>
            <td style="text-align:justify">
                <p><b>Technologies:</b>HTML, GitHub, Programming and Bootstrap<br>
                CodeCulture-Daily is a programming challenge repository offering daily problems to boost
                                coding skills. Solutions and
                                explanations are posted at 7 PM, fostering collaborative learning.</p>
            </td>
        </tr>
    </tbody>
</table>



 """,
        unsafe_allow_html=True,
    )


# Function for displaying Skills
def display_skills():

    st.header("📚 &nbsp; Skills")

    st.markdown(
        """
                 <p style="text-align: center;">
      <a href="https://git.io/typing-svg" style="text-align: center;">
        <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Diverse+Technical+Skills+Acquired"
          alt="Typing SVG" loading="lazy" />

      </a>
    </p>
                
                """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Technical Skills")
    st.markdown(
        '<i class="fas fa-code"></i>&nbsp; **Programming Languages:** C++, Python, C, R, Ruby, JavaScript, PHP, Java, MATLAB',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<i class="fas fa-laptop-code"></i>&nbsp; **Web Technologies:** HTML, CSS, Bootstrap, Streamlit, Flask',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<i class="fas fa-database"></i>&nbsp; **Database:** MySQL, Influxdb (Time Series Database)',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<i class="fas fa-pencil-ruler"></i>&nbsp; **IDE:** VS Code, PyCharm, Jupyter Notebooks, Komodo',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<i class="fas fa-tools"></i>&nbsp; **Miscellaneous:** GitHub, Grafana, Machine Learning, Web Scraping',
        unsafe_allow_html=True,
    )

    st.markdown("#### Soft Skills")
    st.markdown(
        '<i class="fas fa-exchange-alt"></i>&nbsp; Adaptability', unsafe_allow_html=True
    )
    st.markdown(
        '<i class="fas fa-search-plus"></i>&nbsp; Attention to Detail',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<i class="fas fa-user-check"></i>&nbsp; Open-mindedness',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<i class="fas fa-comments"></i>&nbsp; Proficient Communicator',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<i class="fas fa-bolt"></i>&nbsp; Quick Learner', unsafe_allow_html=True
    )


# Function for displaying Achievements
def display_achievements():
    st.header("🌟 &nbsp; Achievements")
    st.markdown(
        """
                 <p style="text-align: center;">
      <a href="https://git.io/typing-svg" style="text-align: center;">
        <img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Highlighting+my+key+accomplishments"
          alt="Typing SVG" loading="lazy" />

      </a>
    </p>
                
                """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
                <ul style = "text-align: justify">
                <li><b>NEP Conference Presenter:</b> Engaged the audience at the NEP Conference with a concise presentation on the rich heritage and culture of my home state. Contributed diverse perspectives, fostering cultural awareness.</li>
    <li> <b>GitHub Profile:</b> Diverse ML and programming projects, impactful internship contributions. Meticulously documented with beginner-friendly instructions for an innovative and visually appealing coding profile.</li>
    <li><b> HackerRank Proficiency:</b> Earned a commendable 5-star HackerRank rating in Python and MySQL, showcasing intermediate Python and beginner-level SQL skills, with a notable 3-star rating in C programming.</li>
    </ul>""",
        unsafe_allow_html=True,
    )


# Function for section navigation
def select_section(selected_section):

    # Content based on selected section
    if selected_section == "Profile":
        display_objective()

    elif selected_section == "Education":
        display_education()

    elif selected_section == "Experience":
        display_experience()

    elif selected_section == "Projects":
        display_projects()

    elif selected_section == "Skills":
        display_skills()

    elif selected_section == "Achievements":
        display_achievements()


# Social Links
def social_links():

    # Links with Font Awesome icons
    st.sidebar.markdown(
        """
        <a href="mailto:rawatmadhurima@gmail.com"><i class="fas fa-envelope"></i> Email</a> &nbsp; | &nbsp;
      <a href="tel:+9407959924"><i class="fa fa-phone"></i> 9407959924</a> &nbsp; | &nbsp;
      <a href="https://github.com/madhurimarawat"><i class="fab fa-github"></i> GitHub</a> &nbsp; |
      <a href="https://www.linkedin.com/in/madhurima-rawat/"><i class="fab fa-linkedin"></i> LinkedIn</a> &nbsp;|&nbsp;
      <a href="https://linktr.ee/madhurima_rawat" target="_blank"><i class="fa fa-link"></i> LinkTree</a> &nbsp;|&nbsp;
      <a href="https://madhurimarawat.github.io/Portfolio-Website/"><i class="fas fa-globe"></i> Portfolio</a> &nbsp;|
      <a href="https://madhurima-devfolio.streamlit.app/"><i class="fas fa-code"></i> Devfolio</a> &nbsp;|&nbsp;
      <a href="https://hackerrank.com/rawatmadhurima4"><i class="fas fa-laptop-code"></i> HackerRank</a> &nbsp;|&nbsp;
      <a href="https://alison.com/profile/31860447"><i class="fas fa-tools"></i> Alison</a>             
""",
        unsafe_allow_html=True,
    )


# Main Function
def main():
    st.title("Madhurima Rawat's Devfolio")

    # Sidebar navigation
    st.sidebar.title("Explore")
    selected_section = st.sidebar.radio(
        "Go to",
        ["Profile", "Education", "Experience", "Projects", "Skills", "Achievements"],
    )

    # Include Font Awesome CSS
    st.sidebar.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <div class="sidebar-content">
            <h1><a href="https://drive.google.com/file/d/1EYrjwt8p55lhdj78in0dio0IwTDdsPAL/view?usp=sharing" target="_blank">
                <i class="fas fa-file-alt"></i> Visit My Resume
            </a></h1>
        </div>
        
    """,
        unsafe_allow_html=True,
    )

    # Print newlines
    st.sidebar.write("\n")

    # Displaying Links
    social_links()

    # Showing sections
    select_section(selected_section)


# Function to include background image and opacity
def display_background_image(url, opacity):
    """
    Displays a background image with a specified opacity on the web app using CSS.

    Args:
    - url (str): URL of the background image.
    - opacity (float): Opacity level of the background image.
    """
    # Set background image using HTML and CSS
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# Calling Main Funtion
if __name__ == "__main__":

    # Call function to display the background image with opacity
    display_background_image(
        "https://lirp.cdn-website.com/1764a706/dms3rep/multi/opt/What-is-project-first-Alpha-Alias-640w.jpeg",
        0.8,
    )

    main()
