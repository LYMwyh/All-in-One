'use client';

import GithubIcon from "@/components/GithubIcon";
import {sectionIDToName} from "@/utils/customIDHelper";
import {CurrentScrollTargetContext, sectionIDsInCurrentPageContext} from "@/context/ScrollTargetContext";
import {useContext, useLayoutEffect, useRef} from "react";
import {HeaderHeightDispatchContext} from "@/context/HeaderContext";

export default function Header() {
    const scrollSectionTargets = useContext(sectionIDsInCurrentPageContext);
    const {currentScrollTarget, dispatchCurrentScrollTarget} = useContext(CurrentScrollTargetContext);
    const setHeaderHeight = useContext(HeaderHeightDispatchContext);
    const headerRef = useRef(null);

    useLayoutEffect(() =>{
        if (headerRef.current) {
            // setHeaderHeight(headerRef.current.getBoundingClientRect().height);

            const resizeObserver = new ResizeObserver(() => {
                const currentHeaderHeight = headerRef.current.getBoundingClientRect().height;
                setHeaderHeight(currentHeaderHeight);
            });

            resizeObserver.observe(headerRef.current);
            return () => resizeObserver.disconnect();
        }
    }, [])

    return (
        <header ref={headerRef} className="sticky z-50 top-0 bg-background p-6 flex gap-4 items-center justify-between justify-self-stretch flex-wrap">
            <div className="flex items-center shrink-0 mr-6 cursor-default">
                <span className="font-bold text-3xl tracking-tight">HelloWorld-er</span>
            </div>
            <nav className="hidden grow lg:flex flex-row gap-4 justify-start shrink-0 font-bold text-bright tracking-tight *:border-l-2 *:border-l-foreground *:px-2">
                {scrollSectionTargets.map(id => {
                    return (
                        <button key={id} onClick={() => {
                            dispatchCurrentScrollTarget({type: "navigateByID", id: id});
                        }}>
                            <div className="hover:underline hover:underline-offset-2 hover:decoration-dotted hover:decoration-2">{sectionIDToName(id)}</div>
                        </button>
                    );
                })}
            </nav>
            <div className="hidden lg:flex justify-end shrink-0">
                <a className="w-fit h-fit m-auto" href="https://github.com/HelloWorld-er"><GithubIcon /></a>
            </div>
            <div className="block lg:hidden">
                <button
                    className="cursor-pointer flex items-center px-3 py-2 border rounded border-foreground hover:text-foreground hover:border-foreground">
                    <svg
                        className="fill-current h-3 w-3"
                        viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <title>Menu</title>
                        <path d="M0 3h20v2H0V3zm0 5h20v2H0V8zm0 5h20v2H0v-2z"/>
                    </svg>
                </button>
            </div>
        </header>
    );
}