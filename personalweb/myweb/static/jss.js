// script.js

document.addEventListener('DOMContentLoaded', function () {
    // Function to observe when elements enter the viewport
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            // If the element is visible, add the "show" class to trigger animation
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
                // Stop observing this element after it has animated
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 }); // Adjust threshold as necessary

    // Observe all elements with the 'animated-header' class
    const headers = document.querySelectorAll('.animated-header');
    headers.forEach(header => observer.observe(header));
});

