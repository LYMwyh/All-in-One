'use client';

import {createContext, useEffect, useReducer, useState} from "react";
import {scrollToElement} from "@/utils/scrollToElement";


export const sectionIDsInCurrentPageContext = createContext(null);
export const ScrollTargetDispatchContext = createContext(null);
export const CurrentScrollTargetContext = createContext(null);

export default function ScrollTargetContextProvider({children}) {
    const [scrollTargets, dispatchScrollTargets] = useReducer((scrollTargets, action) => {
        switch (action.type) {
            case "addScrollTarget": {
                return new Map(scrollTargets).set(action.id, {idType: action.idType, element: action.element});
            }
            case "removeScrollTarget": {
                const newScrollTargets = new Map(scrollTargets);
                newScrollTargets.delete(action.id);
                return newScrollTargets;
            }
            default: {
                throw new Error("Unknown action type " + action.type);
            }
        }
    }, new Map(), undefined);

    let currentScrollTargetIndex = 0;
    const [currentScrollTarget, dispatchCurrentScrollTarget] = useReducer((currentScrollTarget, action) => {
        if (!scrollTargets.size) return null;
        switch (action.type) {
            case "update": {
                let index = 0;
                for (const elementInfo of scrollTargets.values()) {
                    const elementRect = elementInfo.element.getBoundingClientRect();
                    if ((elementRect.top > 0 && elementRect.top < window.innerHeight) || (elementRect.bottom > 0 && elementRect.bottom < window.innerHeight)) {
                        currentScrollTargetIndex = index;
                        return elementInfo.element;
                    }
                    index ++;
                }
                currentScrollTargetIndex = index - 1;
                return scrollTargets.size ? [...scrollTargets.values()][currentScrollTargetIndex - 1].element : null;
            }
            case "scroll": {
                switch (action.direction) {
                    case "up": {
                        if (currentScrollTargetIndex - 1 >= 0) {
                            currentScrollTargetIndex --;
                        }
                        const targetElement = [...scrollTargets.values()][currentScrollTargetIndex].element;
                        scrollToElement(targetElement);
                        return targetElement;
                    }
                    case "down": {
                        if (currentScrollTargetIndex + 1 < scrollTargets.size) {
                            currentScrollTargetIndex ++;
                        }
                        const targetElement = [...scrollTargets.values()][currentScrollTargetIndex].element;
                        scrollToElement(targetElement);
                        return targetElement;
                    }
                    default: {
                        throw new Error("Unknown scroll direction " + action.direction);
                    }
                }
            }
            case "navigate": {
                const target = scrollTargets.get(action.id);
                if (target) {
                    currentScrollTargetIndex = [...scrollTargets.keys()].indexOf(action.id);
                    scrollToElement(target.element);
                    return target.element;
                }
                else {
                    throw new Error("Unknown scroll target " + action.id);
                }
            }
            default: {
                throw new Error("Unknown action type " + action.type);
            }
        }
    }, null, undefined);

    const [sectionIDsInCurrentPage, setSectionIDsInCurrentPage] = useState([]);

    useEffect(() => {
        setSectionIDsInCurrentPage([...scrollTargets.keys()].filter(key => scrollTargets.get(key).idType === 'section'));
    }, [scrollTargets]);

    return (
        <sectionIDsInCurrentPageContext.Provider value={sectionIDsInCurrentPage}>
            <ScrollTargetDispatchContext.Provider value={dispatchScrollTargets}>
                <CurrentScrollTargetContext.Provider value={{currentScrollTarget, dispatchCurrentScrollTarget}}>
                    {children}
                </CurrentScrollTargetContext.Provider>
            </ScrollTargetDispatchContext.Provider>
        </sectionIDsInCurrentPageContext.Provider>
    );
}