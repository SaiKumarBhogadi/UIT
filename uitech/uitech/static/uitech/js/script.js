/*
$(document).ready(function () {
    $('.items').slick({
      dots: true,
      infinite: true,
      speed: 800,
      autoplay: true,
      autoplaySpeed: 2000,
      slidesToShow: 4,
      slidesToScroll: 4,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    });
  });


document.addEventListener('DOMContentLoaded', function() {
    function myFunction(button) {
      var parent = button.parentElement;
      var dots = parent.querySelector('.dots');
      var moreText = parent.querySelector('.more');
  
      if (dots.style.display === 'none') {
        dots.style.display = 'inline';
        button.textContent = 'Read more';
        moreText.style.display = 'none';
      } else {
        dots.style.display = 'none';
        button.textContent = 'Read less';
        moreText.style.display = 'inline';
      }
    }
  
    document.querySelectorAll('.myBtn').forEach(function(button) {
      button.addEventListener('click', function() {
        myFunction(this);
      });
    });
  });
*/

$(document).ready(function() {
    // Slick carousel initialization
    $('.items').slick({
      dots: true,
      infinite: true,
      speed: 800,
      autoplay: true,
      autoplaySpeed: 2000,
      slidesToShow: 4,
      slidesToScroll: 4,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    });
  
    // Read more/less button functionality
    function myFunction(button) {
      var parent = button.parentElement;
      var dots = parent.querySelector('.dots');
      var moreText = parent.querySelector('.more');
  
      if (dots.style.display === 'none') {
        dots.style.display = 'inline';
        button.textContent = 'Read more';
        moreText.style.display = 'none';
      } else {
        dots.style.display = 'none';
        button.textContent = 'Read less';
        moreText.style.display = 'inline';
      }
    }
  
    document.querySelectorAll('.myBtn').forEach(function(button) {
      button.addEventListener('click', function() {
        myFunction(this);
      });
    });
  });