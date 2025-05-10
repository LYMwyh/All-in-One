export function scrollToElement(element, offset = 0) {
    // element.scrollIntoView({
    //     behavior: "smooth",
    //     block: "start",
    // })

    if (!element) return;
    
    // Get the element's position relative to the document
    const elementPosition = element.getBoundingClientRect().top + window.scrollY;

    // Scroll to the adjusted position
    window.scrollTo({
        top: elementPosition - offset, // Apply the offset
        behavior: 'smooth', // Smooth scrolling effect
    });
}