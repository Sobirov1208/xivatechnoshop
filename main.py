import sqlite3
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from button import *
from aiogram.types import Message,CallbackQuery


#Configure logging
logging.basicConfig(level=logging.INFO)

#Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
Admin = 734754471

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	# conn = sqlite3.connect("user_info.db")
	# cursor = conn.cursor()
	# cursor.execute("""CREATE TABLE IF NOT EXISTS user(
	# 	id INTEGER
	# 	)""")
	# conn.commit()
	# tekshirish = message.chat.id
	# cursor.execute(f"SELECT id FROM user WHERE id = {tekshirish}")
	# data = cursor.fetchone()
	# if data is None:
	# 	user_id = [message.chat.id]

	# 	cursor.execute("INSERT INTO user VALUES (?)",user_id)
	# 	conn.commit()
	await message.reply(f"""β»οΈ Muddatli to'lovβ

π― Barcha turdaki maishiy texnikalar!!!
π Pasport+plastik karta
π Xar oy bo'lib to'lash  3, 6, 9 oy

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank""",reply_markup = menu)
# 		await bot.send_message(Admin,f"Ro'yhatga qo'shildi: \nusername: @{message.from_user.username}\nid: {message.from_user.id}")
# 	else:
# 		await message.reply("Siz ro'yhatdan o'tgansiz")
# @dp.message_handler(commands=["reklama"])
# async def send_welcome(message: types.Message):
# 	conn = sqlite3.connect("user_info.db")
# 	cursor = conn.cursor()
# 	cursor.execute("SELECT * FROM user ")
# 	data = cursor.fetchall()
# 	for dat in data:
# 		if dat[0]==734754471:
# 			pass
# 		else:
# 			user_id = dat[0]
# 			await bot.send_message(chat_id = user_id,text = "Bizning kanalimizga obuna bo'ling @")

@dp.message_handler(text="π± Telefon")
async def menular(message:Message):
	await message.answer("""Tovar turini tanlang ππ""",reply_markup = telefon)
#Samsung
@dp.callback_query_handler(text="Samsung")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Samsung)
	await call.message.delete()

@dp.callback_query_handler(text="A03S")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/A03S.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY A03S
πΎ 3 Gb/32 Gb 
πΈ 13 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 758.000 so'mdan
π 6 oyga 429.000 so'mdan
π 9 oyga 299.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="A01")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/A01.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY A01
πΎ 2 Gb/16 Gb 
πΈ 13 Mp 
π 3000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 589.000 so'mdan
π 6 oyga 327.000 so'mdan
π 9 oyga 233.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="A02")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/A02.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY A02
πΎ 2 Gb/32 Gb 
πΈ 13+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 604.000 so'mdan
π 6 oyga 335.000 so'mdan
π 9 oyga 238.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="A03")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/A03.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY A03
πΎ 4 Gb/64 Gb 
πΈ 13+2+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 800.000 so'mdan
π 6 oyga 444.000 so'mdan
π 9 oyga 316.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="A12")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/A12.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY A12
πΎ 3 Gb/32 Gb 
πΈ 48+5+2+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 790.000 so'mdan
π 6 oyga 439.000 so'mdan
π 9 oyga 312.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
	await call.message.answer_photo(
		photo =open('image/A12.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY A12
πΎ 3 Gb/64 Gb 
πΈ 48+5+2+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 907.000 so'mdan
π 6 oyga 504.000 so'mdan
π 9 oyga 359.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="M12")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/M12.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY M12
πΎ 3 Gb/32 Gb 
πΈ 48+5+2+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 819.000 so'mdan
π 6 oyga 455.000 so'mdan
π 9 oyga 324.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="A22")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/A22.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY A22
πΎ 4 Gb/64 Gb 
πΈ 48+8+2+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.099.000 so'mdan
π 6 oyga 610.000 so'mdan
π 9 oyga 434.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="A32")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/A32.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY A32
πΎ 4 Gb/64 Gb 
πΈ 64+8+5+5 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.325.000 so'mdan
π 6 oyga 736.000 so'mdan
π 9 oyga 523.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="A52")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/A52.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY A52
πΎ 4 Gb/128 Gb 
πΈ 64+12+5+5 Mp 
π 4500 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.741.000 so'mdan
π 6 oyga 967.000 so'mdan
π 9 oyga 688.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="S20FE")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/S20fe.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY S20FE
πΎ 6 Gb/128 Gb 
πΈ 12+8+12 Mp 
π 4500 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.453.000 so'mdan
π 6 oyga 1.363.000 so'mdan
π 9 oyga 967.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="S21")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/S21.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY S21
πΎ 8 Gb/128 Gb 
πΈ 64+12+12 Mp 
π 4000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 3.703.000 so'mdan
π 6 oyga 2.058.000 so'mdan
π 9 oyga 1.463.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="S21+")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/S21+.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY S21+
πΎ 8 Gb/128 Gb 
πΈ 64+12+12+10 Mp 
π 4800 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 4.341.000 so'mdan
π 6 oyga 2.412.000 so'mdan
π 9 oyga 1.715.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="Z FLIP3")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/Zflip3.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY Z FLIP3
πΎ 8 Gb/128 Gb 
πΈ 12+12 Mp 
π 3300 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 4.660.000 so'mdan
π 6 oyga 2.589.000 so'mdan
π 9 oyga 1.841.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="S21Ultra")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/S21ultra.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY S21 ULTRA
πΎ 8 Gb/256 Gb 
πΈ 108+12+10+10 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 5.395.000 so'mdan
π 6 oyga 2.998.000 so'mdan
π 9 oyga 2.132.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="Z Flod3")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/Zflod3.jpg','rb'),
		caption = """#Telefon, #Samsung

π± SAMSUNG GALAXY Z Flod3
πΎ 12 Gb/256 Gb 
πΈ 12+12+12 Mp 
π 4400 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 8.093.000 so'mdan
π 6 oyga 4.496.000 so'mdan
π 9 oyga 3.197.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_sam)
@dp.callback_query_handler(text="back2")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = telefon)
@dp.callback_query_handler(text="back1")
async def menular(call: CallbackQuery):
	await call.message.answer("""Orqaga qaytdik""",reply_markup = menu)
	await call.message.delete()
@dp.callback_query_handler(text="back5")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=Samsung,parse_mode="HTML")
	await call.message.delete()

#Vivo
@dp.callback_query_handler(text="Vivo")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Vivo)
	await call.message.delete()

@dp.callback_query_handler(text="Y1s")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/y1s.jpg','rb'),
		caption = """#Telefon, #VIVO

