import {Roboto_Condensed, Roboto_Mono} from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";

const robotoCondensed = Roboto_Condensed({
    variable: "--font-roboto-condensed",
    subsets: ["latin"],
});

const robotoMono = Roboto_Mono({
    variable: "--font-roboto-mono",
    subsets: ["latin"],
});

export const metadata = {
    title: "HelloWorld Chronicle",
    description: "HelloWorld-er's personal website",
};

export default function RootLayout({children}) {
    return (
        <html lang="en">
        <body
            className={`${robotoCondensed.variable} ${robotoMono.variable} font-roboto-condensed antialiased h-lvh px-30 flex flex-col bg-background text-foreground`}
        >
            <Header/>
            <main className="grow *:h-full overflow-scroll [scrollbar-width:_none]">
                {children}
            </main>
        </body>
        </html>
    );
}
