function myfunc(a){
    if (typeof a == 'object') {
        alert("obyektdir")
    } else if(typeof a == 'number'){
        alert("ededdir")
    } else if (typeof a == 'string'){
        alert("metndir")
    }
}
myfunc(null)