π± VIVO         Y1S
πΎ 2 Gb/32 Gb 
πΈ 13 Mp 
π 4000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 603.000 so'mdan
π 6 oyga 335.000 so'mdan
π 9 oyga 238.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_vivo)
@dp.callback_query_handler(text="Y12s")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/y12s.jpg','rb'),
		caption = """#Telefon, #VIVO

π± VIVO    Y12S
πΎ 3 Gb/32 Gb 
πΈ 13+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 785.000 so'mdan
π 6 oyga 436.000 so'mdan
π 9 oyga 310.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_vivo)
@dp.callback_query_handler(text="Y20")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/Y20.jpg','rb'),
		caption = """#Telefon, #VIVO

π± VIVO       Y20
πΎ 4 Gb/64 Gb 
πΈ 13+2+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 883.000 so'mdan
π 6 oyga 491.000 so'mdan
π 9 oyga 349.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_vivo)
@dp.callback_query_handler(text="Y31")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/y31.jpg','rb'),
		caption = """#Telefon, #VIVO

π± VIVO       Y31
πΎ 4 Gb/64 Gb 
πΈ 48+2+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 981.000 so'mdan
π 6 oyga 545.000 so'mdan
π 9 oyga 388.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_vivo)
@dp.callback_query_handler(text="Y53s")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/y53s.jpg','rb'),
		caption = """#Telefon, #VIVO

π± VIVO       Y53S
πΎ 8 Gb/128 Gb 
πΈ 64 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.349.000 so'mdan
π 6 oyga 750.000 so'mdan
π 9 oyga 533.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_vivo)
@dp.callback_query_handler(text="V21")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/v21.jpg','rb'),
		caption = """#Telefon, #VIVO

π± VIVO       V21
πΎ 8 Gb/128 Gb 
πΈ 64+8+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.036.000 so'mdan
π 6 oyga 1.131.000 so'mdan
π 9 oyga 805.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_vivo)
@dp.callback_query_handler(text="back4")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=Vivo,parse_mode="HTML")
	await call.message.delete()
@dp.callback_query_handler(text="back3")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = telefon)
#Redmi
@dp.callback_query_handler(text="Redmi")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Redmi)
	await call.message.delete()

@dp.callback_query_handler(text="9a")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/9a.jpg','rb'),
		caption = """#Telefon, #Redmi

π± REDMI 9A        
πΎ 2 Gb/32 Gb 
πΈ 13 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 623.000 so'mdan
π 6 oyga 346.000 so'mdan
π 9 oyga 246.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_redmi)
@dp.callback_query_handler(text="9c")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/9c.jpg','rb'),
		caption = """#Telefon, #Redmi

π± REDMI 9C
πΎ 4 Gb/128 Gb 
πΈ 13+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 834.000 so'mdan
π 6 oyga 463.000 so'mdan
π 9 oyga 330.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_redmi)
@dp.callback_query_handler(text="9t")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/9t.jpg','rb'),
		caption = """#Telefon, #Redmi

π± REDMI 9C
πΎ 4 Gb/64 Gb 
πΈ 48+8+2+2 Mp 
π 6000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 903.000 so'mdan
π 6 oyga 502.000 so'mdan
π 9 oyga 357.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_redmi)
@dp.callback_query_handler(text="10")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/note10.jpg','rb'),
		caption = """#Telefon, #Redmi

π± REDMI Note 10
πΎ 4 Gb/64 Gb 
πΈ 48+8+2+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.040.000 so'mdan
π 6 oyga 578.000 so'mdan
π 9 oyga 411.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_redmi)
@dp.callback_query_handler(text="10s")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/note10s.jpg','rb'),
		caption = """#Telefon, #Redmi

π± REDMI Note 10S
πΎ 4 Gb/64 Gb 
πΈ 64+8+2+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.202.000 so'mdan
π 6 oyga 668.000 so'mdan
π 9 oyga 475.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_redmi)
@dp.callback_query_handler(text="10promax")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/note10promax.jpg','rb'),
		caption = """#Telefon, #Redmi

π± REDMI Note 10 Pro Max
πΎ 8 Gb/128 Gb 
πΈ 108+8+5+2 Mp 
π 5020 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.447.000 so'mdan
π 6 oyga 804.000 so'mdan
π 9 oyga 572.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_redmi)
@dp.callback_query_handler(text="11lite")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/11lite.jpg','rb'),
		caption = """#Telefon, #Redmi

π± REDMI 11 Lite
πΎ 8 Gb/128 Gb 
πΈ 64+8+5 Mp 
π 4250 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.741.000 so'mdan
π 6 oyga 967.000 so'mdan
π 9 oyga 688.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_redmi)
@dp.callback_query_handler(text="11t")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/11t.jpg','rb'),
		caption = """#Telefon, #Redmi

π± REDMI Note 10 Pro Max
πΎ 8 Gb/128 Gb 
πΈ 108+8+5 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.085.000 so'mdan
π 6 oyga 1.158.000 so'mdan
π 9 oyga 824.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_redmi)
@dp.callback_query_handler(text="back7")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=Redmi,parse_mode="HTML")
	await call.message.delete()
@dp.callback_query_handler(text="back6")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = telefon)
#Iphone
@dp.callback_query_handler(text="Iphone")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Iphone)
	await call.message.delete()
@dp.callback_query_handler(text="11")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/11.jpg','rb'),
		caption = """#Telefon, #Iphone

