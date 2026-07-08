const config = {
  title: "Nandeesh Shetty | Portfolio",
  description: {
    long: "Official portfolio of Nandeesh Shetty, a full-stack web developer and Computer Science undergraduate specializing in MERN stack, Java Spring Boot, and modern web technologies. Explore Nandeesh Shetty's projects, skills, certifications, resume, and contact information.",
    short:
      "Official portfolio of Nandeesh Shetty with projects, skills, resume, and contact information.",
  },
  objective:
    "Motivated Computer Science undergraduate with hands-on experience in full-stack web development and a strong foundation in problem-solving. Eager to contribute to innovative tech projects while continuously growing my skills in software engineering and modern web technologies.",
  keywords: [
    "Nandeesh Shetty",
    "Nandeesh Shetty portfolio",
    "Nandeesh Shetty developer",
    "Nandeesh Shetty web developer",
    "portfolio",
    "full-stack developer",
    "web development",
    "MERN stack",
    "React",
    "Node.js",
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
