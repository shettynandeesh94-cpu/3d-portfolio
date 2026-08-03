import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>PROJECT REPORT ON PERSONAL PORTFOLIO - NANDEESH SHETTY</title>
<style>
    @page {
        size: A4;
        margin: 1.8cm 1.8cm 1.8cm 1.8cm;
    }
    body {
        font-family: 'Times New Roman', Times, serif;
        font-size: 11.5pt;
        line-height: 1.5;
        color: #000000;
        margin: 0;
        padding: 0;
    }
    .page-break {
        page-break-before: always;
    }
    
    /* Cover Page */
    .cover-page {
        text-align: center;
        padding-top: 0.2cm;
        padding-bottom: 0.5cm;
    }
    .zephyr-logo-img {
        height: 75px;
        margin-bottom: 5px;
    }
    .company-address {
        font-size: 13pt;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 30px;
    }
    .report-title-label {
        font-size: 13pt;
        margin-top: 20px;
    }
    .report-main-title {
        font-size: 20pt;
        font-weight: bold;
        margin: 10px 0 30px 0;
        letter-spacing: 1px;
    }
    .section-label {
        font-size: 13pt;
        margin-top: 12px;
    }
    .section-value {
        font-size: 15pt;
        font-weight: bold;
        margin-bottom: 18px;
    }
    .academic-year {
        font-size: 15pt;
        font-weight: bold;
        margin-top: 6px;
    }
    
    /* Certificate & Acknowledgement */
    .cert-title {
        text-align: center;
        font-size: 17pt;
        font-weight: bold;
        margin-bottom: 25px;
        margin-top: 15px;
    }
    .cert-body {
        text-align: justify;
        font-size: 12.5pt;
        line-height: 1.75;
        margin-bottom: 35px;
    }
    .cert-footer {
        margin-top: 70px;
    }
    .cert-date-place {
        float: left;
        font-size: 11.5pt;
    }
    .cert-signature {
        float: right;
        font-size: 11.5pt;
        text-align: right;
    }
    .clear {
        clear: both;
    }
    
    /* Headings */
    h1 {
        font-size: 15pt;
        font-weight: bold;
        text-transform: uppercase;
        margin-top: 25px;
        margin-bottom: 12px;
        border-bottom: 1px solid #000;
        padding-bottom: 4px;
    }
    h2 {
        font-size: 13pt;
        font-weight: bold;
        margin-top: 18px;
        margin-bottom: 8px;
    }
    h3 {
        font-size: 11.5pt;
        font-weight: bold;
        margin-top: 12px;
        margin-bottom: 4px;
    }
    
    p {
        text-align: justify;
        margin-bottom: 10px;
    }
    
    ul {
        margin-top: 4px;
        margin-bottom: 10px;
        padding-left: 22px;
    }
    li {
        margin-bottom: 5px;
        text-align: justify;
    }
    
    /* Code Excerpts */
    pre {
        background-color: #f8f9fa;
        border: 1px solid #d1d5db;
        padding: 8px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 8pt;
        white-space: pre-wrap;
        word-wrap: break-word;
        margin: 10px 0;
        border-left: 4px solid #0066cc;
        line-height: 1.35;
    }
    
    /* 2 Screenshots Per Page Container */
    .two-img-page {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        height: 100%;
    }
    .screenshot-item {
        text-align: center;
        margin-bottom: 15px;
    }
    .screenshot-img-2perpage {
        width: 92%;
        max-height: 330px;
        object-fit: contain;
        border: 1px solid #333;
        box-shadow: 0 3px 8px rgba(0,0,0,0.18);
        border-radius: 4px;
    }
    .screenshot-caption-2perpage {
        text-align: center;
        font-size: 9.5pt;
        font-style: italic;
        margin-top: 6px;
        color: #111;
        font-weight: bold;
    }

    .flow-box {
        text-align: center;
        background-color: #f9f9f9;
        border: 1px dashed #666;
        padding: 12px;
        margin: 15px 0;
        font-family: Arial, sans-serif;
        line-height: 1.7;
    }
    
    .toc-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        font-size: 11.5pt;
    }
    .toc-table td {
        padding: 6px 0;
    }
    .toc-dots {
        border-bottom: 1px dotted #000;
    }
    .toc-page {
        text-align: right;
        width: 40px;
    }
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover-page">
    <div style="margin-bottom: 30px;">
        <img src="zephyr_logo.png" class="zephyr-logo-img" alt="Zephyr Logo">
        <div class="company-address">
            Oberle towers, Balmatta, Mangalore<br>
            D.K, Karnataka 575002,India
        </div>
    </div>
    
    <div style="margin-bottom: 40px;">
        <div class="report-title-label">Project report on</div>
        <div class="report-main-title">PERSONAL PORTFOLIO</div>
    </div>
    
    <div>
        <div class="section-label">Submitted By</div>
        <div class="section-value">NANDEESH SHETTY</div>
        
        <div class="section-label">Institution</div>
        <div class="section-value">NMAM INSTITUTE OF TECHNOLOGY</div>
        
        <div class="section-label">Internship Company</div>
        <div class="section-value">Zephyr Technologies</div>
        
        <div class="section-label">Course</div>
        <div class="section-value">Full Stack Web Development Internship</div>
        
        <div class="section-label">Academic Year</div>
        <div class="academic-year">2026–2027</div>
    </div>
