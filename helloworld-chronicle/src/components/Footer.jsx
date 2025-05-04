export default function Footer({className}) {
    return (
        <footer className={"flex flex-col items-center justify-center rounded-md bg-slate-800 text-slate-200 p-4" + " " + className}>
            <div className="text-sm">
                © 2023 HelloWorld-er. All rights reserved.
            </div>
        </footer>
    );
}