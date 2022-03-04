from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup


menu = ReplyKeyboardMarkup(
	keyboard = [
		[
		KeyboardButton(text="📱 Telefon"),
		],
		[
		KeyboardButton(text = "🔌 Maishiy texnika"),
		],
	],
	resize_keyboard=True
)

telefon = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "📱 Samsung",callback_data = "Samsung"),
			InlineKeyboardButton(text= "📱 Redmi",callback_data = "Redmi")
		],
		[
			InlineKeyboardButton(text= "📱 Iphone",callback_data = "Iphone"),
			InlineKeyboardButton(text= "📱 TCL",callback_data = "Tcl"),
			InlineKeyboardButton(text= "📱 Honor",callback_data = "Honor")
		],
		[
			InlineKeyboardButton(text= "📱 Poco",callback_data = "Poco"),
			InlineKeyboardButton(text= "📱 Vivo",callback_data = "Vivo"),
			InlineKeyboardButton(text= "📱 Oppo",callback_data = "Oppo")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back1"),
		],
	],
)


Samsung = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "📱 A01",callback_data = "A01"),
			InlineKeyboardButton(text= "📱 A02",callback_data = "A02"),
			InlineKeyboardButton(text= "📱 A03",callback_data = "A03")
		],
		[
			InlineKeyboardButton(text= "📱 A03S",callback_data = "A03S"),
			InlineKeyboardButton(text= "📱 A12",callback_data = "A12"),
			InlineKeyboardButton(text= "📱 M12",callback_data = "M12")
		],
		[
			InlineKeyboardButton(text= "📱 A22",callback_data = "A22"),
			InlineKeyboardButton(text= "📱 A32",callback_data = "A32"),
			InlineKeyboardButton(text= "📱 A52",callback_data = "A52")
		],
		[
			InlineKeyboardButton(text= "📱 S20FE",callback_data = "S20FE"),
			InlineKeyboardButton(text= "📱 S21",callback_data = "S21"),
			InlineKeyboardButton(text= "📱 S21+",callback_data = "S21+")
		],
		[
			InlineKeyboardButton(text= "📱 S21 Ultra",callback_data = "S21Ultra"),
			InlineKeyboardButton(text= "📱 Z Flip3",callback_data = "Z Flip3"),
			InlineKeyboardButton(text= "📱 Z Flod3",callback_data = "Z Flod3")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back2"),
		],

	],
)
Orqaga_sam=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back5")
		],	
	],
)

Vivo = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "📱 Y1S",callback_data = "Y1s"),
			InlineKeyboardButton(text= "📱 Y12S",callback_data = "Y12s"),
			InlineKeyboardButton(text= "📱 Y20",callback_data = "Y20")
		],
		[
			InlineKeyboardButton(text= "📱 Y31",callback_data = "Y31"),
			InlineKeyboardButton(text= "📱 Y53S",callback_data = "Y53s"),
			InlineKeyboardButton(text= "📱 V21",callback_data = "V21")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back3"),
		],

	],
)
Orqaga_vivo=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back4")
		],	
	],
)