</div>

<div class="page-break"></div>

<!-- CERTIFICATE -->
<div class="cert-title">CERTIFICATE</div>
<div class="cert-body">
    This is to certify that <strong>Nandeesh Shetty</strong>, USN: <strong>NNM23CS117</strong>, a final-year student of the Department of Computer Science and Engineering, NMAM Institute of Technology (NMAMIT), Nitte, has successfully completed the project titled <strong>“Personal Portfolio Website”</strong> as part of the Full Stack Web Development coursework.
    <br><br>
    The project work embodied in this report is a record of the bona fide work carried out by the student during the academic year 2025–2026, under the guidance and supervision of the Department of Computer Science and Engineering.
</div>
<div class="cert-footer">
    <div class="cert-date-place">
        Date: 28/07/2026<br>
        Place: Nitte
    </div>
    <div class="cert-signature">
        Signature of Guide / Faculty-in-Charge
    </div>
    <div class="clear"></div>
</div>

<div class="page-break"></div>

<!-- ACKNOWLEDGEMENT -->
<div class="cert-title">ACKNOWLEDGEMENT</div>
<div class="cert-body">
    I would like to express my sincere gratitude to the Department of Computer Science and Engineering, NMAM Institute of Technology (NMAMIT), Nitte, for providing me with the opportunity and resources to undertake this project on Personal Portfolio Website development.
    <br><br>
    I am grateful to my faculty guide and the teaching staff of the department for their valuable guidance, constructive feedback, and continuous encouragement throughout the duration of this project, which helped me apply modern full stack web development concepts effectively.
    <br><br>
    I also extend my heartfelt thanks to my friends and family members for their constant support and motivation, which played an important role in the successful completion of this project.
    <br><br><br>
    <div style="text-align: right; font-weight: bold;">Nandeesh Shetty</div>
</div>

<div class="page-break"></div>

<!-- ABSTRACT -->
<div class="cert-title">ABSTRACT</div>
<p>
The Personal Portfolio Website is a modern, responsive web application developed to present a comprehensive and professional digital profile, including technical skills, academic background, projects, work experience, and certifications. The platform is designed to give recruiters, collaborators, and visitors an engaging and organized overview of the developer's technical capabilities and accomplishments.
</p>
<p>
The application was built using Next.js 16 and React 19 with TypeScript for a type-safe, component-driven front-end architecture, with Turbopack as the build tool for fast development and optimized production bundling. Tailwind CSS was used to implement a clean, responsive, and consistent design system, while HTML5, CSS3, and JavaScript form the underlying foundation of the interface. Version control and collaboration were managed using Git and GitHub, and the completed application was deployed on Vercel for public accessibility.
</p>
<p>
The portfolio consists of clearly defined sections — Home, About, Skills, Projects, Experience, Education, Certifications, and Contact — supported by smooth animations and an interactive, mobile-first user interface. The project demonstrates the practical application of modern front-end engineering practices, including component reusability, responsive layout design, and streamlined deployment workflows, resulting in a fast, accessible, and visually polished personal branding platform.
</p>

<div class="page-break"></div>

