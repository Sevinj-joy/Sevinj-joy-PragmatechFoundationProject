// let ad =prompt('Adinizi daxil edin')
// let soyad =prompt('Soyadinizi daxil edin')
// let yas = prompt('Yasinizi daxil edin')


// function checktype (a){
//     if (typeof a =='number' ){
//         return String(a).length
//      }  else if (typeof a =='string') {
//         alert('siz metn daxil etmisiniz')
//     }else if (typeof a =='object'){
//         alert('siz obyekt daxil etmisiniz')
//     }
// }checktype(null)

let a = prompt('Melumati daxil edin')

function checktype (a){
        if (typeof a =='number' ){
        let numArr =[]
        for( let a of Number){
            if( String(a).length == 2)
            numArr.push(a)

        }
        alert("2 reqemli eded")
           
      }  else if (typeof a =='string') {
       
       }else if (typeof a =='object'){
       alert('siz obyekt daxil etmisiniz')
        }
     }