Redmi = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "📱 Redmi 9A",callback_data = "9a"),
			InlineKeyboardButton(text= "📱 Redmi 9T",callback_data = "9t"),
			InlineKeyboardButton(text= "📱 Redmi 9C",callback_data = "9c")
		],
		[
			InlineKeyboardButton(text= "📱  Note 10",callback_data = "10"),
			InlineKeyboardButton(text= "📱  Note 10S",callback_data = "10s"),
			InlineKeyboardButton(text= "📱  Redmi 11T",callback_data = "11t")
		],
		[
			InlineKeyboardButton(text= "📱 Note 10 Pro Max",callback_data = "10promax"),
			InlineKeyboardButton(text= "📱 Mi 11 Lite",callback_data = "11lite")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back6"),
		],

	],
)
Orqaga_redmi=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back7")
		],	
	],
)
Iphone = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "📱 11",callback_data = "11"),
			InlineKeyboardButton(text= "📱 11 Pro",callback_data = "11pro"),
			InlineKeyboardButton(text= "📱 11 Pro Max",callback_data = "11promax")
		],
		[
			InlineKeyboardButton(text= "📱 XR",callback_data = "xr"),
			InlineKeyboardButton(text= "📱 SE",callback_data = "se"),
			InlineKeyboardButton(text= "📱 12 Mini",callback_data = "12mini")
		],
		[
			InlineKeyboardButton(text= "📱 12",callback_data = "12"),
			InlineKeyboardButton(text= "📱 12 Pro",callback_data = "12pro"),
			InlineKeyboardButton(text= "📱 12 Pro Max",callback_data = "12promax")
		],
		[
			InlineKeyboardButton(text= "📱 13 Mini",callback_data = "13mini"),
			InlineKeyboardButton(text= "📱 13",callback_data = "13"),
			InlineKeyboardButton(text= "📱 13 Pro",callback_data = "13pro")
		],
		[
			InlineKeyboardButton(text= "📱 13 Pro Max",callback_data = "13promax")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back8"),
		],

	],
)
Orqaga_iphone=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back9")
		],	
	],
)
Honor = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "📱 Honor 50",callback_data = "50"),
			InlineKeyboardButton(text= "📱 Honor 50 Lite",callback_data = "50lite")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back10"),
		],

	],
)
Orqaga_honor=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back11")
		],

	],
)
Poco = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "📱 Poco M4",callback_data = "m4"),
			InlineKeyboardButton(text= "📱 Poco F3",callback_data = "f3")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back12"),
		],

	],
)
Orqaga_poco=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back13")
		],

	],
)
TCL = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "📱 TCL 20SE",callback_data = "20se"),
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back14"),
		],

	],
)
Orqaga_tcl=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back15")
		],

	],
)
Oppo = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "📱 Oppo A72",callback_data = "a72"),
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back16"),
		],

	],
)
Orqaga_oppo=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back17")
		],

	],
)



texnika = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Gaz plita",callback_data = "gaz plita"),
			InlineKeyboardButton(text= "🔌 Televizor",callback_data = "televizor")
		],
		[
			InlineKeyboardButton(text= "🔌 Kir mashina",callback_data = "kir mashina"),
			InlineKeyboardButton(text= "🔌 Xolodilnik",callback_data = "xolodilnik")
		],
		[
			InlineKeyboardButton(text= "🔌 Mikrovolnovka",callback_data = "mikrovolnovka"),
			InlineKeyboardButton(text= "🔌 Blender",callback_data = "blender")
		],
		[
			InlineKeyboardButton(text= "🔌 Konditsioner",callback_data = "kondinsioner"),
			InlineKeyboardButton(text= "🔌 Chang yutgich",callback_data = "chan yutgich")
		],
		[
			InlineKeyboardButton(text= "🔌 Mini duxovka",callback_data = "mini duxovka"),
			InlineKeyboardButton(text= "🔌 Posuda moyka",callback_data = "posuda moyka")
		],
		[
			InlineKeyboardButton(text= "🔌 Go'sht maydalagich",callback_data = "go'sht maydalagich"),
			InlineKeyboardButton(text= "🔌 Dazmol",callback_data = "dazmol"),

		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back46"),
		],
	],
)

Gaz_plitasi = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Apetito 50",callback_data = "apetito50"),
			InlineKeyboardButton(text= "🔌 Apetito 01-G",callback_data = "apetito01"),
			InlineKeyboardButton(text= "🔌 Apetito 02-G",callback_data = "apetito02")
		],
		[
			InlineKeyboardButton(text= "🔌 Milagro Lite",callback_data = "milagrolite"),
			InlineKeyboardButton(text= "🔌 Milagro 01-K",callback_data = "milagro01"),
			InlineKeyboardButton(text= "🔌 Milagro F90G inox",callback_data = "milagro90")
		],
		[
			InlineKeyboardButton(text= "🔌 Ferre 60 19W",callback_data = "ferre6019"),
			InlineKeyboardButton(text= "🔌 Ferre 60 4PW",callback_data = "ferre604"),
			InlineKeyboardButton(text= "🔌 Ferre 90 2T",callback_data = "ferre902")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back19"),
		],

	],
)
Orqaga_gaz_plita=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back20")
		],	
	],
)

