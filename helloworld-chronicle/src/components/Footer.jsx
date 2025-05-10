export default function Footer({className}) {
    return (
        <footer className={"mx-auto md:mx-20 flex flex-col items-center justify-center rounded-t-md bg-slate-800 text-slate-200 p-4" + " " + className}>
            <div className="text-xs xl:text-md">
                © 2023 HelloWorld-er. All rights reserved.
            </div>
        </footer>
    );
}