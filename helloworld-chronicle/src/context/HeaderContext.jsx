'use client';

import {createContext, useState} from "react";

export const HeaderHeightContext = createContext(null);
export const HeaderHeightDispatchContext = createContext(null);

export default function HeaderHeightContextProvider({children}) {
    const [headerHeight, setHeaderHeight] = useState(null);

    return (
        <HeaderHeightContext.Provider value={headerHeight}>
            <HeaderHeightDispatchContext.Provider value={setHeaderHeight}>
                {children}
            </HeaderHeightDispatchContext.Provider>
        </HeaderHeightContext.Provider>
    );
}
