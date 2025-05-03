'use client';

import Typist from "@/components/Typist";
import React, {memo, useEffect, useState} from "react";
import {scrollToElement} from "@/utils/scrollToElement";

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
    return (
        <>
            <section id="hello-world" className="flex flex-col items-center text-center">
                <HomeHeading/>
                <Typist rootKey="typist-2">
                    <p className="text-2xl w-[calc(40*var(--text-sm))]">
                        Welcome to my personal website where I share my thoughts and experiences.
                    </p>
                    <p className="text-2xl w-[calc(40*var(--text-sm))]">
                        I am a high schooler from Hong Kong.
                    </p>
                </Typist>
                <button className="px-4 py-2 border border-dotted rounded-4xl" onClick={() => {
                    const aboutMeElement = document.getElementById("about-me");
                    if (aboutMeElement) {
                        scrollToElement(aboutMeElement);
                    }
                }}>Scroll To see More
                </button>
            </section>
            <section id="about-me" className="flex flex-col mx-auto">
                <div className="my-auto">
                    <h2 className="flex flex-row items-center gap-8">
                        About Me
                        <div className="grow border-shadow border-b-2"></div>
                    </h2>
                    <div>
                        <p>
                            Hi, <span className="text-highlight font-bold">I’m Derek</span>, <span
                            className="text-highlight font-bold">a student from Hong Kong</span>.
                            I’m <span className="text-highlight font-bold">a self-taught programmer</span>, <span
                            className="text-highlight font-bold">an active learner</span>, and <span
                            className="text-highlight font-bold">a community contributor</span>.
                            Computer science and programming are my biggest passions. Over the past three years, I’ve
                            dedicated countless hours to learning and improving my skills, developing one project after
                            another—each inspired by my observations of school and daily life, whether it’s a sketch
                            assistant or a fun game.
                        </p>
                        <p>
                            I built this website to bring all my projects together, creating a space where I can share
                            my experiences and passion for coding with you. For me, it’s a personal journey of growth.
                            For others, I hope it can be a helpful resource. Some of my projects are designed to support
                            specific groups, like the elderly. Games like Flappy Bird and Alien Invasion can help
                            improve reaction speed, while the Twenty-Four Puzzle strengthens basic math skills and
                            number sensitivity. I also developed the Magical Wallpaper Crawler to enhance online search
                            efficiency.
                        </p>
                        <p>
                            Beyond coding, I’ve shared my study log, which I hope will inspire other students to explore
                            subjects like history more deeply. My writings can serve as examples for analyzing comics or
                            historical statements. Additionally, my voluntary work is something I hope will encourage
                            more people to get involved in their communities and support those in need.
                        </p>
                        <p>
                            I invite you to explore this site, check out my projects, and join me on this journey of
                            learning and discovery!
                        </p>
                    </div>
                </div>
            </section>
        </>
    );
}