<!-- TABLE OF CONTENTS -->
<div class="cert-title">TABLE OF CONTENTS</div>
<table class="toc-table">
    <tr><td>1. Introduction</td><td class="toc-dots"></td><td class="toc-page">1</td></tr>
    <tr><td>2. Objectives</td><td class="toc-dots"></td><td class="toc-page">2</td></tr>
    <tr><td>3. Problem Statement</td><td class="toc-dots"></td><td class="toc-page">3</td></tr>
    <tr><td>4. Scope of the Project</td><td class="toc-dots"></td><td class="toc-page">4</td></tr>
    <tr><td>5. Literature Survey</td><td class="toc-dots"></td><td class="toc-page">5</td></tr>
    <tr><td>6. Technology Stack</td><td class="toc-dots"></td><td class="toc-page">6</td></tr>
    <tr><td>7. System Requirements</td><td class="toc-dots"></td><td class="toc-page">7</td></tr>
    <tr><td>8. System Design and Architecture</td><td class="toc-dots"></td><td class="toc-page">8</td></tr>
    <tr><td>9. Methodology</td><td class="toc-dots"></td><td class="toc-page">9</td></tr>
    <tr><td>10. Modules Description</td><td class="toc-dots"></td><td class="toc-page">10</td></tr>
    <tr><td>11. Implementation / Source Code</td><td class="toc-dots"></td><td class="toc-page">11</td></tr>
    <tr><td>12. Features</td><td class="toc-dots"></td><td class="toc-page">12</td></tr>
    <tr><td>13. Outputs / Screenshots</td><td class="toc-dots"></td><td class="toc-page">13</td></tr>
    <tr><td>14. Results</td><td class="toc-dots"></td><td class="toc-page">14</td></tr>
    <tr><td>15. Conclusion</td><td class="toc-dots"></td><td class="toc-page">15</td></tr>
    <tr><td>16. Future Scope</td><td class="toc-dots"></td><td class="toc-page">16</td></tr>
    <tr><td>17. References</td><td class="toc-dots"></td><td class="toc-page">17</td></tr>
</table>

<div class="page-break"></div>

<!-- CHAPTER 1 -->
<div style="text-align: right; font-size: 9pt; color: #666; margin-bottom: 15px;">Personal Portfolio Website – Project Report</div>
<h1>CHAPTER 1: INTRODUCTION</h1>
<p>
In today's competitive academic and professional environment, a strong digital presence has become essential for students and technology professionals seeking internships, job opportunities, and collaborations. Traditional resumes and static documents, while useful, often fail to capture the full scope of a candidate's technical abilities, project work, and creative problem-solving skills in an engaging manner.
</p>
<p>
The Personal Portfolio Website is designed to address this need by providing a dynamic, interactive, and visually appealing platform that showcases an individual's skills, projects, education, certifications, and professional experience. Unlike a conventional resume, a portfolio website allows for richer presentation through project demonstrations, embedded links, structured layouts, and responsive design that adapts seamlessly to desktops, tablets, and mobile devices.
</p>

<h2>OBJECTIVES</h2>
<ul>
    <li>To design and develop a responsive personal portfolio website using modern front-end technologies.</li>
    <li>To showcase technical skills, academic qualifications, projects, and certifications in an organized digital format.</li>
    <li>To implement a component-based architecture using React.js and Next.js for reusability and maintainability.</li>
    <li>To leverage TypeScript for type safety and improved code reliability.</li>
    <li>To utilize Tailwind CSS for building a consistent, utility-first, and responsive design system.</li>
    <li>To ensure fast load times and optimized builds using Turbopack as the build engine.</li>
    <li>To create an interactive and visually engaging user interface with smooth 3D animations and transitions.</li>
</ul>

<h2>PROBLEM STATEMENT</h2>
<p>
Students and early-career technology professionals often rely solely on static resumes or generic professional networking profiles to present their skills and achievements to recruiters. Plain text resumes cannot effectively communicate a candidate's ability to build real, functioning applications. The Personal Portfolio Website addresses this problem by providing a custom-built, full-stack front-end solution.
</p>

<div class="page-break"></div>

<!-- CHAPTER 6 IMPLEMENTATION / SOURCE CODE -->
<h1>CHAPTER 6: IMPLEMENTATION / SOURCE CODE</h1>
<p>The following section presents representative excerpts of the source code used to implement the core structure and components of Nandeesh Shetty's 3D Personal Portfolio Website.</p>

<h3>1. App Page Component (src/app/page.tsx)</h3>
<pre>
"use client";
import React from "react";
import SmoothScroll from "@/components/smooth-scroll";
import { cn } from "@/lib/utils";
import AnimatedBackground from "@/components/animated-background";
import SkillsSection from "@/components/sections/skills";
import ExperienceSection from "@/components/sections/experience";
import ProjectsSection from "@/components/sections/projects";
import ContactSection from "@/components/sections/contact";
import HeroSection from "@/components/sections/hero";

