'use client';

import Typist from "@/components/Typist";
import React, {memo, useContext, useEffect, useLayoutEffect, useState} from "react";
import Section from "@/components/Section";
import GithubIcon from "@/components/GithubIcon";
import PetProjectCard from "@/components/PetProjectCard";
import {CurrentScrollTargetContext} from "@/context/ScrollTargetContext";
import Footer from "@/components/Footer";
import Header from "@/components/Header";
import {HeaderHeightContext} from "@/context/HeaderContext";

// Isolated Typist Component for the Heading
const HomeHeading = memo(() => {
    const typedHeadings = ["Derek", "a Developer", "a Student from Hong Kong"];
    const [typedHeading, setTypedHeading] = useState("Derek");

    useEffect(() => {
        let index = 0;

        function updateTypedHeading() {
            setTypedHeading(typedHeadings[index]);
            index = (index + 1) % typedHeadings.length; // Loop back to the start
            setTimeout(updateTypedHeading, 20000);
        }

        updateTypedHeading();
    }, []);

    return (
        <h1>Hello World, <br/>
            <span className="text-highlight">
                <Typist rootKey="typist-1">I am {typedHeading}</Typist>
            </span>!
        </h1>
    );
});


export default function Home() {
    const {currentScrollTarget, dispatchCurrentScrollTarget} = useContext(CurrentScrollTargetContext);
    const headerHeight = useContext(HeaderHeightContext);

    const [mainHeightStyle, setMainHeightStyle] = useState({});
    useLayoutEffect(() => {
        if (headerHeight) {
            setMainHeightStyle({ minHeight: `calc(100vh - ${headerHeight}px)` });
        }
    }, [headerHeight]);

    function updateScrollTop() {
        dispatchCurrentScrollTarget({type: "update"});
    }

    useEffect(() => {
        window.addEventListener("scroll", updateScrollTop);

        return () => {
            window.removeEventListener("scroll", updateScrollTop);
        };
    }, []);

    if (!headerHeight) {
        return (
            <div className="h-fit px-10 lg:px-30 flex flex-col flex-nowrap">
                <Header />
            </div>
        );
    }
    return (
        <div className="h-fit px-10 lg:px-30 flex flex-col flex-nowrap">
            <Header />
            <main className="h-fit">
                <Section sectionID="hello-world" className="h-full flex flex-col items-center text-center" style={mainHeightStyle ? mainHeightStyle : null}>
                    <HomeHeading/>
                    <Typist rootKey="typist-2">
                        <p className="text-2xl w-[calc(40*var(--text-sm))] max-w-full">
                            Welcome to my personal website where I share my thoughts and experiences.
                        </p>
                        <p className="text-2xl w-[calc(40*var(--text-sm))] max-w-full">
                            I am a high schooler from Hong Kong.
                        </p>
                    </Typist>
                    <button className="px-4 py-2 border border-dotted rounded-4xl" onClick={() => {
                        dispatchCurrentScrollTarget({type: "navigateByID", id: "sectionID-about-me"});
                    }}>Scroll To see More
                    </button>
                </Section>
                <Section sectionID="about-me" className="h-full flex flex-col mx-auto" style={mainHeightStyle ? mainHeightStyle : null}>
                    <div className="my-auto">
                        <h2 className="flex flex-row items-center gap-8">
                            About Me
                            <div className="grow border-shadow border-b-2"></div>
                        </h2>
                        <div>
                            <p>
                                Hi, <span className="text-highlight font-bold">I’m Derek</span>, <span
                                className="text-highlight font-bold">a student from Hong Kong</span>.
                                I’m <span className="text-highlight font-bold">a self-taught programmer</span>and <span
                                className="text-highlight font-bold">an active learner</span>.
                                Computer science and programming are my biggest passions. Over the past three years, I’ve
                                dedicated countless hours to learning and improving my skills, developing one project after
                                another—each inspired by my observations of school and daily life.
                            </p>
                            <p>
                                I built this website to bring all my projects together, creating a space where I can share
                                my experiences and passion for coding with you. For me, it’s a personal journey of growth.
                                For others, I hope it can be a helpful resource.
                            </p>
                            <p>
                                I invite you to explore this site, check out my projects, and join me on this journey of
                                learning and discovery!
                            </p>
                        </div>
                    </div>
                </Section>
                <Section sectionID="pet-projects" className="h-full flex flex-col mx-auto" style={mainHeightStyle ? mainHeightStyle : null}>
                    <div className="my-auto">
                        <h2 className="flex flex-row items-center gap-8">
                            Pet Projects
                            <div className="grow border-shadow border-b-2"></div>
                        </h2>
                        <div className="flex flex-col lg:grid grid-cols-3 grid-rows-2 gap-8">
                            <PetProjectCard>
                                {{
                                    heading: "Twenty-Four Puzzle",
                                    description: "A classical mathematics game that challenges your math skills and number sensitivity. The goal is to use four numbers and basic operations to reach the target number of 24.",
                                    tags: ["Tauri", "SolidJS", "TailwindCSS"],
                                    repositoryLabel: "Public Repository",
                                    repositoryLink: "https://github.com/HelloWorld-er/Twenty-Four-Puzzle",
                                    repositoryIcon: <GithubIcon />,
                                }}
                            </PetProjectCard>
                            <PetProjectCard>
                                {{
                                    heading: "HelloWorld Chronicle",
                                    description: "My personal website that serves as a portfolio and a blog. It showcases my projects, thoughts, and experiences.",
                                    tags: ["Next.js", "TailwindCSS"],
                                    repositoryLabel: "Private Repository",
                                    repositoryLink: "",
                                    repositoryIcon: null,
                                }}
                            </PetProjectCard>
                            <PetProjectCard>
                                {{
                                    heading: "ARP Spoofing Detection",
                                    description: "A tool that detects ARP spoofing attacks on a network. It uses libpcap to capture packets and ImGui for the GUI.",
                                    tags: ["C++", "libpcap", "ImGui", "glfw + Vulkan"],
                                    repositoryLabel: "Public Repository",
                                    repositoryLink: "https://github.com/HelloWorld-er/ArpSpoofingDetection",
                                    repositoryIcon: <GithubIcon />,
                                }}
                            </PetProjectCard>
                        </div>
                    </div>
                </Section>
            </main>
            <Footer className="mt-3" />
        </div>
    );
}