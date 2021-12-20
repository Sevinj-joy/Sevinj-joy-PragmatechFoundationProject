// // EMR 1 DUYMESINI BASANDA
function backrndcolor(){
    document.body.style.backgroundColor = "lightgray";
}
// EMR 2 DUYMESINI BASANDA
function headcolor(){
    document.getElementById("heading").style.backgroundColor = "red";

}
// EMR 3 DUYMESINI BASANDA
function textcolor(){
    document.getElementById("ptext").style.backgroundColor = "yellow";
}
 cntText = "Proqramlaşdırma sahəsində bilik və təcrübə istifadə müddəti çox tez bitən məfhumdur.Bu gün əldə etdiyiniz bilik bir neçə il sonra istifadəyə yararsız hala gələbilər. Buna görə də sizin bir vəzifəniz də öz bilik portfolionuzu daimi yeniləmək olmalıdır.Bunun üçün kitabda verilən tövsiyələr"
 
//  EMR 4 DUYMESINI BASANDA
 function countext(){
    say = cntText.length;
    alert(say);
 }
//  EMR 5 DUYMESINI BASANDA

 function WordCount() { 
    sozsayi = cntText.split(" ").length ;
    alert(sozsayi);

}
//   EMR 6 DUYMESINI BASANDA
let text = document.getElementById("text");
sozsayi = text.split("proqramçı").length;

function soztap(){
    alert(sozsayi);
    
}