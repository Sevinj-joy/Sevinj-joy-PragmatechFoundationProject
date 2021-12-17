// deyisenler
let Sekiller = [ ];

// sekillerin siyahisi

Sekiller [0] = 'Images/big-one.jpg';
Sekiller [1] = 'Images/forest.jpg';
Sekiller [2] = 'Images/Hopetoun_falls.jpg';
Sekiller [3] = 'Images/man-walking-dog.jpg';
Sekiller [4] = 'Images/natural-beauty.jpg';

// slider funksiyasi
function changeImage (){

    let x = document.getElementsByClassName("small-image").getAttribute("src"); 
    document.querySelector("big-image" ).innerHTML = x;
    
}
   
   