π± Iphone 11
πΎ 4 Gb/64 Gb 
πΈ 12+12 Mp 
π 3100 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 3.189.000 so'mdan
π 6 oyga 1.771.000 so'mdan
π 9 oyga 1.260.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="11pro")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/11pro.jpg','rb'),
		caption = """#Telefon, #Iphone

π± Iphone 11 Pro
πΎ 4 Gb/64 Gb 
πΈ 12+12+12 Mp 
π 3000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 4.267.000 so'mdan
π 6 oyga 2.371.000 so'mdan
π 9 oyga 1.686.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="11promax")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/11promax.jpg','rb'),
		caption = """#Telefon, #Iphone

π± Iphone 11 Pro Max
πΎ 4 Gb/64 Gb 
πΈ 12+12+12 Mp 
π 4000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 4.758.000 so'mdan
π 6 oyga 2.643.000 so'mdan
π 9 oyga 1.880.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="xr")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/xr.jpg','rb'),
		caption = """#Telefon, #Iphone

π± Iphone XR 
πΎ 3 Gb/64 Gb 
πΈ 12 Mp 
π 3000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.845.000 so'mdan
π 6 oyga 1.580.000 so'mdan
π 9 oyga 1.124.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="se")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/se.jpg','rb'),
		caption = """#Telefon, #Samsung

π± Iphone SE
πΎ 3 Gb/64 Gb 
πΈ 12 Mp 
π 2800 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.207.000 so'mdan
π 6 oyga 1.226.000 so'mdan
π 9 oyga 872.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="12mini")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/12mini.jpg','rb'),
		caption = """#Telefon, #Iphone

π± Iphone 12 Mini
πΎ 4 Gb/64 Gb 
πΈ 12+12 Mp 
π 2300 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 3.335.000 so'mdan
π 6 oyga 1.853.000 so'mdan
π 9 oyga 1.318.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="12")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/12.jpg','rb'),
		caption = """#Telefon, #Iphone

π± Iphone 12
πΎ 4 Gb/64 Gb 
πΈ 12+12 Mp 
π 2800 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 3.875.000 so'mdan
π 6 oyga 2.153.000 so'mdan
π 9 oyga 1.531.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="12pro")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/12pro.jpg','rb'),
		caption = """#Telefon, #Iphone

π± IPhone 12 Pro
πΎ 6 Gb/128 Gb 
πΈ 12+12+12 Mp 
π 2800 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 5.395.000 so'mdan
π 6 oyga 2.997.000 so'mdan
π 9 oyga 2.132.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="12promax")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/12promax.jpg','rb'),
		caption = """#Telefon, #Iphone

π± Iphone 12 Pro Max
πΎ 6 Gb/128 Gb 
πΈ 12+12+12 Mp 
π 3700 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 5.984.000 so'mdan
π 6 oyga 3.324.000 so'mdan
π 9 oyga 2.364.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="13mini")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/13mini.jpg','rb'),
		caption = """#Telefon, #Iphone

π± Iphone 13 Mini
πΎ 4 Gb/128 Gb 
πΈ 12+12 Mp 
π 2400 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 4.169.000 so'mdan
π 6 oyga 2.316.000 so'mdan
π 9 oyga 1.647.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="13")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/13.jpg','rb'),
		caption = """#Telefon, #Iphone

π± Iphone 13
πΎ 4 Gb/128 Gb 
πΈ 12+12 Mp 
π 3200 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 4.670.000 so'mdan
π 6 oyga 2.589.000 so'mdan
π 9 oyga 1.841.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="13pro")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/13pro.jpg','rb'),
		caption = """#Telefon, #Iphone

π± Iphone 13 Pro
πΎ 6 Gb/128 Gb 
πΈ 12+12+12 Mp 
π 3100 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 6.131.000 so'mdan
π 6 oyga 3.406.000 so'mdan
π 9 oyga 2.422.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="13promax")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/13promax.jpg','rb'),
		caption = """#Telefon, #Iphone

π± Iphone 13 Pro Max
πΎ 6 Gb/128 Gb 
πΈ 12+12+12 Mp 
π 4400 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 6.769.000 so'mdan
π 6 oyga 3.760.000 so'mdan
π 9 oyga 2.674.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_iphone)
@dp.callback_query_handler(text="back8")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = telefon)
@dp.callback_query_handler(text="back9")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=Iphone,parse_mode="HTML")
	await call.message.delete()
#Honor
@dp.callback_query_handler(text="Honor")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Honor)
	await call.message.delete()
@dp.callback_query_handler(text="50")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/honor50.jpg','rb'),
		caption = """#Telefon, #Honor

π± Honor 50
πΎ 8 Gb/128 Gb 
πΈ 108+8+2+2 Mp 
π 4300 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.158.000 so'mdan
π 6 oyga 1.200.000 so'mdan
π 9 oyga 853.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_honor)
@dp.callback_query_handler(text="50lite")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/honor50lite.jpg','rb'),
		caption = """#Telefon, #Honor

π± Honor 50 Lite
πΎ 6 Gb/128 Gb 
πΈ 64+8+2+2 Mp 
π 4300 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.422.000 so'mdan
π 6 oyga 790.000 so'mdan
π 9 oyga 562.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_honor)
@dp.callback_query_handler(text="back10")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = telefon)
@dp.callback_query_handler(text="back11")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=Honor,parse_mode="HTML")
	await call.message.delete()
#Poco
@dp.callback_query_handler(text="Poco")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Poco)
	await call.message.delete()
