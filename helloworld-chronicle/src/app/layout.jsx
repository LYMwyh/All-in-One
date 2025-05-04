import {Roboto_Condensed, Roboto_Mono} from "next/font/google";
import "./globals.css";
import ScrollTargetContextProvider from "@/context/ScrollTargetContext";

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
            className={`${robotoCondensed.variable} ${robotoMono.variable} font-roboto-condensed antialiased px-30 bg-background text-foreground`}
        >
            <ScrollTargetContextProvider>
                {children}
            </ScrollTargetContextProvider>
        </body>
        </html>
    );
}
