import {Roboto_Condensed, Roboto_Mono} from "next/font/google";
import "./globals.css";
import ScrollTargetContextProvider from "@/context/ScrollTargetContext";
import HeaderHeightContextProvider from "@/context/HeaderContext";

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
            className={`${robotoCondensed.variable} ${robotoMono.variable} font-roboto-condensed antialiased bg-background text-foreground`}
        >
            <HeaderHeightContextProvider>
                <ScrollTargetContextProvider>
                    {children}
                </ScrollTargetContextProvider>
            </HeaderHeightContextProvider>
        </body>
        </html>
    );
}