Mini_duxovka = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 MD-3618 Eco",callback_data = "md-3618 eco"),
			InlineKeyboardButton(text= "🔌 MD-3618 Lux",callback_data = "md-3618 lux")
		],
		[
			InlineKeyboardButton(text= "🔌 MD-4218 Lux",callback_data = "md-4218 lux"),
			InlineKeyboardButton(text= "🔌 MD-3614 Elektr",callback_data = "md-3614 elektr")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back21"),
		],

	],
)
Orqaga_duxovka=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back22")
		],	
	],
)

Posudamoyka = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Artel T21",callback_data = "artel t21"),
			InlineKeyboardButton(text= "🔌 Avalon DW 32T",callback_data = "avalon dw 32t")
		],
		[
			InlineKeyboardButton(text= "🔌 Avalon-DW 1007 inox",callback_data = "avalon dw 1007"),
			InlineKeyboardButton(text= "🔌 Avalon-DW 14D inox",callback_data = "avalon dw 14")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back23"),
		],

	],
)
Orqaga_moyka=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back24")
		],	
	],
)

Tv = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Artel 24 Led",callback_data = "artel24"),
			InlineKeyboardButton(text= "🔌 Artel 32",callback_data = "artel32")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel 43 smart",callback_data = "artel43s"),
			InlineKeyboardButton(text= "🔌 Artel 43",callback_data = "artel43")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel 50 smart",callback_data = "artel50s"),
			InlineKeyboardButton(text= "🔌 Artel 50 smart",callback_data = "artel50sm")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel 50 smart Led",callback_data = "artel50sma"),
			InlineKeyboardButton(text= "🔌 Artel 55",callback_data = "artel55")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel 65 Led",callback_data = "artel65"),
			InlineKeyboardButton(text= "🔌 Artel 75 Led",callback_data = "artel75")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back25"),
		],

	],
)
Orqaga_tv=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back26")
		],	
	],
)

Dazmol = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Artel SI 815",callback_data = "artel815"),
			InlineKeyboardButton(text= "🔌 Artel 5509",callback_data = "artel5509")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel SI 9518",callback_data = "artel9518"),
			InlineKeyboardButton(text= "🔌 Artel SI 8008",callback_data = "artel8008")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back27"),
		],

	],
)
Orqaga_dazmol=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back28")
		],	
	],
)

Gosht = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Artel MG 4130",callback_data = "artel4130"),
			InlineKeyboardButton(text= "🔌 Artel MG 3600",callback_data = "artel3600")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel MG 3580",callback_data = "artel3580"),
			InlineKeyboardButton(text= "🔌 Avalon-3840",callback_data = "avalon3840")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back29"),
		],

	],
)
Orqaga_gosht=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back30")
		],	
	],
)

Konditsioner = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Artel 12 Grand",callback_data = "artel12g"),
			InlineKeyboardButton(text= "🔌 Artel 12 Invertor",callback_data = "artel12i")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel 18 Shahrisabz",callback_data = "artel18sh"),
			InlineKeyboardButton(text= "🔌 Artel 24 Shahrisabz",callback_data = "artel24sh")
		],
		[
			InlineKeyboardButton(text= "🔌 Avalon 12",callback_data = "avalon12"),
			InlineKeyboardButton(text= "🔌 Avalon 24 Invertor",callback_data = "avalon24i")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel 30HR",callback_data = "artel30hr"),
			InlineKeyboardButton(text= "🔌 Artel 60HR",callback_data = "artel60hr")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back31"),
		],

	],
)
Orqaga_kon=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back32")
		],	
	],
)

