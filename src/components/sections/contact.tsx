"use client";
import React from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import ContactForm from "../ContactForm";
import { config } from "@/data/config";
import { SectionHeader } from "./section-header";
import SectionWrapper from "../ui/section-wrapper";

const ContactSection = () => {
  return (
    <SectionWrapper id="contact" className="min-h-screen max-w-7xl mx-auto px-4 py-16">
      <SectionHeader id='contact' className="relative mb-8 md:mb-14" title={
        <>
          LET&apos;S WORK <br />
          TOGETHER
        </>} />
      <div className="flex justify-center z-[10] w-full">
        <Card className="w-full max-w-2xl bg-white/80 dark:bg-black/80 backdrop-blur-md rounded-xl mt-4 md:mt-10 border border-border shadow-lg">
          <CardHeader className="p-4 sm:p-6">
            <CardTitle className="text-2xl sm:text-4xl font-bold">Contact Form</CardTitle>
            <CardDescription className="text-xs sm:text-sm mt-2 leading-relaxed">
              Please contact me directly at{" "}
              <a
                target="_blank"
                href={`mailto:${config.email}`}
                className="text-primary underline underline-offset-2 cursor-can-hover break-all"
              >
                {config.email}
              </a>
              {" "}or call{" "}
              <a
                href={`tel:${config.phone.replace(/\s/g, "")}`}
                className="text-primary underline underline-offset-2 cursor-can-hover whitespace-nowrap"
              >
                {config.phone}
              </a>{" "}
              or drop your info here.
            </CardDescription>
          </CardHeader>
          <CardContent className="p-4 sm:p-6 pt-0 sm:pt-0">
            <ContactForm />
          </CardContent>
        </Card>
      </div>
    </SectionWrapper>
  );
};
export default ContactSection;
