let img = document.querySelector('.img')
img.addEventListener('mouseover' , (el)=>el.currentTarget.style.width = '50%')
img.addEventListener('mouseout' , (el)=>el.currentTarget.style.width = '25%')
