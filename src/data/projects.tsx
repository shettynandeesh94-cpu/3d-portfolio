import { Button } from "@/components/ui/button";
import { TypographyH3, TypographyP } from "@/components/ui/typography";
import { ArrowUpRight } from "lucide-react";
import Link from "next/link";
import { ReactNode } from "react";
import { LiveDemoEmbed } from "@/components/live-demo-embed";

const ProjectsLinks = ({ live, repo }: { live?: string; repo?: string }) => {
  return (
    <div className="flex flex-col md:flex-row items-center justify-start gap-3 my-3 mb-8">
      {live && live !== "#" && (
        <Link
          className="font-mono underline flex gap-2"
          rel="noopener"
          target="_new"
          href={live}
        >
          <Button variant={"default"} size={"sm"}>
            Visit Website
            <ArrowUpRight className="ml-3 w-5 h-5" />
          </Button>
        </Link>
      )}
      {repo && repo !== "#" && (
        <Link
          className="font-mono underline flex gap-2"
          rel="noopener"
          target="_new"
          href={repo}
        >
          <Button variant={"default"} size={"sm"}>
            Github
            <ArrowUpRight className="ml-3 w-5 h-5" />
          </Button>
        </Link>
      )}
    </div>
  );
};

export type Skill = {
  title: string;
  bg: string;
  fg: string;
  icon: ReactNode;
};

const MaskIcon = ({ src, title }: { src: string; title?: string }) => (
  <span
    role="img"
    aria-label={title}
    className="block bg-current"
    style={{
      width: "1em",
      height: "1em",
      WebkitMaskImage: `url(${src})`,
      maskImage: `url(${src})`,
      WebkitMaskRepeat: "no-repeat",
      maskRepeat: "no-repeat",
      WebkitMaskPosition: "center",
      maskPosition: "center",
      WebkitMaskSize: "contain",
      maskSize: "contain",
    }}
  />
);

const brand = (title: string, file: string): Skill => ({
  title,
  bg: "black",
  fg: "white",
  icon: <MaskIcon src={`/assets/logos/${file}`} title={title} />,
});

const PROJECT_SKILLS = {
  mongo: brand("MongoDB", "mongodb-mono.svg"),
  express: brand("Express", "express-mono.svg"),
  react: brand("React.js", "react-mono.svg"),
  node: brand("Node.js", "nodedotjs-mono.svg"),
  sockerio: brand("Socket.io", "socketdotio-mono.svg"),
  js: brand("JavaScript", "javascript-mono.svg"),
  jwt: {
    title: "JWT",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">JWT</span>,
  },
  java: {
    title: "Java",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">☕</span>,
  },
  springboot: {
    title: "Spring Boot",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">🍃</span>,
  },
  html: {
    title: "HTML",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">HTML</span>,
  },
  css: {
    title: "CSS",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">CSS</span>,
  },
  mysql: {
    title: "MySQL",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">SQL</span>,
  },
  php: {
    title: "PHP",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">PHP</span>,
  },
  bootstrap: {
    title: "Bootstrap",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">B</span>,
  },
  python: {
    title: "Python",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">🐍</span>,
  },
  streamlit: {
    title: "Streamlit",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">🎈</span>,
  },
  ts: brand("TypeScript", "typescript-mono.svg"),
  tailwind: brand("Tailwind CSS", "tailwind-css-mono.svg"),
  shadcn: brand("Shadcn UI", "shadcn-ui-mono.svg"),
  nextjs: brand("Next.js", "nextdotjs-mono.svg"),
  framerMotion: brand("Framer Motion", "motion.svg"),
  vite: {
    title: "Vite",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">⚡</span>,
  },
  gemini: {
    title: "Google Gemini AI",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">✨</span>,
  },
  webaudio: {
    title: "Web Audio API",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">🎙️</span>,
  },
  ai: {
    title: "AI & LLM",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">🤖</span>,
  },
  nlp: {
    title: "NLP",
    bg: "black",
    fg: "white",
    icon: <span className="text-xs font-bold">NLP</span>,
  },
};

export type Project = {
  id: string;
  category: string;
  date: string;
  title: string;
  src: string;
  screenshots: string[];
  skills: { frontend: Skill[]; backend: Skill[] };
  content: React.ReactNode | any;
  github?: string;
  live: string;
};

