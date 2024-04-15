// This automatically invoked function gives the buttons their rounded corners without setting rx values in CSS.
(function setGlowEffectRx() {
    const glowEffects = document.querySelectorAll('.glow-effect');

    // iterate over each button (represented by glow-effect class)
    glowEffects.forEach(glowEffect => {
        // store the rect objects (lines and blur)
        const glowLines = glowEffect.querySelectorAll('rect');
        // get the border-radius property of the button
        const rx = getComputedStyle(glowEffect).borderRadius;

        // iterate over each rect and set its rx equal to button border-radius
        glowLines.forEach(line => {
            line.setAttribute('rx', rx);
        })
    });
})();