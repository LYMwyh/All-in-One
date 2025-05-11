'use client';

import GithubIcon from "@/components/GithubIcon";
import {sectionIDToName} from "@/utils/customIDHelper";
import {CurrentScrollTargetContext, sectionIDsInCurrentPageContext} from "@/context/ScrollTargetContext";
import {useContext, useEffect, useLayoutEffect, useRef, useState} from "react";
import {HeaderHeightDispatchContext} from "@/context/HeaderContext";
import CloseIcon from "@/components/CloseIcon";

export default function Header() {
    const scrollSectionTargets = useContext(sectionIDsInCurrentPageContext);
    const {currentScrollTarget, dispatchCurrentScrollTarget} = useContext(CurrentScrollTargetContext);
    const setHeaderHeight = useContext(HeaderHeightDispatchContext);
    const headerRef = useRef(null);

    const [showMenu, setShowMenu] = useState(false);
    const menuRef = useRef(null);

    useLayoutEffect(() =>{
        if (headerRef.current) {
            const resizeObserver = new ResizeObserver(() => {
                const currentHeaderHeight = headerRef.current.getBoundingClientRect().height;
                setHeaderHeight(currentHeaderHeight);
            });
            resizeObserver.observe(headerRef.current);
            return () => resizeObserver.disconnect();
        }
    }, [headerRef.current])

    useEffect(() => {
        const handleClickOutside = (event) => {
            if (!menuRef.current) return;
            const menuRect = menuRef.current.getBoundingClientRect();
            if (menuRect.top >= 0 && menuRect.left >= 0 && menuRect.bottom <= window.innerHeight &&
                menuRect.right <= window.innerWidth && menuRef.current && !menuRef.current.contains(event.target)) {
                setShowMenu(false);
            }
        };
        document.addEventListener("click", handleClickOutside);
        return () => document.removeEventListener("click", handleClickOutside);
    }, []);

    return (
        <header ref={headerRef} className="sticky z-50 top-0 mx-auto sm:mx-5 md:mx-20 p-6 bg-background flex gap-2 sm:gap-4 xl:gap-8 items-center justify-between justify-self-stretch flex-nowrap">
            <div className="flex items-center shrink-0 cursor-default">
                <span className="font-bold text-3xl 2xl:text-4xl tracking-tight">HelloWorld-er</span>
            </div>
            <nav className="hidden flex-row sm:flex grow gap-4 justify-start shrink-0 font-bold text-bright tracking-tight *:border-l-2 *:border-l-foreground *:px-2">
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
            <div className={"hidden sm:flex justify-end shrink-0"}>
                <a className="w-fit h-fit" href="https://github.com/HelloWorld-er"><GithubIcon /></a>
            </div>
            <div className="block sm:hidden">
                <button
                    className="cursor-pointer flex items-center px-3 py-2 border rounded border-foreground hover:text-foreground hover:border-foreground"
                    onClick={() => {
                        if (!showMenu) {
                            setShowMenu(true);
                        }
                    }}>
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
            <div ref={menuRef} className={(showMenu ? "translate-x-0" : "-translate-x-full") + " " + "transform transition-all fixed top-0 left-0 min-w-2/3 h-full px-4 py-8 sm:p-12 flex flex-col gap-8 flex-nowrap bg-darker-shadow"}>
                <div className="self-stretch flex flex-nowrap justify-between gap-10 items-center shrink-0 cursor-default">
                    <span className="font-bold text-4xl sm:text-5xl tracking-tight">HelloWorld-er</span>
                    <span className="w-fit h-fit cursor-pointer text-bright" onClick={() => setShowMenu(false)}><CloseIcon /></span>
                </div>
                <nav className="flex flex-col grow gap-4 justify-start shrink-0 font-bold text-bright tracking-tight *:border-l-2 *:border-l-foreground *:px-2">
                    {scrollSectionTargets.map(id => {
                        return (
                            <button key={id} onClick={() => {
                                dispatchCurrentScrollTarget({type: "navigateByID", id: id});
                                setShowMenu(false);
                            }}>
                                <div className="text-left sm:text-xl hover:underline hover:underline-offset-2 hover:decoration-dotted hover:decoration-2">{sectionIDToName(id)}</div>
                            </button>
                        );
                    })}
                </nav>
                <div className="flex justify-start shrink-0">
                    <a className="w-fit h-fit sm:*:h-8" href="https://github.com/HelloWorld-er"><GithubIcon /></a>
                </div>
            </div>
        </header>
    );
}