const projects: Project[] = [
  {
    id: "realtime-chat",
    category: "Full-Stack Application",
    date: "2025",
    title: "Chat Analyzer",
    src: "/assets/projects-screenshots/portfolio/landing.png",
    screenshots: [],
    skills: {
      frontend: [
        PROJECT_SKILLS.react,
        PROJECT_SKILLS.js,
        PROJECT_SKILLS.html,
        PROJECT_SKILLS.css,
      ],
      backend: [
        PROJECT_SKILLS.python,
        PROJECT_SKILLS.streamlit,
        PROJECT_SKILLS.nlp,
      ],
    },
    live: "https://chat-analyzer-1-prom.onrender.com/",
    github: "https://github.com/shettynandeesh94-cpu/chat-analyzer",
    get content() {
      return (
        <div>
          <TypographyP className="font-mono text-2xl text-center">
            A full-stack real-time chat analysis tool that extracts deep
            insights from WhatsApp and messaging exports.
          </TypographyP>
          <TypographyP className="font-mono ">
            Built with Python and Streamlit, this chat analyzer parses exported
            chat files and generates detailed analytics — from message frequency
            heatmaps to sentiment analysis and word clouds — giving you an
            unprecedented view into your conversations.
          </TypographyP>
          <ProjectsLinks live={this.live} repo={this.github} />

          {/* ── LIVE DEMO ── */}
          <TypographyH3 className="my-4 mt-8 flex items-center gap-2">
            <span className="inline-block w-2 h-2 rounded-full bg-green-400 animate-pulse" />
            Live Demo
          </TypographyH3>
          <p className="font-mono mb-4 text-sm text-muted-foreground">
            Try it right here — upload a WhatsApp chat export and explore the
            analytics instantly.
          </p>
          <LiveDemoEmbed
            url="https://chat-analyzer-1-prom.onrender.com/"
            title="Chat Analyzer"
          />

          <TypographyH3 className="my-4 mt-10">
            Chat Insights & Analytics
          </TypographyH3>
          <p className="font-mono mb-2">
            Analyzes exported chat files to surface message volume over time,
            most-active hours, top senders, emoji usage, word frequency, and
            more — all visualised as interactive charts.
          </p>

          <TypographyH3 className="my-4 mt-8">Key Features</TypographyH3>
          <p className="font-mono mb-2">
            The application includes NLP-powered sentiment analysis to gauge the
            tone of conversations, word clouds highlighting recurring themes, an
            activity heatmap, media-share statistics, and exportable reports —
            all rendered in a clean, responsive Streamlit interface.
          </p>

          <TypographyH3 className="my-4 mt-8">Tech Stack</TypographyH3>
          <p className="font-mono mb-2">
            Python for data processing and NLP, Streamlit for the interactive
            web interface, Pandas for data wrangling, Matplotlib / Plotly for
            visualisations, and deployed live on Render for zero-config hosting.
          </p>
        </div>
      );
    },
  },
  {
    id: "govtwatch-ai",
    category: "AI & Automation Platform",
    date: "2026",
    title: "GovtWatch-AI",
    src: "/assets/projects-screenshots/portfolio/landing.png",
    screenshots: [],
    skills: {
      frontend: [
        PROJECT_SKILLS.react,
        PROJECT_SKILLS.ts,
        PROJECT_SKILLS.tailwind,
        PROJECT_SKILLS.shadcn,
      ],
      backend: [
        PROJECT_SKILLS.node,
        PROJECT_SKILLS.express,
        PROJECT_SKILLS.mongo,
        PROJECT_SKILLS.jwt,
      ],
    },
    live: "https://govtwatch-ai.vercel.app/",
    github: "#",
    get content() {
      return (
        <div>
          <TypographyP className="font-mono text-2xl text-center">
            An intelligent, AI-powered government website and regulatory document monitoring platform.
          </TypographyP>
          <TypographyP className="font-mono ">
            GovtWatch-AI automatically tracks, scrapes, and analyzes updates from critical Indian Government portals (including SEBI, MRPL, GeM, Department of Expenditure, and MeitY) to detect policy changes, newly uploaded circulars, and specific keywords so compliance teams never miss a critical regulatory update.
          </TypographyP>
          <ProjectsLinks live={this.live} repo={this.github} />

          {/* ── LIVE DEMO ── */}
          <TypographyH3 className="my-4 mt-8 flex items-center gap-2">
            <span className="inline-block w-2 h-2 rounded-full bg-green-400 animate-pulse" />
            Live Demo
          </TypographyH3>
          <p className="font-mono mb-4 text-sm text-muted-foreground">
            Explore the live platform directly below — track government websites, view AI summaries, and monitor policy updates.
          </p>
          <LiveDemoEmbed
            url="https://govtwatch-ai.vercel.app/"
            title="GovtWatch-AI"
          />

          <TypographyH3 className="my-4 mt-10">
            🤖 Automated Web Scraping & Ingestion
          </TypographyH3>
          <p className="font-mono mb-2">
            Daily automated monitoring of designated Indian government portals (SEBI, MRPL, GeM, DoE, MeitY) with Puppeteer, Cheerio, and Node-Cron to detect new tenders, notifications, gazettes, and policy circulars. Downloads and extracts text from complex multi-page PDFs while preserving document structure.
          </p>

          <TypographyH3 className="my-4 mt-8">
            🔍 Intelligent Change Detection & Diffs
          </TypographyH3>
          <p className="font-mono mb-2">
            Compares historical versions of documents and webpages to highlight additions, modifications, and removals with side-by-side line level comparisons and AI-generated summaries.
          </p>

          <TypographyH3 className="my-4 mt-8">
            🎯 Keyword Tracking & Multi-Channel Alerts
          </TypographyH3>
          <p className="font-mono mb-2">
            Define custom keywords (e.g., "Refinery", "Tax", "Compliance") and receive immediate automated email and dashboard notifications the moment they appear on any monitored government site.
          </p>

          <TypographyH3 className="my-4 mt-8">
            📊 Comprehensive Dashboard & 🛡️ Secure Admin Panel
          </TypographyH3>
          <p className="font-mono mb-2">
            Built with React, TypeScript, Tailwind CSS, and Shadcn UI to visualize recent changes, download PDF/CSV reports with jsPDF, manage monitored URLs, and enforce Role-Based Access Control (RBAC) with audit logs.
          </p>
        </div>
      );
    },
  },
  {
    id: "examgen-ai",
    category: "AI Recruitment & Assessment Engine",
    date: "2026",
    title: "ExamGen AI Pro",
    src: "/assets/projects-screenshots/portfolio/landing.png",
    screenshots: [],
    skills: {
      frontend: [
        PROJECT_SKILLS.react,
        PROJECT_SKILLS.vite,
        PROJECT_SKILLS.tailwind,
        PROJECT_SKILLS.framerMotion,
        PROJECT_SKILLS.webaudio,
      ],
      backend: [
        PROJECT_SKILLS.gemini,
        PROJECT_SKILLS.node,
        PROJECT_SKILLS.express,
        PROJECT_SKILLS.mongo,
        PROJECT_SKILLS.jwt,
      ],
    },
    live: "https://exam-gen-ai-smoky.vercel.app/",
    github: "#",
    get content() {
      return (
        <div>
          <TypographyP className="font-mono text-2xl text-center">
            Next-Generation AI Practice Exam Generator, Automated Assessment Engine & Interactive Recruitment Simulator.
          </TypographyP>
          <TypographyP className="font-mono ">
            ExamGen AI Pro is a comprehensive, production-grade AI learning and placement platform. It enables students to upload reference textbooks/notes (PDFs), auto-extract topic hierarchies, generate custom mock exams (MCQs, short answer, long answer, and scenario questions) using Google Gemini AI, and grade descriptive answers in real time with granular alignment metrics. Additionally, it features an immersive, standalone AI Mock Interview Workspace simulating real-world recruiter assessments.
          </TypographyP>
          <ProjectsLinks live={this.live} repo={this.github} />

          {/* ── LIVE DEMO ── */}
          <TypographyH3 className="my-4 mt-8 flex items-center gap-2">
            <span className="inline-block w-2 h-2 rounded-full bg-green-400 animate-pulse" />
            Live Demo
          </TypographyH3>
          <p className="font-mono mb-4 text-sm text-muted-foreground">
            Experience the live application right here — generate exams, practice mock interviews, and test speaking telemetry.
          </p>
          <LiveDemoEmbed
            url="https://exam-gen-ai-smoky.vercel.app/"
            title="ExamGen AI Pro"
          />

          <TypographyH3 className="my-4 mt-10">
            🌟 Dynamic Exam Synthesis & PDF Ingestion
          </TypographyH3>
          <p className="font-mono mb-2">
            Parses, splits, and catalogs text chunks from uploaded subject materials (PDF textbooks and lecture notes). Generates multi-format questions including Multiple Choice, Conceptual Short Answer, Comprehensive Long Answer, and Scenario-based Case Studies tailored to selected difficulty tiers (Easy, Medium, Hard).
          </p>

          <TypographyH3 className="my-4 mt-8">
            ⚡ AI-Powered Real-Time Grading, Scoring & Feedback
          </TypographyH3>
          <p className="font-mono mb-2">
            Evaluates descriptive and subjective student submissions with real-time Google Gemini AI autograding. The interactive diagnostics dashboard visualizes alignment scores, gaps in conceptual understanding, and tailored suggestions for improvement.
          </p>

          <TypographyH3 className="my-4 mt-8">
            🎙️ Immersive Recruiter Mock Interview Workspace
          </TypographyH3>
          <p className="font-mono mb-2">
            Features a dedicated full-screen placement-room viewport with an animated professional AI recruiter avatar powered by Framer Motion. The avatar exhibits lifelike breathing, smart eyelid blinking, audio-synchronized mouth movement during speech synthesis (TTS), thinking orbits, and listening states during voice-to-text recording. Includes a live Web Audio visualizer rendering cyan waveform frequency telemetry in canvas.
          </p>

          <TypographyH3 className="my-4 mt-8">
            📊 Interactive Telemetry HUD (Speaking Biometrics)
          </TypographyH3>
          <p className="font-mono mb-2">
            Real-time biometric analytics including Speaking Tempo (Words-Per-Minute estimation), Tone & Emotion detector (Confident, Analytical, Attentive), Speech Clarity & Conceptual Alignment percentages matching response against answer rubrics, and a ticking elapsed question timer.
          </p>

          <TypographyH3 className="my-4 mt-8">
            💻 Full-Stack Architecture & Security
          </TypographyH3>
          <p className="font-mono mb-2">
            Built with React 18, Vite, Tailwind CSS, Framer Motion, and Lucide React on the frontend, with Node.js, Express.js, MongoDB, JWT authentication, and Google Gemini API integration on the backend.
          </p>
        </div>
      );
    },
  },
];
export default projects;
