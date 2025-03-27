import {For, createSignal, onMount, createEffect, createMemo} from "solid-js";
import Card from "~/components/Card.jsx";

export default function Index() {
    const numberOfNavItems = 10;
    const [selectedNavItemIndex, setSelectedNavItemIndex] = createSignal(0);

    let navigationBar;

    onMount(() => {
        const selectedNavItem = createMemo(() => navigationBar.children[1].children[selectedNavItemIndex()] || null);
        createEffect(() => {
            if(selectedNavItem()) {
                scrollToCenterY(navigationBar, selectedNavItem());
            }
        })
    })

    function scrollToCenterY(container, item) {
        const containerRect = container.getBoundingClientRect();
        const itemRect = item.getBoundingClientRect();

        const scrollTop = itemRect.top - containerRect.top - containerRect.height / 2 + itemRect.height / 2;
        container.scrollBy({top: scrollTop, behavior: "smooth"});
    }

    let scrollingContainer;
    const scrollingPage = [
        <p class="card flex grow items-center justify-center text-2xl text-center">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda eaque eum ipsa
            ipsum
            mollitia numquam officiis quas qui quis, sequi ullam voluptatem. Adipisci
            consectetur
            dignissimos officia possimus quaerat unde vel.
        </p>,
        <p class="card flex grow items-center justify-center text-2xl text-center">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda eaque eum ipsa
            ipsum
            mollitia numquam officiis quas qui quis, sequi ullam voluptatem. Adipisci
            consectetur
            dignissimos officia possimus quaerat unde vel.
        </p>
    ]
    const [page, setPage] = createSignal(0);
    let lastScrollTop = 0;
    function scrollingInCard(currentScrollTop) {
        if (currentScrollTop > lastScrollTop && page() + 1 < scrollingPage.length) {
            setPage(page() + 1);
        }
        else if (currentScrollTop < lastScrollTop && page() - 1 >= 0) {
            setPage(page() - 1);
        }
        lastScrollTop = currentScrollTop;
    }

    onMount(() => {
        for (let i = 0; i < scrollingContainer.children.length; i ++) {
            scrollingContainer.children[i].classList.add("w-full", "h-full");
        }

        const selectedPageItem = createMemo(() => scrollingContainer.children[page()] || null)

        createEffect(() => {
            console.log(selectedPageItem())
            if (selectedPageItem()) {
                console.log("Scrolled")
                scrollToCenterY(scrollingContainer, selectedPageItem())
            }
        })
    })

    return (
        <div class="flex w-screen h-screen flex-row justify-between padding-1">
            <div class="flex flex-col gap-4 w-2/7 h-full bg-gray-800">
                <a href="/">
                    <div class="m-5 text-gray-100 text-4xl font-bold">
                        HelloWorld-er
                    </div>
                </a>
                <nav ref={(rl) => navigationBar = rl}
                     class="m-5 h-1/2 overflow-scroll [scrollbar-width:_none] [mask-image:_linear-gradient(to_bottom,_transparent,_black_40%,_black_calc(100%_-_40%),_transparent)] border-l border-gray-300 pl-4">
                    <div class="h-1/2"></div>
                    <ul class="max-w-80 h-fit flex flex-col flex-nowrap items-stretch gap-4">
                        <For each={[...Array(numberOfNavItems)]}>
                            {(item, index) => {
                                return (
                                    <li class={`${selectedNavItemIndex() === index() ? "selected" : ""} cursor-pointer group p-2 flex-shrink-0 flex items-center justify-center`}
                                        onClick={() => {
                                            setSelectedNavItemIndex(index());
                                        }}>
                                    <span
                                        class="w-66 h-12 flex items-center justify-center uppercase font-bold text-gray-300 group-[.selected]:border-b group-[.selected]:border-gray-300 group-[.selected]:[mask-image:_linear-gradient(to_left,_transparent,_black_15%,_black_calc(100%_-_15%),_transparent)]"> Who I am ? </span>
                                    </li>
                                )
                            }}
                        </For>
                    </ul>
                    <div class="h-1/2"></div>
                </nav>
                <div class="flex-grow flex flex-col-reverse m-5 gap-7">
                    <div class="text-gray-600 text-sm">
                        © 2025 HelloWorld-er. All rights reserved.
                    </div>
                    <div class="flex flex-row items-center text-gray-500 gap-4 font-bold">
                        <div class="border-b-3 border-dotted">Other Accounts:</div>
                        <div class="grow flex flex-row justify-between">
                            <a href="https://github.com/HelloWorld-er" target="_blank"
                               title="HelloWorld-er GitHub account">
                                <svg viewBox="0 0 16 16" aria-hidden="true" width="32" height="32">
                                    <path fill="white"
                                          d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z">
                                    </path>
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            {/*<svg xmlns="http://www.w3.org/2000/svg" class="">*/}

            {/*</svg>*/}
            <div class="grow bg-gradient-to-r from-gray-800 to-gray-950 to-20% flex items-center justify-center">
                <Card>
                    <div class="flex w-full h-full flex-col">
                        <h1 class="font-bold my-4 uppercase">Who I am ?</h1>
                        <div ref={(el) => scrollingContainer = el}
                             class="grow overflow-scroll [scrollbar-width:_none]"
                             onScroll={(e) => {
                                 e.preventDefault();
                                 scrollingInCard(e.currentTarget.scrollTop);
                             }}>
                            <For each={scrollingPage}>
                                {(item) => {
                                    return item;
                                }}
                            </For>
                        </div>
                    </div>
                </Card>
            </div>
        </div>
    )
}