@dp.callback_query_handler(text="m4")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/m4.jpg','rb'),
		caption = """#Telefon, #Poco

π± Poco M4
πΎ 6 Gb/128 Gb 
πΈ 50+8 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.373.000 so'mdan
π 6 oyga 763.000 so'mdan
π 9 oyga 543.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_poco)
@dp.callback_query_handler(text="f3")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/f3.jpg','rb'),
		caption = """#Telefon, #Poco

π± Poco F3
πΎ 8 Gb/256 Gb 
πΈ 48+8+5 Mp 
π 4520 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.011.000 so'mdan
π 6 oyga 1.117.000 so'mdan
π 9 oyga 795.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_poco)
@dp.callback_query_handler(text="back12")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = telefon)
@dp.callback_query_handler(text="back13")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=Poco,parse_mode="HTML")
	await call.message.delete()
#Tcl
@dp.callback_query_handler(text="Tcl")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =TCL)
	await call.message.delete()
@dp.callback_query_handler(text="20se")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/20se.jpg','rb'),
		caption = """#Telefon, #Tcl

π± Tcl 20SE
πΎ 4 Gb/64 Gb 
πΈ 48+5+2+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 834.000 so'mdan
π 6 oyga 463.000 so'mdan
π 9 oyga 330.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_tcl)
@dp.callback_query_handler(text="back14")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = telefon)
@dp.callback_query_handler(text="back15")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=TCL,parse_mode="HTML")
	await call.message.delete()
#Oppo
@dp.callback_query_handler(text="Oppo")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Oppo)
	await call.message.delete()
@dp.callback_query_handler(text="a72")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/a72.jpg','rb'),
		caption = """#Telefon, #Oppo

π± Oppo A72
πΎ 4 Gb/128 Gb 
πΈ 48+8+2+2 Mp 
π 5000 Mah
π² 1 yil kafolat servis

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.261.000 so'mdan
π 6 oyga 700.000 so'mdan
π 9 oyga 498.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_oppo)
@dp.callback_query_handler(text="back16")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = telefon)
@dp.callback_query_handler(text="back17")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=Oppo,parse_mode="HTML")
	await call.message.delete()
########==========maishiy texnika ============####

@dp.message_handler(text="π Maishiy texnika")
async def menular(message:Message):
	await message.answer("""Tovar turini tanlang ππ""",reply_markup = texnika)
#gaz plita
@dp.callback_query_handler(text="gaz plita")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Gaz_plitasi)
	await call.message.delete()

@dp.callback_query_handler(text="apetito50")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/apetito50.jpg','rb'),
		caption = """#Maishiy texnika, #Gaz plita

π Apetito 50

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 898.000 so'mdan
π 6 oyga 499.000 so'mdan
π 9 oyga 355.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gaz_plita)
@dp.callback_query_handler(text="apetito01")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/apetito01.jpg','rb'),
		caption = """#Maishiy texnika, #Gaz plita

π Apetito 01-G

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.207.000 so'mdan
π 6 oyga 670.000 so'mdan
π 9 oyga 477.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gaz_plita)
@dp.callback_query_handler(text="apetito02")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/apetito02.jpg','rb'),
		caption = """#Maishiy texnika, #Gaz plita

π Apetito 02-G

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.594.000 so'mdan
π 6 oyga 886.000 so'mdan
π 9 oyga 630.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gaz_plita)
@dp.callback_query_handler(text="milagrolite")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/milagroglite.jpg','rb'),
		caption = """#Maishiy texnika, #Gaz plita

π Milagro G Lite

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 863.000 so'mdan
π 6 oyga 480.000 so'mdan
π 9 oyga 341.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gaz_plita)
@dp.callback_query_handler(text="milagro01")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/milagro01.jpg','rb'),
		caption = """#Maishiy texnika, #Gaz plita

π Milagro 01-K

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.270.000 so'mdan
π 6 oyga 706.000 so'mdan
π 9 oyga 502.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gaz_plita)
@dp.callback_query_handler(text="milagro90")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/milagrof90g.jpg','rb'),
		caption = """#Maishiy texnika, #Gaz plita

π Milagro F90G inox

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.139.000 so'mdan
π 6 oyga 1.188.000 so'mdan
π 9 oyga 845.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gaz_plita)
@dp.callback_query_handler(text="back20")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Gaz_plitasi)
@dp.callback_query_handler(text="back19")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()

@dp.callback_query_handler(text="ferre6019")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/ferre6019.jpg','rb'),
		caption = """#Maishiy texnika, #Gaz plita

π Ferre 60 19W

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.207.000 so'mdan
π 6 oyga 671.000 so'mdan
π 9 oyga 477.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gaz_plita)

@dp.callback_query_handler(text="ferre604")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/ferre604.jpg','rb'),
		caption = """#Maishiy texnika, #Gaz plita

π Ferre 60 4PW

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.648.000 so'mdan
π 6 oyga 916.000 so'mdan
π 9 oyga 651.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gaz_plita)

@dp.callback_query_handler(text="ferre902")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/ferre902.jpg','rb'),
		caption = """#Maishiy texnika, #Gaz plita

π Ferre 90 2T

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.188.000 so'mdan
π 6 oyga 1.216.000 so'mdan
π 9 oyga 864.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gaz_plita)	

#Duxovka
@dp.callback_query_handler(text="mini duxovka")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Mini_duxovka)
	await call.message.delete()

@dp.callback_query_handler(text="md-3618 eco")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/md-3618eco.jpg','rb'),
		caption = """#Maishiy texnika, #Duxovka

