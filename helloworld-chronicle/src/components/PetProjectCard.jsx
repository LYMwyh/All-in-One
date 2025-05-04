import React from "react";

export default function PetProjectCard({children}) {

    return (
        <div className="px-3 py-4 flex flex-col gap-2  bg-slate-800 rounded-xl">
            <div className="text-3xl font-bold my-4">
                {children.heading}
            </div>
            <p className="grow">
                {children.description}
            </p>
            <div className="flex flex-row gap-4 flex-wrap justify-items-start">
                {children.tags.map(tag => {
                    return (
                        <div key={tag} className="px-2 py-0.5 bg-dark-shadow rounded-md">{tag}</div>
                    );
                })}
            </div>
            <div className="flex flex-row flex-wrap">
                <span className="px-2 py-0.5 font-bold">{children.repositoryLabel}</span>
                <a className="px-2 py-0.5 text-shadow" href={children.repositoryLink}>
                    {children.repositoryIcon}
                </a>
            </div>
        </div>
    );
}