function MainPage() {
  return (
    &lt;SmoothScroll&gt;
      &lt;AnimatedBackground /&gt;
      &lt;main className={cn("bg-slate-100 dark:bg-transparent canvas-overlay-mode")}&gt;
        &lt;HeroSection /&gt;
        &lt;SkillsSection /&gt;
        &lt;ExperienceSection /&gt;
        &lt;ProjectsSection /&gt;
        &lt;ContactSection /&gt;
      &lt;/main&gt;
    &lt;/SmoothScroll&gt;
  );
}
export default MainPage;
</pre>

<h3>2. Hero Section Component (src/components/sections/hero.tsx)</h3>
<pre>
import { cn } from "@/lib/utils";
import Link from "next/link";
import React from "react";
import { Button } from "../ui/button";
import { File } from "lucide-react";
import { BlurIn } from "../reveal-animations";
import { config } from "@/data/config";
import SectionWrapper from "../ui/section-wrapper";

const HeroSection = () => {
  return (
    &lt;SectionWrapper id="hero" className="relative w-full h-screen"&gt;
      &lt;div className="grid md:grid-cols-2"&gt;
        &lt;div className="flex flex-col justify-center items-start md:p-20"&gt;
          &lt;BlurIn delay={0.7}&gt;&lt;p&gt;Hi, I am&lt;/p&gt;&lt;/BlurIn&gt;
          &lt;BlurIn delay={1}&gt;
            &lt;h1 className="font-bold text-7xl md:text-9xl"&gt;{config.author}&lt;/h1&gt;
          &lt;/BlurIn&gt;
          &lt;p className="font-medium text-slate-500"&gt;CS Undergraduate · Full-Stack Developer&lt;/p&gt;
          &lt;div className="mt-8 flex gap-3"&gt;
            &lt;Link href={"/resume"}&gt;&lt;Button&gt;&lt;File size={24} /&gt; Resume&lt;/Button&gt;&lt;/Link&gt;
            &lt;Link href={"#contact"}&gt;&lt;Button variant={"outline"}&gt;Hire Me&lt;/Button&gt;&lt;/Link&gt;
          &lt;/div&gt;
        &lt;/div&gt;
      &lt;/div&gt;
    &lt;/SectionWrapper&gt;
  );
};
export default HeroSection;
</pre>

<div class="page-break"></div>

<h3>3. Projects Section Component (src/components/sections/projects.tsx)</h3>
<pre>
"use client";
import React from "react";
import projects from "@/data/projects";
import { SectionHeader } from "./section-header";
import SectionWrapper from "../ui/section-wrapper";
import ScrollingPreview from "../scrolling-preview";

const ProjectsSection = () => {
  return (
    &lt;SectionWrapper id="projects" className="max-w-7xl mx-auto px-4"&gt;
      &lt;SectionHeader id="projects" title="Projects" /&gt;
      &lt;div className="grid grid-cols-1 md:grid-cols-3 gap-4"&gt;
        {projects.map((project) =&gt; (
          &lt;div key={project.id}&gt;
            &lt;ScrollingPreview src={project.src} alt={project.title} /&gt;
          &lt;/div&gt;
        ))}
      &lt;/div&gt;
    &lt;/SectionWrapper&gt;
  );
};
export default ProjectsSection;
</pre>

<h3>4. Contact Section Component (src/components/sections/contact.tsx)</h3>
<pre>
"use client";
import React from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import ContactForm from "../ContactForm";

const ContactSection = () => {
  return (
    &lt;section id="contact" className="min-h-screen max-w-7xl mx-auto"&gt;
      &lt;Card className="bg-white/70 dark:bg-black/70 backdrop-blur-sm rounded-xl"&gt;
        &lt;CardHeader&gt;&lt;CardTitle className="text-4xl"&gt;Contact Form&lt;/CardTitle&gt;&lt;/CardHeader&gt;
        &lt;CardContent&gt;&lt;ContactForm /&gt;&lt;/CardContent&gt;
      &lt;/Card&gt;
    &lt;/section&gt;
  );
};
export default ContactSection;
</pre>

<div class="page-break"></div>

<!-- CHAPTER 8 OUTPUTS / SCREENSHOTS (EXACT INTRO TEXT & 2 IMAGES PER PAGE) -->
<h1>CHAPTER 8: OUTPUTS / SCREENSHOTS</h1>
<p style="text-align: justify; margin-bottom: 20px;">
The following section presents placeholders for the application's key interface screens. Actual screenshots captured from the deployed application should be inserted at each indicated location.
</p>

