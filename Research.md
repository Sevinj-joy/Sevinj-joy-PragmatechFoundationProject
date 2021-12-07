 # Araşdırma mətni 

 ## sual-   display:flex xüsusiyyətinin əsas neçə alt xüsusiyyəti var və bunlar nə işə yarayır?

 cavab- display:flex in asagidaki xususiyyleri vardir.

    flex-direction
    flex-wrap
    flex-flow
    justify-content
    align-items
    align-content

## sual- display:grid   xüsusiyyətinin alt xüsusiyyətləri hansılardır və qısaca nə işə yaradığını yazın

cavab- display:grid in xususiyyetleri asagidakilardir.

   grid-column-gap       (sutunlar arasi boslugu olculendirir.)
   grid-row-gap          (setirler arasi boslugu olculendirir .)
   grid-gap              (setir ve sutunlar arasi bosluqlar yaradir ,hansiki buda daha seliqeli goruntu elde etmeyimize komek edir.)
        
   grid-template-columns     ( sutunlar arasi bosluq yaradir)
   grid-row-gap              (setirler arasi bosluq yaradir.)
               
   grid-column-start  ( sutun bu emrle baslayir )
   grid-column-end  ( sutun bu emrle biterek birlesmesini yaradir)

   grid-row-start (setirin bu emirle baslayib)
   grid-row-end   (bu emrle biterek birlesmesini yaradir)
   
  ## sual- sizə görə flex və grid layout arasında ən əhəmiyyətli fərqlər hansılardır?
    
   cavab- Fikrimce Grid sistemi bize vaxta ve uzun kodlara qenaet etmemize ehemiyyet verir , beleki Biz setir ve sutun arasindaki boslugu veya setirin , sutunun istediyimiz movqede (ortada , axirda ) olmasini sadece 2 kodla heyata kecire bilirik.

  ## sual- display:inline-block,display:flex və display:grid xüsusiyyətlər hansı hallarda istifadə olunmalıdı və səbəbləri nələrdir?

   cavab-  
   display:inline-block  bu kod bize imkan veririr ki tag lar yan -yana duzule bilsin 

   display:flex  biz bu kod ve onun alt xusuiyyetleri  sayesinde realda  nizamli sekilde yan yana ve ya orta movqede , beraber mesafelerle arali dayana bilen qutular yarada bilirik.

   display:grid  Bu sistemle biz artiq cox rahatliqla table yarada , table in setir ve sutunlari onlarin yaratdiqlari movqelerle istediyimiz seliqeli goruntuye tez nail ola bilerik.

# Araşdırma mətni -page 2

## sual -display:inline və display:inline-block arasında fərqlər nədir?

Cavab-- displey: inline-block  ve display:inline elementleri yan-yana duzer. Aralarindaki ferq odurki display:inline olduqda elemente width ve height vermek olmur. Displey: inline-block  da ise eksine elemente width ve height vermek olur.



## sual -semantik veb nə deməkdir izah edin

cavab--Semantik veb (semantic web ) – informasiyanın maşın emalı üçün əlverişli formada təqdim edilməsi məqsədi ile yaranib. HTML-səhifələrə əsaslanan adi Veb-də informasiya səhifələrin mətnlərində yerləşir və insan onu brauzerin köməyilə əldə edir.



## sual-  HTML taq ve attribute arasındakı fərqlər nələrdir?


cavab-- HTML atributu (attribute ) HTML elementi haqqında əlavə məlumat verir.tag daxilindeki goruntunun sabit olmamasi hemcinin deyisdirilmesine komek edir. Bu yolla html tag forması və strukturu və ya xassələri dəyişdirilə bilər. 



## sual <!DOCTYPE html> nədir? Nə üçün istifadə edilir?

cavab-- Doctype (Sənəd Tipi Bəyannaməsi), İnternet səhifələrini hazırlayarkən səhifənizin hansı tipə aid olduğunu internet brauzerinə bildirmək üçün istifadə edilən bildiriş etiketidir.  Bu etiketlə siz internet brauzerlərinə səhifənizi tərtib edərkən hansı HTML versiyasından istifadə etdiyinizi bildirə və veb saytınızın bütün internet brauzerlərində ideal şəkildə göstərilməsini təmin edə bilərsiniz.



## css-də istifadə olunan inherit və initial ifadələrinin mənasını araşdırın yazın

cavab-- CSS de initial  her seyi reset edir baslangic xususiyyete qaytarir.Inherit ise mirasi davam etdirir. Vərəsəlik dəyəri təyin etdiyimiz elementin yuxarı elementinin dəyərlərini alir


## sual -HTML-in köhnə versiyaları ilə HTML5 arasında ən əhəmiyyətli fərqlər nələrdir?

cavab--
. HTML və HTML5 arasındakı əsas fərq ondan ibarətdir ki, nə audio, nə də video HTML-nin tərkib hissəsi sayıla bilməz, lakin hər ikisi HTML5-in ayrılmaz hissəsidir. HTML5 de video yerlesdirerken artqi hazir onun xususiyyetleri ile birlikde yerlesdirmek ucun <video controls> yazmaq kifayet edir


### Araşdırma mətni
Javascript variable qaynağından Javascript deyişənlər haqqında araşdırma edin. Araşdırma edərkən bu suallara cavab axtararaq araşdırın

### Sual -Dəyişən proqramlaşdırmada ya da Javascript-də nə üçün var ?
## cavab-- 
Deyisenler- Verilenleri saxlamaq ucun istifade olunur.

### Sual- Dəyişənləri adlandırarkən nələrə diqqət etmək lazımdır?
## Cavab--
Adda yalnız hərf, rəqəmlər və ya $ və _ simvolları ola biler.
Birinci simvol rəqəm olmamalıdır.

### Sual- Hansı ifadələri dəyişən adı olaraq vermək olmaz?
## Cavab--
abstract	arguments	await*	boolean
break	byte	case	catch
char	class*	const	continue
debugger	default	delete	do
double	else	enum*	eval
export*	extends*	false	final
finally	float	for	function
goto	if	implements	import*
in	instanceof	int	interface
let*	long	native	new
null	package	private	protected
public	return	short	static
super*	switch	synchronized	this
throw	throws	transient	true
try	typeof	var	void
volatile	while	with	yield
### Sual - let,var,const ifadələrinin menası nədir və aralarında fərqlər nədir?
## Cavab--
VAR açar sözü demək olar ki, let  ilə eynidir. O, həmçinin dəyişən elan edir, lakin bir qədər fərqlidir ve artiq istifade olunmur. Const deyiseni mensub edildiyi operator artiq basqa deyisen menimsedile bilmez , cunki const constant demekdir yeni deyismez sabit.

### Javascript data types qaynağından araşdırın.Aşağıdakı suallara cavab axtarın
## Sual - Hansı məlumat növləri var?

# cavab--
JavaScript-də səkkiz əsas məlumat növü var. 
1. Number type
2. String
3. Boolean (logical type)
4. The “null” value
5. The “undefined” value
6. Objects 
7. BigInt
8. Symbols

## Sual Məlumat növlərinin fərqləndirilməsi nəyə lazmdır?

## Sual -undefined,null,NaN ifadələrinin mənası nədir?
# Cavab
NULL , sadəcə olaraq “heç nə”, “boş” və ya “naməlum dəyər”i təmsil edir.
Undefined menasi  Müəyyən edilməmiş mənası "dəyər təyin edilmir" deməkdir.
NaN hesablama xətasını göstərir. Bu, səhv və ya qeyri-müəyyən bir riyazi əməliyyatın nəticəsidir.