π MD-3618 Eco

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 250.000 so'mdan
π 6 oyga 139.000 so'mdan
π 9 oyga 100.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_duxovka)
@dp.callback_query_handler(text="md-3618 lux")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/md-3618lux.jpg','rb'),
		caption = """#Maishiy texnika, #Duxovka

π MD-3618 Lux

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 358.000 so'mdan
π 6 oyga 199.000 so'mdan
π 9 oyga 142.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_duxovka)
@dp.callback_query_handler(text="md-4218 lux")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/md-4218lux.jpg','rb'),
		caption = """#Maishiy texnika, #Duxovka

π MD-4218 Lux

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 427.000 so'mdan
π 6 oyga 237.000 so'mdan
π 9 oyga 169.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_duxovka)
@dp.callback_query_handler(text="md-3614 elektr")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/md-3614elektr.jpg','rb'),
		caption = """#Maishiy texnika, #Duxovka

π MD-3614 Elektr plita

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 334.000 so'mdan
π 6 oyga 185.000 so'mdan
π 9 oyga 132.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_duxovka)


@dp.callback_query_handler(text="back22")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Mini_duxovka)
@dp.callback_query_handler(text="back21")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()


#Posudamoyka
@dp.callback_query_handler(text="posuda moyka")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Posudamoyka)
	await call.message.delete()

@dp.callback_query_handler(text="artel t21")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artelt21.jpg','rb'),
		caption = """#Maishiy texnika, #Posudamoyka

π Artel T21

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.036.000 so'mdan
π 6 oyga 1.131.000 so'mdan
π 9 oyga 804.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_moyka)

@dp.callback_query_handler(text="avalon dw 32t")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon32t.jpg','rb'),
		caption = """#Maishiy texnika, #Posudamoyka

π Avalon DW 32T

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.550.000 so'mdan
π 6 oyga 1.417.000 so'mdan
π 9 oyga 1.008.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_moyka)

@dp.callback_query_handler(text="avalon dw 1007")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon1007.jpg','rb'),
		caption = """#Maishiy texnika, #Posudamoyka

π Avalon DW 1007 inox

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.364.000 so'mdan
π 6 oyga 1.314.000 so'mdan
π 9 oyga 934.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_moyka)

@dp.callback_query_handler(text="avalon dw 14")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avl14d.jpg','rb'),
		caption = """#Maishiy texnika, #Posudamoyka

π Avalon DW 14D inox

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.860.000 so'mdan
π 6 oyga 1.589.000 so'mdan
π 9 oyga 1.130.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_moyka)

@dp.callback_query_handler(text="back24")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Posudamoyka)
@dp.callback_query_handler(text="back23")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()

#TV
@dp.callback_query_handler(text="televizor")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Tv)
	await call.message.delete()

@dp.callback_query_handler(text="artel24")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel24.jpg','rb'),
		caption = """#Maishiy texnika, #Tv

π Artel Led 24/9000
βοΈ	O'lchami : 24
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 500.000 so'mdan
π 6 oyga 278.000 so'mdan
π 9 oyga 198.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_tv)

@dp.callback_query_handler(text="artel32")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel32.jpg','rb'),
		caption = """#Maishiy texnika, #Tv

π Artel UA32H3200
βοΈ	O'lchami : 32
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 966.000 so'mdan
π 6 oyga 537.000 so'mdan
π 9 oyga 382.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_tv)

@dp.callback_query_handler(text="artel43")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel43.jpg','rb'),
		caption = """#Maishiy texnika, #Tv

π Artel UA43H1400
βοΈ	O'lchami : 43
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.432.000 so'mdan
π 6 oyga 796.000 so'mdan
π 9 oyga 566.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_tv)	

@dp.callback_query_handler(text="artel43s")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel43s.jpg','rb'),
		caption = """#Maishiy texnika, #Tv

π Artel UA43H3401 smart
βοΈ	O'lchami : 43
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.472.000 so'mdan
π 6 oyga 818.000 so'mdan
π 9 oyga 581.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_tv)	

@dp.callback_query_handler(text="artel50s")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel50s.jpg','rb'),
		caption = """#Maishiy texnika, #Tv

π Artel UA50H3401 smart
βοΈ	O'lchami : 50
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.031.000 so'mdan
π 6 oyga 1.128.000 so'mdan
π 9 oyga 802.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_tv)	

@dp.callback_query_handler(text="artel50sm")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel50sm.jpg','rb'),
		caption = """#Maishiy texnika, #Tv

π Artel UA50H3502 smart 4k
βοΈ	O'lchami : 50
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.193.000 so'mdan
π 6 oyga 1.218.000 so'mdan
π 9 oyga 866.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_tv)	

@dp.callback_query_handler(text="artel50sma")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel50sma.jpg','rb'),
		caption = """#Maishiy texnika, #Tv

π Artel 50AU20H smart LED 4K
βοΈ	O'lchami : 50
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.521.000 so'mdan
π 6 oyga 1.400.000 so'mdan
π 9 oyga 996.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_tv)

@dp.callback_query_handler(text="artel55")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel55.jpg','rb'),
		caption = """#Maishiy texnika, #Tv

π Artel A55 KU 5500
βοΈ	O'lchami : 55
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.958.000 so'mdan
π 6 oyga 1.643.000 so'mdan
π 9 oyga 1.169.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_tv)	

@dp.callback_query_handler(text="artel65")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel65.jpg','rb'),
		caption = """#Maishiy texnika, #Tv

π Artel 65A6502
βοΈ	O'lchami : 65
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 4.081.000 so'mdan
π 6 oyga 2.267.000 so'mdan
π 9 oyga 1.612.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_tv)

@dp.callback_query_handler(text="artel75")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel75.jpg','rb'),
		caption = """#Maishiy texnika, #Tv

π Artel 75/3502 LED ULTRA HD
βοΈ	O'lchami : 75
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 7.652.000 so'mdan
π 6 oyga 4.251.000 so'mdan
π 9 oyga 3.023.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_tv)	
@dp.callback_query_handler(text="back26")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Tv)
@dp.callback_query_handler(text="back25")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()
#Dazmol
@dp.callback_query_handler(text="dazmol")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Dazmol)
	await call.message.delete()

@dp.callback_query_handler(text="artel815")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel815.jpg','rb'),
		caption = """#Maishiy texnika, #Dazmol

