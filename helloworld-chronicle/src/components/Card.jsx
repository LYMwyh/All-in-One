import {children, createSignal, onMount, Show} from "solid-js";

export default function Card(props) {
    const resolved = children(() => props.children);
    let mouseSpotLight;

    const [spotLightMouseX, setSpotLightMouseX] = createSignal(0);
    const [spotLightMouseY, setSpotLightMouseY] = createSignal(0);
    const [putMask, setPutMask] = createSignal(false);

    onMount(() => {
        document.addEventListener("mousemove", (event) => {
            const mouseSpotLightAreaRect = mouseSpotLight.getBoundingClientRect();
            if (event.clientX >= mouseSpotLightAreaRect.x && event.clientX <= mouseSpotLightAreaRect.x + mouseSpotLightAreaRect.width && event.clientY >= mouseSpotLightAreaRect.y && event.clientY <= mouseSpotLightAreaRect.y + mouseSpotLightAreaRect.height) {
                setSpotLightMouseX(event.clientX - mouseSpotLightAreaRect.x);
                setSpotLightMouseY(event.clientY - mouseSpotLightAreaRect.y);
            }
            else if (spotLightMouseX() >= 0 || spotLightMouseY() >= 0){
                setSpotLightMouseX(-100);
                setSpotLightMouseY(-100);
            }
        })
    })

    return (
        <div ref={(rl) => mouseSpotLight = rl}
             class="relative w-full h-full p-10"
             style={{
                 "mask-mode": "luminance",
                 "mask-image": putMask() ? `radial-gradient(circle 100px at ${spotLightMouseX()}px ${spotLightMouseY()}px, white 50%, black 50%), radial-gradient(at 90% 10%, black 10%, white)` : "",
                 "mask-composite": "add",
             }}>
            <div class="relative w-full h-full text-white rounded-lg bg-radial-[at_99%_1%] from-sky-800 to-gray-800 flex flex-col gap-1">
                <div class="grow relative p-10">
                    {resolved()}
                </div>
                <div class="flex justify-between">
                    <Show when={putMask()}
                          fallback={
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="black"
                                   class="bg-white m-4 aspect-square w-fit h-fit px-4 py-2 text-lg font-bold border rounded-full shadow-[0_0_5px_#9ca3af] hover:opacity-90"
                                   onClick={() => setPutMask(!putMask())}
                                   viewBox="0 0 16 16">
                                  <path
                                      d="M2 6a6 6 0 1 1 10.174 4.31c-.203.196-.359.4-.453.619l-.762 1.769A.5.5 0 0 1 10.5 13h-5a.5.5 0 0 1-.46-.302l-.761-1.77a2 2 0 0 0-.453-.618A5.98 5.98 0 0 1 2 6m3 8.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1l-.224.447a1 1 0 0 1-.894.553H6.618a1 1 0 0 1-.894-.553L5.5 15a.5.5 0 0 1-.5-.5"/>
                              </svg>}>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="m-4 aspect-square w-fit h-fit px-4 py-2 text-lg font-bold border rounded-full shadow-[0_0_5px_#9ca3af] hover:brightness-200"
                             onClick={() => setPutMask(!putMask())}
                             viewBox="0 0 16 16">
                            <path
                                d="M2 6a6 6 0 1 1 10.174 4.31c-.203.196-.359.4-.453.619l-.762 1.769A.5.5 0 0 1 10.5 13a.5.5 0 0 1 0 1 .5.5 0 0 1 0 1l-.224.447a1 1 0 0 1-.894.553H6.618a1 1 0 0 1-.894-.553L5.5 15a.5.5 0 0 1 0-1 .5.5 0 0 1 0-1 .5.5 0 0 1-.46-.302l-.761-1.77a2 2 0 0 0-.453-.618A5.98 5.98 0 0 1 2 6m6-5a5 5 0 0 0-3.479 8.592c.263.254.514.564.676.941L5.83 12h4.342l.632-1.467c.162-.377.413-.687.676-.941A5 5 0 0 0 8 1"/>
                        </svg>
                    </Show>
                </div>
            </div>
        </div>
    )
}