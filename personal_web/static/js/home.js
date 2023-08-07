document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('nav ul li a');
  links.forEach(link => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      const targetId = event.target.getAttribute('href');
      document.querySelector(targetId).scrollIntoView({ behavior: 'smooth' });
    });
  });
});



let img = document.querySelector('.img')
img.addEventListener('mouseover' , (el)=>el.currentTarget.style.width = '50%')
img.addEventListener('mouseout' , (el)=>el.currentTarget.style.width = '25%')