<!-- SCREENSHOT PAGE 1: HERO & TECH STACK -->
<div class="two-img-page">
    <div class="screenshot-item">
        <img src="hero_screenshot.png" class="screenshot-img-2perpage" alt="Home Hero Section">
        <div class="screenshot-caption-2perpage">Fig 8.1: Home / Hero Section</div>
    </div>
    
    <div class="screenshot-item">
        <img src="techstack_screenshot.png" class="screenshot-img-2perpage" alt="Tech Stack Section">
        <div class="screenshot-caption-2perpage">Fig 8.2: Skills Section (Tech Stack)</div>
    </div>
</div>

<div class="page-break"></div>

<!-- SCREENSHOT PAGE 2: PROJECTS & EXPERIENCE -->
<div class="two-img-page">
    <div class="screenshot-item">
        <img src="projects_screenshot.png" class="screenshot-img-2perpage" alt="Projects Showcase Section">
        <div class="screenshot-caption-2perpage">Fig 8.3: Projects Section</div>
    </div>
    
    <div class="screenshot-item">
        <img src="experience_screenshot.png" class="screenshot-img-2perpage" alt="Experience Section">
        <div class="screenshot-caption-2perpage">Fig 8.4: Experience Section</div>
    </div>
</div>

<div class="page-break"></div>

<!-- SCREENSHOT PAGE 3: EDUCATION & CERTIFICATIONS -->
<div class="two-img-page">
    <div class="screenshot-item">
        <img src="education_screenshot.png" class="screenshot-img-2perpage" alt="Education Section">
        <div class="screenshot-caption-2perpage">Fig 8.5: Education Section</div>
    </div>
    
    <div class="screenshot-item">
        <img src="certifications_screenshot.png" class="screenshot-img-2perpage" alt="Certifications Section">
        <div class="screenshot-caption-2perpage">Fig 8.6: Certifications Section</div>
    </div>
</div>

<div class="page-break"></div>

<!-- SCREENSHOT PAGE 4: CONTACT SECTION -->
<div class="two-img-page">
    <div class="screenshot-item" style="margin-top: 20px;">
        <img src="contact_screenshot.png" class="screenshot-img-2perpage" alt="Contact Section">
        <div class="screenshot-caption-2perpage">Fig 8.7: Contact Section</div>
    </div>
</div>

<div class="page-break"></div>

<!-- RESULTS & CONCLUSION -->
<h1>CHAPTER 9: RESULTS</h1>
<p>
The portfolio website renders consistently and correctly across desktops, laptops, tablets, and mobile devices. Tailwind CSS's responsive utility classes ensured that layouts adjusted fluidly to varying screen sizes without loss of usability. Component-based architecture resulted in fast page load times and smooth client-side interactions across all sections of the application.
</p>

<h1>CHAPTER 10: CONCLUSION</h1>
<p>
The Personal Portfolio Website successfully demonstrates the design and development of a modern, responsive web application using React.js, TypeScript, Next.js, and Tailwind CSS. The project effectively consolidates technical skills, academic background, project work, professional experience, and certifications into a single, professionally designed digital platform.
</p>

<h1>CHAPTER 11: REFERENCES</h1>
<ul>
    <li>React.js Official Documentation – https://react.dev</li>
    <li>TypeScript Official Documentation – https://www.typescriptlang.org/docs</li>
    <li>Next.js Official Documentation – https://nextjs.org/docs</li>
    <li>Tailwind CSS Official Documentation – https://tailwindcss.com/docs</li>
    <li>Vercel Documentation – https://vercel.com/docs</li>
</ul>

</body>
</html>
"""

html_path = r"c:\Users\Nandeesh Shetty\Downloads\3d-portfolio-main\3d-portfolio-main\portfolio-main\3d-portfolio-main\Project_Report_Nandeesh_Shetty.html"
pdf_path = r"c:\Users\Nandeesh Shetty\Downloads\3d-portfolio-main\3d-portfolio-main\portfolio-main\3d-portfolio-main\Project_Report_Nandeesh_Shetty.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_exe):
    edge_exe = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

cmd = [
    edge_exe,
    "--headless",
    "--disable-gpu",
    f"--print-to-pdf={pdf_path}",
    "--no-pdf-header-footer",
    html_path
]

print("Re-generating PDF with USN NNM23CS117 and Department of Computer Science and Engineering...")
subprocess.run(cmd, check=True)
print(f"Successfully generated PDF at: {pdf_path}")
