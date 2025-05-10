import {ScrollTargetDispatchContext} from "@/context/ScrollTargetContext";
import {useContext, useEffect, useRef} from "react";

export default function Section({sectionID, className, style, children}) {
    const dispatch = useContext(ScrollTargetDispatchContext);
    const sectionRef = useRef(null);

    useEffect(() => {
        dispatch({
            type: "addScrollTarget",
            id: "sectionID-" + sectionID,
            idType: "section",
            element: sectionRef.current,
        });

        return () => {
            dispatch({
                type: "removeScrollTarget",
                id: "sectionID-" + sectionID,
            })
        }
    }, []);

    return (
        <section ref={sectionRef} className={className} style={style}>
            {children}
        </section>
    );
}