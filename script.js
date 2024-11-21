document.addEventListener('DOMContentLoaded', () => {
    // Interactive Visualization 1
    const vis1 = document.getElementById('interactive-vis1');
    vis1.innerHTML = '<p>Interactive visualization will go here.</p>';

    // Interactive Visualization 2
    const vis2 = document.getElementById('interactive-vis2');
    vis2.innerHTML = '<p>Interactive visualization will go here.</p>';
});

// JavaScript to add the pulse animation on hover
document.addEventListener('DOMContentLoaded', () => {
    const title = document.getElementById('title');

    // Add hover event listeners
    title.addEventListener('mouseover', () => {
        // Add pulse animation
        title.classList.add('animate__pulse');
    });

    title.addEventListener('mouseout', () => {
        // Remove pulse animation after hover ends
        title.classList.remove('animate__pulse');
    });
});
