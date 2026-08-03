import base64
import os
import subprocess

BASE = r"c:\Users\Nandeesh Shetty\Downloads\3d-portfolio-main\3d-portfolio-main\portfolio-main\3d-portfolio-main"

def b64(fname):
    path = os.path.join(BASE, fname)
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

print("Encoding images...")
logo_src          = b64("zephyr_logo.png")
hero_src          = b64("hero_screenshot.png")
techstack_src     = b64("techstack_screenshot.png")
projects_src      = b64("projects_screenshot.png")
experience_src    = b64("experience_screenshot.png")
education_src     = b64("education_screenshot.png")
certifications_src= b64("certifications_screenshot.png")
contact_src       = b64("contact_screenshot.png")
print("All images encoded.")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Project Report - Nandeesh Shetty</title>
<style>
@page {{ size: A4; margin: 2cm 2cm 2cm 2cm; }}
body {{ font-family: "Times New Roman", Times, serif; font-size: 12pt; color: #000; margin:0; padding:0; }}
.pb {{ page-break-before: always; }}
.cover {{ text-align: center; padding-top: 5px; }}
.top-line {{ border: none; border-top: 1.5px solid #888; margin: 0 0 10px 0; }}
.logo {{ height: 90px; margin: 12px auto 0 auto; display: block; }}
.addr {{ font-size: 13pt; font-weight: bold; margin: 18px 0 28px 0; line-height: 1.7; }}
.title-lbl {{ font-size: 13pt; color: #8B6914; font-style: italic; margin-top: 22px; }}
.title-main {{ font-size: 18pt; font-weight: bold; letter-spacing: 0.5px; margin: 6px 0 0 0; }}
.sec-lbl {{ font-size: 12pt; color: #8B6914; font-style: italic; margin-top: 22px; }}
.sec-val {{ font-size: 14pt; font-weight: bold; margin: 4px 0 0 0; }}
h1 {{ font-size: 14pt; font-weight: bold; text-transform: uppercase; border-bottom: 1.5px solid #000; padding-bottom: 4px; margin-top: 20px; }}
h2 {{ font-size: 13pt; font-weight: bold; margin-top: 16px; }}
h3 {{ font-size: 12pt; font-weight: bold; margin-top: 12px; }}
p, li {{ text-align: justify; line-height: 1.65; }}
ul {{ padding-left: 20px; }}
pre {{ background: #f7f7f7; border: 1px solid #ccc; border-left: 4px solid #0066cc; padding: 8px; font-family: "Courier New", Courier, monospace; font-size: 8.5pt; white-space: pre-wrap; word-break: break-all; line-height: 1.35; margin: 8px 0; }}
.ct {{ text-align: center; font-size: 16pt; font-weight: bold; margin: 18px 0 22px 0; }}
.cert-body {{ text-align: justify; font-size: 12pt; line-height: 1.75; }}
.scr-img {{ width: 100%; max-height: 340px; object-fit: contain; border: 1px solid #444; display: block; margin: 0 auto; }}
.scr-cap {{ text-align: center; font-size: 9.5pt; font-style: italic; font-weight: bold; margin: 5px 0 25px 0; }}
.toc td {{ padding: 5px 0; font-size: 12pt; }}
.toc .dots {{ border-bottom: 1px dotted #000; }}
.toc .pg {{ text-align: right; width: 35px; }}
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover">

  <!-- Zephyr Letterhead: line | logo | line -->
  <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:18px;">
    <tr>
      <td style="width:30%; border-top: 1.5px solid #888; vertical-align: middle;">&nbsp;</td>
      <td style="width:40%; text-align:center; vertical-align: middle; padding: 0 10px;">
        <!-- Zephyr logo recreated in HTML -->
        <div style="display:inline-block; text-align:center;">
          <!-- Blue box with white slash -->
          <div style="width:62px; height:62px; background: linear-gradient(135deg, #5b9bd5 0%, #2e75b6 100%); border-radius:8px; margin: 0 auto 4px auto; position:relative; overflow:hidden;">
            <div style="position:absolute; top:8px; left:22px; width:7px; height:52px; background:white; transform:rotate(-20deg); border-radius:3px;"></div>
          </div>
          <div style="font-family: Arial, sans-serif; font-size: 16pt; font-weight: bold; letter-spacing: 3px; color: #1a1a1a; line-height:1.1;">ZEPHYR</div>
          <div style="font-family: Arial, sans-serif; font-size: 7pt; color: #555; letter-spacing: 0.5px;">Technologies &amp; Solutions Pvt. Ltd.</div>
        </div>
      </td>
      <td style="width:30%; border-top: 1.5px solid #888; vertical-align: middle;">&nbsp;</td>
    </tr>
  </table>

  <div class="addr">Oberle towers, Balmatta, Mangalore<br>D.K, Karnataka 575002,India</div>
  <div class="title-lbl">Project report on</div>
  <div class="title-main">PERSONAL PORTFOLIO</div>
  <div class="sec-lbl">Submitted By</div>
  <div class="sec-val">NANDEESH SHETTY</div>
  <div class="sec-lbl">Institution</div>
  <div class="sec-val">NMAM INSTITUTE OF TECHNOLOGY</div>
  <div class="sec-lbl">Internship Company</div>
  <div class="sec-val">Zephyr Technologies</div>
  <div class="sec-lbl">Course</div>
  <div class="sec-val">Full Stack Web Development Internship</div>
  <div class="sec-lbl">Academic Year</div>
  <div class="sec-val">2026&ndash;2027</div>
</div>


<div class="pb"></div>
<!-- CERTIFICATE -->
<div class="ct">CERTIFICATE</div>
<div class="cert-body">
This is to certify that <b>Nandeesh Shetty</b>, USN: <b>NNM23CS117</b>, a student of the
Department of Computer Science and Engineering, NMAM Institute of Technology (NMAMIT), Nitte,
has successfully completed the project titled <b>&quot;Personal Portfolio Website&quot;</b> as part of the
Full Stack Web Development coursework at Zephyr Technologies &amp; Solutions Pvt. Ltd.
<br><br>
The project work embodied in this report is a record of the bona fide work carried out by the student
during the academic year 2025&ndash;2026, under the guidance and supervision of the Department.
<br><br><br>
<table width="100%">
  <tr>
    <td>Date: 28/07/2026<br>Place: Nitte</td>
    <td style="text-align:right">Signature of Guide / Faculty-in-Charge</td>
  </tr>
</table>
</div>

<div class="pb"></div>
<!-- ACKNOWLEDGEMENT -->
<div class="ct">ACKNOWLEDGEMENT</div>
<div class="cert-body">
I would like to express my sincere gratitude to the Department of Computer Science and Engineering,
NMAM Institute of Technology (NMAMIT), Nitte, for providing me with the opportunity and resources
to undertake this project on Personal Portfolio Website development.
<br><br>
I am grateful to my faculty guide and the teaching staff of the department for their valuable guidance,
constructive feedback, and continuous encouragement throughout the duration of this project.
<br><br>
I also extend my heartfelt thanks to my friends and family members for their constant support and motivation.
<br><br><br>
<div style="text-align:right; font-weight:bold;">Nandeesh Shetty</div>
</div>

<div class="pb"></div>
<!-- ABSTRACT -->
<div class="ct">ABSTRACT</div>
<p>
The <b>Personal Portfolio Website</b> is a full-stack, 3D-animated, and responsive web application developed
by <b>Nandeesh Shetty</b>, a Computer Science &amp; Engineering undergraduate at NMAM Institute of Technology,
to present a comprehensive professional profile to recruiters, collaborators, and fellow developers.
</p>
<p>
Built using <b>Next.js 16</b>, <b>React 19</b>, and <b>TypeScript</b>, the application features an immersive
3D animated background powered by <b>Spline</b>, smooth scroll behaviour implemented through <b>Lenis</b>,
and rich page animations driven by <b>GSAP</b> and <b>Framer Motion</b>. The UI is styled with
<b>Tailwind CSS</b> and <b>Radix UI</b> component primitives, providing a consistent, accessible, and
responsive design system across all device sizes.
</p>
<p>
The portfolio is organized into clearly defined sections — Hero, Skills, Projects, Experience, Education,
Certifications, and Contact. The Skills section showcases 21 technologies including React.js, Node.js,
Express.js, Java, Spring Boot, PHP, MongoDB, MySQL, Socket.io, JWT, and Git. The Projects section
presents real-world applications such as the <b>Chat Analyzer</b>, <b>College Event Management System</b>,
and <b>CineREC (DBMS Project)</b> using an interactive scrolling preview component with live demo embeds.
</p>
<p>
The Experience section highlights Nandeesh's ongoing internship as a <b>Full-Stack Web Developer at
Zephyr Technologies &amp; Solutions</b> (July 2026 – Present), along with a prior research and field survey
in organic farming. The Education section details his B.Tech in Computer Science &amp; Engineering (CGPA: 8.27)
and PUC from BSRNSV PU College (84.5%). The Certifications section includes credentials from
<b>Oracle</b> (OCI Generative AI Professional), <b>Udemy</b> (Full Stack Development), and
<b>Microsoft Learn</b> (AINNOVATION 2025 AI &amp; Azure Learning Challenges).
</p>
<p>
The Contact section integrates <b>Nodemailer</b> and <b>Resend</b> for functional email delivery directly
from the portfolio. Additional features include a real-time visitor presence indicator via <b>Socket.io</b>,
a radial navigation menu, dark/light theme switching, animated particle backgrounds, an easter-egg system,
and a custom preloader. The application is deployed on <b>Vercel</b> at
<i>nandeeshshetty.vercel.app</i> and version-controlled on GitHub.
</p>

<div class="pb"></div>
<!-- TABLE OF CONTENTS -->
<div class="ct">TABLE OF CONTENTS</div>
<table class="toc" width="100%">
  <tr><td>1. Introduction</td><td class="dots"></td><td class="pg">1</td></tr>
  <tr><td>2. Objectives</td><td class="dots"></td><td class="pg">2</td></tr>
  <tr><td>3. Problem Statement</td><td class="dots"></td><td class="pg">3</td></tr>
  <tr><td>4. Technology Stack</td><td class="dots"></td><td class="pg">4</td></tr>
  <tr><td>5. System Design &amp; Architecture</td><td class="dots"></td><td class="pg">5</td></tr>
  <tr><td>6. Implementation / Source Code</td><td class="dots"></td><td class="pg">6</td></tr>
  <tr><td>7. Features</td><td class="dots"></td><td class="pg">7</td></tr>
  <tr><td>8. Outputs / Screenshots</td><td class="dots"></td><td class="pg">8</td></tr>
  <tr><td>9. Results</td><td class="dots"></td><td class="pg">9</td></tr>
  <tr><td>10. Conclusion</td><td class="dots"></td><td class="pg">10</td></tr>
  <tr><td>11. References</td><td class="dots"></td><td class="pg">11</td></tr>
</table>

<div class="pb"></div>
<h1>CHAPTER 1: INTRODUCTION</h1>
<p>In today's competitive academic and professional environment, a strong digital presence has become essential
for students and technology professionals. The Personal Portfolio Website provides a dynamic, interactive, and
visually appealing platform that showcases technical skills, projects, education, certifications, and professional
experience in a way that static resumes cannot.</p>

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
<p>Students and early-career technology professionals often rely solely on static resumes that cannot effectively
communicate their ability to build real, functioning applications. The Personal Portfolio Website addresses this
by providing a custom-built, full-stack front-end solution that demonstrates live project work and technical capability.</p>

<div class="pb"></div>
<h1>CHAPTER 2: TECHNOLOGY STACK</h1>
<ul>
  <li><b>Next.js 16</b> &ndash; React-based framework for SSR and SSG with Turbopack</li>
  <li><b>React 19</b> &ndash; UI component library for building reusable interface elements</li>
  <li><b>TypeScript</b> &ndash; Superset of JavaScript providing static type checking</li>
  <li><b>Tailwind CSS</b> &ndash; Utility-first CSS framework for responsive design</li>
  <li><b>Framer Motion</b> &ndash; Animation library for smooth page transitions and effects</li>
  <li><b>Three.js / React Three Fiber</b> &ndash; 3D rendering in the browser</li>
  <li><b>Git &amp; GitHub</b> &ndash; Version control and repository hosting</li>
  <li><b>Vercel</b> &ndash; Cloud platform for deployment and hosting</li>
</ul>

<div class="pb"></div>
<h1>CHAPTER 3: IMPLEMENTATION / SOURCE CODE</h1>
<p>The following section presents representative excerpts of the source code used to implement the core components
of Nandeesh Shetty's 3D Personal Portfolio Website.</p>

<h3>1. App Page (src/app/page.tsx)</h3>
<pre>"use client";
import React from "react";
import SmoothScroll from "@/components/smooth-scroll";
import {{ cn }} from "@/lib/utils";
import AnimatedBackground from "@/components/animated-background";
import SkillsSection from "@/components/sections/skills";
import ExperienceSection from "@/components/sections/experience";
import ProjectsSection from "@/components/sections/projects";
import ContactSection from "@/components/sections/contact";
import HeroSection from "@/components/sections/hero";

function MainPage() {{
  return (
    &lt;SmoothScroll&gt;
      &lt;AnimatedBackground /&gt;
      &lt;main className={{cn("bg-slate-100 dark:bg-transparent canvas-overlay-mode")}}&gt;
        &lt;HeroSection /&gt;
        &lt;SkillsSection /&gt;
        &lt;ExperienceSection /&gt;
        &lt;ProjectsSection /&gt;
        &lt;ContactSection /&gt;
      &lt;/main&gt;
    &lt;/SmoothScroll&gt;
  );
}}
export default MainPage;</pre>

<h3>2. Hero Section (src/components/sections/hero.tsx)</h3>
<pre>import {{ cn }} from "@/lib/utils";
import Link from "next/link";
import React from "react";
import {{ Button }} from "../ui/button";
import {{ File }} from "lucide-react";
import {{ BlurIn }} from "../reveal-animations";
import {{ config }} from "@/data/config";
import SectionWrapper from "../ui/section-wrapper";

const HeroSection = () =&gt; {{
  return (
    &lt;SectionWrapper id="hero" className="relative w-full h-screen"&gt;
      &lt;div className="grid md:grid-cols-2"&gt;
        &lt;div className="flex flex-col justify-center items-start md:p-20"&gt;
          &lt;BlurIn delay={{0.7}}&gt;&lt;p&gt;Hi, I am&lt;/p&gt;&lt;/BlurIn&gt;
          &lt;BlurIn delay={{1}}&gt;
            &lt;h1 className="font-bold text-7xl md:text-9xl"&gt;{{config.author}}&lt;/h1&gt;
          &lt;/BlurIn&gt;
          &lt;div className="mt-8 flex gap-3"&gt;
            &lt;Link href={{"/resume"}}&gt;&lt;Button&gt;&lt;File size={{24}} /&gt; Resume&lt;/Button&gt;&lt;/Link&gt;
            &lt;Link href={{"#contact"}}&gt;&lt;Button variant={{"outline"}}&gt;Hire Me&lt;/Button&gt;&lt;/Link&gt;
          &lt;/div&gt;
        &lt;/div&gt;
      &lt;/div&gt;
    &lt;/SectionWrapper&gt;
  );
}};
export default HeroSection;</pre>

<div class="pb"></div>
<h3>3. Projects Section (src/components/sections/projects.tsx)</h3>
<pre>"use client";
import React from "react";
import projects from "@/data/projects";
import {{ SectionHeader }} from "./section-header";
import SectionWrapper from "../ui/section-wrapper";
import ScrollingPreview from "../scrolling-preview";

const ProjectsSection = () =&gt; {{
  return (
    &lt;SectionWrapper id="projects" className="max-w-7xl mx-auto px-4"&gt;
      &lt;SectionHeader id="projects" title="Projects" /&gt;
      &lt;div className="grid grid-cols-1 md:grid-cols-3 gap-4"&gt;
        {{projects.map((project) =&gt; (
          &lt;div key={{project.id}}&gt;
            &lt;ScrollingPreview src={{project.src}} alt={{project.title}} /&gt;
          &lt;/div&gt;
        ))}}
      &lt;/div&gt;
    &lt;/SectionWrapper&gt;
  );
}};
export default ProjectsSection;</pre>

<h3>4. Contact Section (src/components/sections/contact.tsx)</h3>
<pre>"use client";
import React from "react";
import {{ Card, CardContent, CardHeader, CardTitle }} from "@/components/ui/card";
import ContactForm from "../ContactForm";

const ContactSection = () =&gt; {{
  return (
    &lt;section id="contact" className="min-h-screen max-w-7xl mx-auto"&gt;
      &lt;Card className="bg-white/70 dark:bg-black/70 backdrop-blur-sm rounded-xl"&gt;
        &lt;CardHeader&gt;&lt;CardTitle className="text-4xl"&gt;Contact Form&lt;/CardTitle&gt;&lt;/CardHeader&gt;
        &lt;CardContent&gt;&lt;ContactForm /&gt;&lt;/CardContent&gt;
      &lt;/Card&gt;
    &lt;/section&gt;
  );
}};
export default ContactSection;</pre>

<div class="pb"></div>
<!-- SCREENSHOTS -->
<h1>CHAPTER 4: OUTPUTS / SCREENSHOTS</h1>
<p style="margin-bottom:20px">The following section presents the application's key interface screens captured
from the deployed portfolio website.</p>

<img src="{hero_src}" class="scr-img" alt="Hero Section">
<div class="scr-cap">Fig 1: Home / Hero Section</div>

<img src="{techstack_src}" class="scr-img" alt="Tech Stack Section">
<div class="scr-cap">Fig 2: Skills / Tech Stack Section</div>

<div class="pb"></div>
<img src="{projects_src}" class="scr-img" alt="Projects Section">
<div class="scr-cap">Fig 3: Projects Section</div>

<img src="{experience_src}" class="scr-img" alt="Experience Section">
<div class="scr-cap">Fig 4: Experience Section</div>

<div class="pb"></div>
<img src="{education_src}" class="scr-img" alt="Education Section">
<div class="scr-cap">Fig 5: Education Section</div>

<img src="{certifications_src}" class="scr-img" alt="Certifications Section">
<div class="scr-cap">Fig 6: Certifications Section</div>

<div class="pb"></div>
<img src="{contact_src}" class="scr-img" alt="Contact Section">
<div class="scr-cap">Fig 7: Contact Section</div>

<div class="pb"></div>
<h1>CHAPTER 5: CONCLUSION</h1>
<p>The Personal Portfolio Website successfully demonstrates the design and development of a modern, responsive web
application using React.js, TypeScript, Next.js, and Tailwind CSS. The project effectively consolidates technical
skills, academic background, project work, professional experience, and certifications into a single professionally
designed digital platform, enhancing the developer's online presence and career prospects.</p>

<h1>CHAPTER 6: REFERENCES</h1>
<ul>
  <li>React.js Official Documentation &ndash; https://react.dev</li>
  <li>TypeScript Official Documentation &ndash; https://www.typescriptlang.org/docs</li>
  <li>Next.js Official Documentation &ndash; https://nextjs.org/docs</li>
  <li>Tailwind CSS Official Documentation &ndash; https://tailwindcss.com/docs</li>
  <li>Vercel Documentation &ndash; https://vercel.com/docs</li>
  <li>Framer Motion &ndash; https://www.framer.com/motion</li>
</ul>

</body>
</html>"""

html_path = os.path.join(BASE, "Project_Report_Nandeesh_Shetty.html")
pdf_path  = os.path.join(BASE, "Project_Report_Nandeesh_Shetty.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("HTML written.")

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_exe):
    edge_exe = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

cmd = [edge_exe, "--headless", "--disable-gpu",
       f"--print-to-pdf={pdf_path}", "--no-pdf-header-footer", html_path]

print("Generating PDF...")
subprocess.run(cmd, check=True)
print(f"PDF saved at: {pdf_path}")
