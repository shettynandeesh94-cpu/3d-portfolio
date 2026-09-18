const config = {
  title: "Nandeesh Shetty | Portfolio",
  description: {
    long: "Official portfolio of Nandeesh Shetty, a Full-Stack & AI/ML Engineer and Computer Science undergraduate specializing in full-stack development, AI/ML engineering, LLM architectures, and modern web technologies. Explore Nandeesh Shetty's projects, skills, certifications, resume, and contact information.",
    short:
      "Official portfolio of Nandeesh Shetty, Full-Stack & AI/ML Engineer with projects, skills, resume, and contact information.",
  },
  objective:
    "Motivated Computer Science undergraduate with hands-on experience in Full-Stack Development and AI/ML Engineering. Skilled in developing intelligent AI-driven applications, scalable web platforms, and machine learning workflows with a strong foundation in problem-solving.",
  keywords: [
    "Nandeesh Shetty",
    "Nandeesh Shetty portfolio",
    "Nandeesh Shetty developer",
    "Nandeesh Shetty web developer",
    "Nandeesh Shetty AI engineer",
    "portfolio",
    "full-stack developer",
    "AI/ML engineer",
    "machine learning",
    "AI engineer",
    "LLM",
    "web development",
    "MERN stack",
    "React",
    "Node.js",
    "Python",
    "Java",
    "Spring Boot",
    "MongoDB",
    "MySQL",
    "Socket.io",
    "PHP",
    "JavaScript",
    "computer science",
  ],
  author: "Nandeesh Shetty",
  email: "shettynandeesh94@gmail.com",
  phone: "+91 9916112293",
  site: "https://nandeeshshetty.vercel.app",

  // for github stars button — set repo to empty to hide the button
  githubUsername: "shettynandeesh94-cpu",
  githubRepo: "",

  get ogImg() {
    return this.site + "/assets/seo/og-image.png";
  },
  social: {
    linkedin: "https://www.linkedin.com/in/nandeesh-shetty/",
    github: "https://github.com/shettynandeesh94-cpu",
  },
};
export { config };