π Artel ART-SI-815

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 98.000 so'mdan
π 6 oyga 55.000 so'mdan
π 9 oyga 39.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_dazmol)

@dp.callback_query_handler(text="artel5509")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel5509.jpg','rb'),
		caption = """#Maishiy texnika, #Dazmol

π Artel-5509

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 123.000 so'mdan
π 6 oyga 68.000 so'mdan
π 9 oyga 49.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_dazmol)

@dp.callback_query_handler(text="artel9518")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel9518.jpg','rb'),
		caption = """#Maishiy texnika, #Dazmol

π Artel ART-SI-9518

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 128.000 so'mdan
π 6 oyga 71.000 so'mdan
π 9 oyga 51.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_dazmol)

@dp.callback_query_handler(text="artel8008")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel8008.jpg','rb'),
		caption = """#Maishiy texnika, #Dazmol

π Artel ART-SI-8008

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 152.000 so'mdan
π 6 oyga 85.000 so'mdan
π 9 oyga 60.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_dazmol)

@dp.callback_query_handler(text="back28")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Dazmol)
@dp.callback_query_handler(text="back27")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()

#Go`sht maydalagich
@dp.callback_query_handler(text="go'sht maydalagich")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Gosht)
	await call.message.delete()

@dp.callback_query_handler(text="artel4130")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel4130.jpg','rb'),
		caption = """#Maishiy texnika, #Go'sht maydalagich

π Artel ART-MG-4130

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 245.000 so'mdan
π 6 oyga 136.000 so'mdan
π 9 oyga 97.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gosht)

@dp.callback_query_handler(text="artel3600")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel3600.jpg','rb'),
		caption = """#Maishiy texnika, #Go'sht maydalagich

π Artel ART MG 3600

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 373.000 so'mdan
π 6 oyga 207.000 so'mdan
π 9 oyga 147.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gosht)

@dp.callback_query_handler(text="artel3580")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel3580.jpg','rb'),
		caption = """#Maishiy texnika, #Go'sht maydalagich

π Artel ART MG 3580

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 446.000 so'mdan
π 6 oyga 248.000 so'mdan
π 9 oyga 176.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gosht)

@dp.callback_query_handler(text="avalon3840")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon3840.jpg','rb'),
		caption = """#Maishiy texnika, #Go'sht maydalagich

π Avalon-3840

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 540.000 so'mdan
π 6 oyga 300.000 so'mdan
π 9 oyga 213.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_gosht)

@dp.callback_query_handler(text="back30")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Gosht)
@dp.callback_query_handler(text="back29")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()	

#Konditsioner
@dp.callback_query_handler(text="kondinsioner")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Konditsioner)
	await call.message.delete()

@dp.callback_query_handler(text="artel12g")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artelgrand12.jpg','rb'),
		caption = """#Maishiy texnika, #Konditsioner

π Artel Grand 12HDM
βοΈ	O'lchami : 12
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.908.000 so'mdan
π 6 oyga 1.060.000 so'mdan
π 9 oyga 754.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_kon)

@dp.callback_query_handler(text="artel12i")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artelgrand12i.jpg','rb'),
		caption = """#Maishiy texnika, #Konditsioner

π Artel Grand 12 HDM Invertor
βοΈ	O'lchami : 12
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.207.000 so'mdan
π 6 oyga 1.226.000 so'mdan
π 9 oyga 872.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_kon)

@dp.callback_query_handler(text="artel18sh")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artelshahri18.jpg','rb'),
		caption = """#Maishiy texnika, #Konditsioner

π Artel 18HR Shahrisabz
βοΈ	O'lchami : 18
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.408.000 so'mdan
π 6 oyga 1.338.000 so'mdan
π 9 oyga 952.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_kon)	

@dp.callback_query_handler(text="artel24sh")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artelshahri24.jpg','rb'),
		caption = """#Maishiy texnika, #Konditsioner

π Artel 24HR Shahrisabz
βοΈ	O'lchami : 24
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.909.000 so'mdan
π 6 oyga 1.616.000 so'mdan
π 9 oyga 1.149.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_kon)	

@dp.callback_query_handler(text="avalon12")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artelavalon12.jpg','rb'),
		caption = """#Maishiy texnika, #Konditsioner

π Avalon 12
βοΈ	O'lchami : 12
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.639.000 so'mdan
π 6 oyga 1.466.000 so'mdan
π 9 oyga 1.043.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_kon)	

@dp.callback_query_handler(text="avalon24i")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artelavalon24i.jpg','rb'),
		caption = """#Maishiy texnika, #Konditsioner

π Avalon 24 Invertor
βοΈ	O'lchami : 24
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 5.793.000 so'mdan
π 6 oyga 3.218.000 so'mdan
π 9 oyga 2.289.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_kon)	

@dp.callback_query_handler(text="artel30hr")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel30hr.jpg','rb'),
		caption = """#Maishiy texnika, #Konditsioner

π Artel 30HR
βοΈ	O'lchami : 30
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 5.460.000 so'mdan
π 6 oyga 3.033.000 so'mdan
π 9 oyga 2.157.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_kon)

@dp.callback_query_handler(text="artel60hr")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel60hr.jpg','rb'),
		caption = """#Maishiy texnika, #Konditsioner

π Artel 60HR
βοΈ	O'lchami : 55
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 8.755.000 so'mdan
π 6 oyga 4.864.000 so'mdan
π 9 oyga 3.460.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_kon)

@dp.callback_query_handler(text="back32")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Konditsioner)
@dp.callback_query_handler(text="back31")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()	

#Kirmashina
@dp.callback_query_handler(text="kir mashina")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Kir_mashina)
	await call.message.delete()	

@dp.callback_query_handler(text="avtomat")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Avto)
	await call.message.delete()	

@dp.callback_query_handler(text="artel80k141")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel80k141.jpg','rb'),
		caption = """#Maishiy texnika, #Avto_kirmashina

