import { cn } from "@/lib/utils";
import Link from "next/link";
import React from "react";
import { Button } from "../ui/button";
import { File, Github, Linkedin } from "lucide-react";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { usePreloader } from "../preloader";
import { BlurIn, BoxReveal } from "../reveal-animations";
import ScrollDownIcon from "../scroll-down-icon";
import { SiGithub, SiLinkedin, SiX } from "react-icons/si";
import { config } from "@/data/config";

import SectionWrapper from "../ui/section-wrapper";

const HeroSection = () => {
  const { isLoading } = usePreloader();

  return (
    <SectionWrapper id="hero" className={cn("relative w-full min-h-screen h-auto md:h-screen")}>
      <div className="grid grid-cols-1 md:grid-cols-2 min-h-full">
        <div
          className={cn(
            "min-h-[calc(100dvh-3rem)] md:h-[calc(100dvh-4rem)] z-[2]",
            "col-span-1",
            "flex flex-col justify-start md:justify-center items-center md:items-start text-center md:text-left",
            "pt-24 pb-16 px-4 sm:px-8 md:p-20 lg:p-24 xl:p-28"
          )}
        >
          {!isLoading && (
            <div className="flex flex-col items-center md:items-start w-full max-w-full">
              <div className="w-full">
                <BlurIn delay={0.7}>
                  <p
                    className={cn(
                      "md:self-start mt-2 sm:mt-4 font-medium text-sm sm:text-xl text-slate-500 dark:text-zinc-400",
                      "cursor-default bg-clip-text"
                    )}
                  >
                    Hi, I am
                  </p>
                </BlurIn>

                <BlurIn delay={1}>
                  <Tooltip delayDuration={300}>
                    <TooltipTrigger asChild>
                      <h1
                        className={cn(
                          "leading-tight text-slate-800 dark:text-slate-100 text-center md:text-left tracking-tight",
                          "font-bold text-3xl sm:text-4xl md:text-5xl lg:text-6xl xl:text-7xl mt-2 mb-3",
                          "cursor-default text-edge-outline font-display whitespace-nowrap select-none"
                        )}
                      >
                        {config.author}
                      </h1>
                    </TooltipTrigger>
                    <TooltipContent
                      side="top"
                      className="dark:bg-white dark:text-black"
                    >
                      theres something waiting for you in devtools
                    </TooltipContent>
                  </Tooltip>
                </BlurIn>

                <BlurIn delay={1.2}>
                  <div
                    className={cn(
                      "md:self-start md:mt-4 max-w-xl font-medium text-sm sm:text-xl text-slate-500 dark:text-zinc-400",
                      "cursor-default bg-clip-text"
                    )}
                  >
                    <p className="text-base sm:text-xl font-semibold text-foreground/90">
                      CS Undergraduate · Full-Stack & AI/ML Engineer
                    </p>
                    <span className="mt-3 block text-xs sm:text-base md:text-lg leading-relaxed whitespace-normal text-muted-foreground">
                      {config.objective}
                    </span>
                  </div>
                </BlurIn>
              </div>

              <div className="mt-6 sm:mt-8 flex flex-col sm:flex-row items-center gap-3 w-full sm:w-fit">
                <Link
                  href={"/resume"}
                  target="_blank"
                  className="w-full sm:w-auto"
                >
                  <BoxReveal delay={2} width="100%">
                    <Button className="flex items-center justify-center gap-2 w-full px-6">
                      <File size={20} />
                      <p>Resume</p>
                    </Button>
                  </BoxReveal>
                </Link>
                <div className="flex items-center gap-3 w-full sm:w-auto justify-center">
                  <Tooltip delayDuration={300}>
                    <TooltipTrigger asChild>
                      <Link href={"#contact"} className="flex-1 sm:flex-none">
                        <Button
                          variant={"outline"}
                          className="w-full sm:w-auto px-6"
                        >
                          Hire Me
                        </Button>
                      </Link>
                    </TooltipTrigger>
                    <TooltipContent side="bottom">
                      <p>pls 🥹 🙏</p>
                    </TooltipContent>
                  </Tooltip>
                  <div className="flex items-center gap-2">
                    <Link
                      href={config.social.github}
                      target="_blank"
                      className="cursor-can-hover"
                    >
                      <Button variant={"outline"} size="icon" className="w-10 h-10">
                        <SiGithub size={20} />
                      </Button>
                    </Link>
                    <Link
                      href={config.social.linkedin}
                      target="_blank"
                      className="cursor-can-hover"
                    >
                      <Button variant={"outline"} size="icon" className="w-10 h-10">
                        <SiLinkedin size={20} />
                      </Button>
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
        <div className="hidden md:grid col-span-1"></div>
      </div>
      <div className="absolute bottom-6 md:bottom-10 left-[50%] -translate-x-1/2 pointer-events-none">
        <ScrollDownIcon />
      </div>
    </SectionWrapper>
  );
};

export default HeroSection;
