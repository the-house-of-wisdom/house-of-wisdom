# House of Wisdom - `بيت الحكمة`

[![Django CI](https://github.com/youzarsiph/house-of-wisdom/actions/workflows/django.yml/badge.svg)](https://github.com/youzarsiph/house-of-wisdom/actions/workflows/django.yml)
[![Black](https://github.com/youzarsiph/house-of-wisdom/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/house-of-wisdom/actions/workflows/black.yml)
[![Ruff](https://github.com/youzarsiph/house-of-wisdom/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/house-of-wisdom/actions/workflows/ruff.yml)

**House of Wisdom** is an open source, AI-powered Learning Management System (LMS) designed to transform how education is delivered online. Built with Python, Django, and Django Rest Framework (DRF), and styled using TailwindCSS, House of Wisdom offers a robust, scalable, and visually appealing platform for personalized and adaptive learning experiences.

---

## Table of Contents

- [House of Wisdom - `بيت الحكمة`](#house-of-wisdom---بيت-الحكمة)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [Roadmap](#roadmap)
  - [License](#license)
  - [Contact](#contact)

---

## Introduction

House of Wisdom redefines online education by moving beyond mere content delivery. With intelligent virtual tutoring, adaptive assessments, automated content generation, and AI-driven analytics, our project aims to create a next-generation LMS that adapts to each learner's needs while providing educators with powerful tools to track and enhance student performance.

Key highlights include:

- **Personalized Learning Journeys:** Dynamic course paths that adjust based on learner performance and feedback.
- **Interactive Virtual Tutors:** Conversational agents powered by Large Language Models (LLMs) that deliver real-time support.
- **Dynamic Content & Assessments:** Automated study guide creation, adaptive testing, and real-time curriculum updates.
- **Modern UI/UX:** A responsive interface built with TailwindCSS for an engaging and accessible user experience.

---

## Features

- **Intelligent Virtual Tutors:**
  Engage with AI-powered chatbots that provide contextual explanations and help clarify challenging concepts in real time.

- **Automated Course Material Generation:**
  Automatically generate study guides, quizzes, and interactive simulations using LLM-based models.

- **Adaptive and Interactive Assessments:**
  Implement dialogue-based assessments that evolve in difficulty according to individual user performance.

- **Dynamic Curriculum Evolution:**
  Update and rearrange course content effortlessly by utilizing real-time analytics and user feedback.

- **Multimodal Learning Experience:**
  Integrate rich content—including text, voice, and visuals—to cater to diverse learning styles.

- **Gamification Elements:**
  Motivate learners with badges, leaderboards, and role-playing scenarios that make learning fun and competitive.

- **Advanced Analytics:**
  Provide narrative performance reports and predictive insights to aid both learners and educators.

- **Collaborative Tools:**
  Facilitate group work and peer interactions through AI-moderated discussion forums and virtual study groups.

- **Seamless Integration with External Data Sources:**
  Connect to external academic databases and research APIs for always up-to-date content.

- **Ethical AI Education:**
  Include modules focused on digital ethics, privacy, and responsible AI usage through interactive case studies.

---

## Architecture

House of Wisdom employs a modular architecture to ensure scalability, maintainability, and extensibility:

- **Backend:**
  Developed in Python with Django, the backend handles core application logic, authentication, and serves RESTful endpoints using DRF.

- **Frontend:**
  The responsive UI is powered by Django templates styled with TailwindCSS, ensuring a modern, customizable look that adapts to various devices.

- **AI & LLM Integration:**
  Integrated AI modules interface with LLMs to facilitate virtual tutoring, content generation, and adaptive assessments.

- **Database:**
  Uses a robust database engine (e.g., PostgreSQL) for scalable, secure data storage.

- **Deployment:**
  The project is containerized using Docker for streamlined deployment and continuous integration, making setup and scaling straightforward.

---

## Installation

### Prerequisites

- **Git:** To clone the repository.
- **Python 3.10+** (or your preferred version as supported by Django).
- **Pip:** For installing Python dependencies.
- **Docker (optional):** For containerized deployment.

### Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/house-of-wisdom.git
    cd house-of-wisdom
    ```

2. **Setup the Python Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Configure the Project:**

    - Create a `.env` file in the project root and configure necessary environment variables (e.g., `DEBUG`, `DATABASE_URL`, secret keys, etc.).

4. **Database Setup:**

    ```bash
    python manage.py migrate
    python manage.py createsuperuser  # Optional: Create an admin user
    ```

5. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

6. **Using Docker (Optional):**

    If you have a `docker-compose.yml` setup:

    ```bash
    docker-compose up --build
    ```

---

## Usage

Once installed, you can access House of Wisdom by opening your web browser and navigating to `http://localhost:8000` (or your configured port).

- **Admin Interface:**
  Log in to the admin panel at `http://localhost:8000/admin` to manage courses, users, and site configurations.

- **API Endpoints:**
  The RESTful API powered by DRF is available under `/api` and is documented through Django’s built-in API docs (if enabled).

- **User Guides and Documentation:**
  Detailed usage guides are available in the `/docs` directory, and tutorials are provided for both developers and end users.

---

## Contributing

We welcome contributions! To get involved:

1. **Fork the Repository:**
   Create your feature branch off `main` and implement your changes.

2. **Local Setup:**
   Follow the [Installation](#installation) instructions to set up your local environment.

3. **Submit a Pull Request:**
   - Adhere to our code style guidelines.
   - Include tests for new features.
   - Update documentation where necessary.

4. **Discussion and Issues:**
   For major changes or new ideas, please open an issue to discuss before starting work.

For more detailed guidelines, refer to our [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Roadmap

Upcoming features and improvements include:

- Expansion of LLM-powered tutoring and adaptive assessments.
- Enhanced real-time collaboration tools.
- Improved integrations with external academic resources.
- Advanced analytics dashboards.

Visit our [Issues](<https://github.com/yourusername/house-of-wisdom/issues>) page for current feature requests and development discussions.

---

## License

House of Wisdom is released under the [MIT License](LICENSE), ensuring that it remains open, free, and accessible to developers and educators worldwide.

---

## Contact

For questions, feedback, or collaboration, please reach out:

- **Maintainer:** Yousuf Abu Shanab
- **GitHub:** [github.com/youzarsiph](https://github.com/yourusername)

---

*House of Wisdom is committed to pushing the boundaries of digital education through innovative AI technologies. We thank all contributors and users for their continuous support and feedback!*