π Artel 80 K 141

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.712.000 so'mdan
π 6 oyga 951.000 so'mdan
π 9 oyga 676.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_avto)

@dp.callback_query_handler(text="avalon1710")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon1710.jpg','rb'),
		caption = """#Maishiy texnika, #Avto_kirmashina

π Avalon 1710

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.158.000 so'mdan
π 6 oyga 1.200.000 so'mdan
π 9 oyga 853.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_avto)

@dp.callback_query_handler(text="avalon1510")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon1510.jpg','rb'),
		caption = """#Maishiy texnika, #Avto_kirmashina

π Avalon 1510

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.070.000 so'mdan
π 6 oyga 1.150.000 so'mdan
π 9 oyga 818.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_avto)

@dp.callback_query_handler(text="avalon1910")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon1910.jpg','rb'),
		caption = """#Maishiy texnika, #Avto_kirmashina

π Avalon 1910

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.658.000 so'mdan
π 6 oyga 1.477.000 so'mdan
π 9 oyga 1.050.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_avto)

@dp.callback_query_handler(text="back37")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Avto)
@dp.callback_query_handler(text="back36")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=Kir_mashina,parse_mode="HTML")
	await call.message.delete()

@dp.callback_query_handler(text="polavtomat")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Pol_avto)
	await call.message.delete()	

@dp.callback_query_handler(text="artel60")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/arteltc60.jpg','rb'),
		caption = """#Maishiy texnika, #Pol_avto_kirmashina

π Artel TC 60

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 545.000 so'mdan
π 6 oyga 303.000 so'mdan
π 9 oyga 215.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_pol)

@dp.callback_query_handler(text="artel100")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/arteltc100fp.jpg','rb'),
		caption = """#Maishiy texnika, #Pol_avto_kirmashina

π Artel TC 100 FP

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 770.000 so'mdan
π 6 oyga 428.000 so'mdan
π 9 oyga 304.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_pol)

@dp.callback_query_handler(text="artel45")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/arteltg45p.jpg','rb'),
		caption = """#Maishiy texnika, #Pol_avto_kirmashina

π Artel TG 45 P

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 456.000 so'mdan
π 6 oyga 254.000 so'mdan
π 9 oyga 180.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_pol)

@dp.callback_query_handler(text="artel120")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/arteltc120.jpg','rb'),
		caption = """#Maishiy texnika, #Pol_avto_kirmashina

π Artel TC 120

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 947.000 so'mdan
π 6 oyga 534.000 so'mdan
π 9 oyga 380.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_pol)

@dp.callback_query_handler(text="back35")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Pol_avto)
@dp.callback_query_handler(text="back34")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=Kir_mashina,parse_mode="HTML")
	await call.message.delete()	
@dp.callback_query_handler(text="back33")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()	
#Changyutgich
@dp.callback_query_handler(text="chan yutgich")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Changyutgich)
	await call.message.delete()	

@dp.callback_query_handler(text="artel0120")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel0120.jpg','rb'),
		caption = """#Maishiy texnika, #Changyutgich

π Artel VCB 0120

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 368.000 so'mdan
π 6 oyga 205.000 so'mdan
π 9 oyga 146.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_chang)

@dp.callback_query_handler(text="artel0220")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel0220.jpg','rb'),
		caption = """#Maishiy texnika, #Changyutgich

π Artel VCC 0220

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 442.000 so'mdan
π 6 oyga 245.000 so'mdan
π 9 oyga 175.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_chang)

@dp.callback_query_handler(text="avalon1840")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon1840.jpg','rb'),
		caption = """#Maishiy texnika, #Changyutgich

π Avalon VCC 1840

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 653.000 so'mdan
π 6 oyga 363.000 so'mdan
π 9 oyga 258.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_chang)

@dp.callback_query_handler(text="avalon4135")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon4135.jpg','rb'),
		caption = """#Maishiy texnika, #Changyutgich

π Avalon VCC 4135

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.045.000 so'mdan
π 6 oyga 581.000 so'mdan
π 9 oyga 413.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_chang)

@dp.callback_query_handler(text="back39")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Changyutgich )
@dp.callback_query_handler(text="back38")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()	

#Mikrovolnovka
@dp.callback_query_handler(text="mikrovolnovka")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Mikrovolnovka)
	await call.message.delete()	

@dp.callback_query_handler(text="artel20mx63")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel20mx63.jpg','rb'),
		caption = """#Maishiy texnika, #Mikrovolnovka

π Artel 20 MX 63

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 388.000 so'mdan
π 6 oyga 215.000 so'mdan
π 9 oyga 153.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_mikro)

@dp.callback_query_handler(text="artel23mx39")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel23mx39.jpg','rb'),
		caption = """#Maishiy texnika, #Mikrovolnovka

π Artel 23 MX 39

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 456.000 so'mdan
π 6 oyga 254.000 so'mdan
π 9 oyga 181.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_mikro)

@dp.callback_query_handler(text="artel0323")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel0323.jpg','rb'),
		caption = """#Maishiy texnika, #Mikrovolnovka

π Artel 0323

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 496.000 so'mdan
π 6 oyga 275.000 so'mdan
π 9 oyga 196.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_mikro)

@dp.callback_query_handler(text="avalon2588")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon2588.jpg','rb'),
		caption = """#Maishiy texnika, #Mikrovolnovka

π Avalon MBI 2588 inox

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.246.000 so'mdan
π 6 oyga 692.000 so'mdan
π 9 oyga 492.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_mikro)

@dp.callback_query_handler(text="back41")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Mikrovolnovka )
@dp.callback_query_handler(text="back40")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()	

#Blender
@dp.callback_query_handler(text="blender")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup = Blender)
	await call.message.delete()	

@dp.callback_query_handler(text="shivaki6700")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/shivaki6700.jpg','rb'),
		caption = """#Maishiy texnika, #Blender

