//document.addEventListener("DOMContentLoaded", function() {
   // const menuIcon = document.getElementById("menu-icon");
   // const navbarList = document.getElementById("navbar-list");

   // menuIcon.addEventListener("click", function() {
     //   navbarList.classList.toggle("show"); // Toggle the visibility of the list when clicked
      //  menuIcon.classList.toggle("active"); // Toggle the active state for the icon
   // });
//});


//function removeNavbar() {
   // const navbar = document.querySelector('.Navbar');
    //navbar.classList.toggle('hidden');
//}


// const menuIcon = document.getElementById('menu-icon');
// const navbarList = document.getElementById('navbar-list');
// const closeBtn = document.getElementById('close-btn');

// // Toggle navbar visibility when the hamburger icon is clicked
// menuIcon.addEventListener('click', () => {
//     navbarList.classList.toggle('show'); // Toggles the "show" class
// });

// Close navbar when the close (X) button is clicked
// closeBtn.addEventListener('click', () => {
//     navbarList.classList.remove('show'); 
   
// });

 // Removes the "show" class







 document.addEventListener("DOMContentLoaded", function() {
    const menuIcon = document.getElementById("menu-icon");
    const navbarList = document.getElementById("navbar-list");
    const closeBtn = document.getElementById("close-btn");
    const navbar = document.querySelector('.Navbar');

    if (menuIcon && navbarList && closeBtn && navbar) {
        // Ensure the navbar and list are hidden by default when the page loads
        navbarList.classList.remove('show');  // Hide the list initially

        // Toggle the navbar visibility when the menu icon is clicked
        menuIcon.addEventListener("click", function() {
            navbar.classList.toggle("show");
            navbarList.classList.toggle("show");
            menuIcon.classList.toggle("active");
        });

        // Close the navbar when the close button (X) is clicked
        closeBtn.addEventListener("click", function() {
            navbar.classList.remove("show");
            navbarList.classList.remove("show");
            menuIcon.classList.remove("active");
        });
    } else {
        console.error("One or more elements not found in the DOM.");
    }
});



  const currentyear = new Date().getFullYear()

  document.getElementById('current-year').textContent=currentyear
