
function backrndcolor(){
    document.body.style.backgroundColor = "lightgray";
}
function headcolor(){
    document.getElementById("heading").style.backgroundColor = "red";

}
function textcolor(){
    document.getElementById("ptext").style.backgroundColor = "yellow";
}
 cntText = "Proqramlaşdırma sahəsində bilik və təcrübə istifadə müddəti çox tez bitən məfhumdur.Bu gün əldə etdiyiniz bilik bir neçə il sonra istifadəyə yararsız hala gələbilər. Buna görə də sizin bir vəzifəniz də öz bilik portfolionuzu daimi yeniləmək olmalıdır.Bunun üçün kitabda verilən tövsiyələr"
 

 function countext(){
    say = cntText.length;
    alert(say);
 }

 function WordCount() { 
    sozsayi = cntText.split(" ").length ;
    alert(sozsayi);

  }