Kir_mashina = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "Avtomat",callback_data = "avtomat")
		],
		[
			InlineKeyboardButton(text= " Pol Avtomat",callback_data = "polavtomat")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back33"),
		],

	],
)

Pol_avto = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Artel TC 60",callback_data = "artel60"),
			InlineKeyboardButton(text= "🔌 Artel TC 100",callback_data = "artel100")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel TG 45",callback_data = "artel45"),
			InlineKeyboardButton(text= "🔌 Artel TC 120",callback_data = "artel120")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back34"),
		],

	],
)
Orqaga_pol=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back35")
		],	
	],
)

Avto = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Artel 80K141",callback_data = "artel80k141"),
			InlineKeyboardButton(text= "🔌 Avalon 1710",callback_data = "avalon1710")
		],
		[
			InlineKeyboardButton(text= "🔌 Avalon 1510",callback_data = "avalon1510"),
			InlineKeyboardButton(text= "🔌 Avalon 1910",callback_data = "avalon1910")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back36"),
		],

	],
)
Orqaga_avto=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back37")
		],	
	],
)

Changyutgich = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Artel VCB 0120",callback_data = "artel0120"),
			InlineKeyboardButton(text= "🔌 Artel VCC 0220",callback_data = "artel0220")
		],
		[
			InlineKeyboardButton(text= "🔌 Avalon VCC 1840",callback_data = "avalon1840"),
			InlineKeyboardButton(text= "🔌 Avalon VCC 4135",callback_data = "avalon4135")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back38"),
		],

	],
)
Orqaga_chang=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back39")
		],	
	],
)

Mikrovolnovka = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Artel 20MX 63",callback_data = "artel20mx63"),
			InlineKeyboardButton(text= "🔌 Artel 23MX 39",callback_data = "artel23mx39")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel 0323",callback_data = "artel0323"),
			InlineKeyboardButton(text= "🔌 Avalon MBI 2588",callback_data = "avalon2588")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back40"),
		],

	],
)
Orqaga_mikro=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back41")
		],	
	],
)

Blender = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Shivaki HB 6700",callback_data = "shivaki6700"),
			InlineKeyboardButton(text= "🔌 Artel HB 815",callback_data = "artelhb815")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel HB 201",callback_data = "artelhb201"),
			InlineKeyboardButton(text= "🔌 Avalon HB 5001",callback_data = "avalon5001")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back42"),
		],

	],
)
Orqaga_blender=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back43")
		],	
	],
)

Xolodilnik = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text= "🔌 Artel HD 228",callback_data = "artel228"),
			InlineKeyboardButton(text= "🔌 Artel HD 341",callback_data = "artel341")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel HD 430",callback_data = "artel430"),
			InlineKeyboardButton(text= "🔌 Artel HD 395",callback_data = "artel395")
		],
		[
			InlineKeyboardButton(text= "🔌 Avalon RF 251",callback_data = "avalon251"),
			InlineKeyboardButton(text= "🔌 Avalon RF 300",callback_data = "avalon300")
		],
		[
			InlineKeyboardButton(text= "🔌 Avalon RF 56",callback_data = "avalon56"),
			InlineKeyboardButton(text= "🔌 Artel AFA 390",callback_data = "artel390")
		],
		[
			InlineKeyboardButton(text= "🔌 Artel AFA 480",callback_data = "artel480"),
			InlineKeyboardButton(text= "🔌 Artel HS 390 ",callback_data = "artelhs390")
		],
		[
			InlineKeyboardButton(text = "Orqaga" ,callback_data = "back44"),
		],

	],
)
Orqaga_xolo=InlineKeyboardMarkup(
		inline_keyboard = [
		[
			InlineKeyboardButton(text = "Orqaga",callback_data = "back45")
		],	
	],
)