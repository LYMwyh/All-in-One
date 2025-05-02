import GithubIcon from "@/components/GithubIcon";

export default function Header() {
    return (
        <header className="p-6 flex gap-4 items-center justify-between justify-self-stretch flex-wrap">
            <div className="flex items-center shrink-0 mr-6 cursor-default">
                <span className="font-bold text-3xl tracking-tight">HelloWorld-er</span>
            </div>
            <nav className="grow flex flex-row gap-4 justify-start shrink-0 font-bold text-bright tracking-tight *:border-l-2 *:border-l-foreground *:px-2">
                <div className="hover:underline hover:underline-offset-2 hover:decoration-dotted hover:decoration-2">Index</div>
                <div className="hover:underline hover:underline-offset-2 hover:decoration-dotted hover:decoration-2">About</div>
            </nav>
            <div className="flex justify-end shrink-0">
                <a className="w-fit h-fit m-auto *:h-6" href="https://github.com/HelloWorld-er"><GithubIcon /></a>
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