π Shivaki HB 6700

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 182.000 so'mdan
π 6 oyga 101.000 so'mdan
π 9 oyga 72.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_blender)

@dp.callback_query_handler(text="artelhb815")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artelhb815.jpg','rb'),
		caption = """#Maishiy texnika, #Blender

π Artel Hb 815

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 211.000 so'mdan
π 6 oyga 117.000 so'mdan
π 9 oyga 84.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_blender)

@dp.callback_query_handler(text="artelhb201")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artelhb201.jpg','rb'),
		caption = """#Maishiy texnika, #Blender

π Artel HB 201

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 255.000 so'mdan
π 6 oyga 142.000 so'mdan
π 9 oyga 101.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_blender)

@dp.callback_query_handler(text="avalon5001")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon5001.jpg','rb'),
		caption = """#Maishiy texnika, #Blender

π Avalon HB 5001

π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 295.000 so'mdan
π 6 oyga 164.000 so'mdan
π 9 oyga 116.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_blender)

@dp.callback_query_handler(text="back43")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Blender )
@dp.callback_query_handler(text="back42")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()	

#Xolodilnik
@dp.callback_query_handler(text="xolodilnik")
async def menular(call: CallbackQuery):
	await call.message.answer("""Quyidagilardan birini tanlang""",reply_markup =Xolodilnik)
	await call.message.delete()

@dp.callback_query_handler(text="artel228")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel228.jpg','rb'),
		caption = """#Maishiy texnika, #Xolodilnik

π Artel HD 228
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.163.000 so'mdan
π 6 oyga 646.000 so'mdan
π 9 oyga 460.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_xolo)

@dp.callback_query_handler(text="artel341")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel341.jpg','rb'),
		caption = """#Maishiy texnika, #Xolodilnik

π Artel HD 341
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.506.000 so'mdan
π 6 oyga 837.000 so'mdan
π 9 oyga 595.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_xolo)

@dp.callback_query_handler(text="artel430")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel430.jpg','rb'),
		caption = """#Maishiy texnika, #Xolodilnik

π Artel HD 430
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.207.000 so'mdan
π 6 oyga 1.226.000 so'mdan
π 9 oyga 872.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_xolo)	

@dp.callback_query_handler(text="artel395")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel395.jpg','rb'),
		caption = """#Maishiy texnika, #Xolodilnik

π Artel HD 395 No Frost
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 1.894.000 so'mdan
π 6 oyga 1.052.000 so'mdan
π 9 oyga 748.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_xolo)	

@dp.callback_query_handler(text="avalon251")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon251.jpg','rb'),
		caption = """#Maishiy texnika, #Xolodilnik

π Avalon RF 251
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.477.000 so'mdan
π 6 oyga 1.376.000 so'mdan
π 9 oyga 979.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_xolo)	

@dp.callback_query_handler(text="avalon300")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon300.jpg','rb'),
		caption = """#Maishiy texnika, #Xolodilnik

π Avalon RF 300
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 3.041.000 so'mdan
π 6 oyga 1.690.000 so'mdan
π 9 oyga 1.202.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_xolo)	

@dp.callback_query_handler(text="avalon56")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/avalon56.jpg','rb'),
		caption = """#Maishiy texnika, #Xolodilnik

π Avalon RF 56
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 5.396.000 so'mdan
π 6 oyga 2.998.000 so'mdan
π 9 oyga 2.132.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_xolo)

@dp.callback_query_handler(text="artel390")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel390.jpg','rb'),
		caption = """#Maishiy texnika, #Xolodilnik

π Artel AFA 390
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.060.000 so'mdan
π 6 oyga 1.145.000 so'mdan
π 9 oyga 814.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_xolo)	

@dp.callback_query_handler(text="artel480")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artel480.jpg','rb'),
		caption = """#Maishiy texnika, #Xolodilnik

π Artel AFA 480
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.330.000 so'mdan
π 6 oyga 1.295.000 so'mdan
π 9 oyga 921.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_xolo)

@dp.callback_query_handler(text="artelhs390")
async def menular(call: CallbackQuery):
	await call.message.answer_photo(
		photo =open('image/artelhs390.jpg','rb'),
		caption = """#Maishiy texnika, #Xolodilnik

π Artel HS 390
π Muddatli to'lov. Banksiz, kafilsiz, oldindan to'lov yo'qπ₯
π§Ύ Pasport + Plastik Karta

π 3 oyga 2.016.000 so'mdan
π 6 oyga 1.120.000 so'mdan
π 9 oyga 797.000 so'mdan
β³ Π’ovarni 15 daqiqada olib ketasiz

βοΈ 99-042-2404

Admin: @bakhtiyorov_islom texnikalarni bugungi narxini bilish uchun adminga murojat qiling
π Manzil: Xiva shahri.
π’ ΠΡΠ»ΠΆΠ°Π»: Qishloq qurilish bank

""",parse_mode="HTML",reply_markup = Orqaga_xolo)	
@dp.callback_query_handler(text="back45")
async def menular(call: CallbackQuery):
	await call.message.answer("""Tovar turini tanlang ππ""",reply_markup = Xolodilnik)
@dp.callback_query_handler(text="back44")
async def menular(call: CallbackQuery):
	await call.message.answer("Orqaga qaytdik",reply_markup=texnika,parse_mode="HTML")
	await call.message.delete()

@dp.callback_query_handler(text="back46")
async def menular(call: CallbackQuery):
	await call.message.answer("""Orqaga qaytdik""",reply_markup = menu)
	await call.message.delete()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)