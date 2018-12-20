	for ranga,count in zip((vozrostanieNum),range(0,10)):
			
			#instagram = list1
			#instagram = types.InlineKeyboardMarkup()
			for name in info['restoran']:
				if ranga == name['range']:
					if ranga < 1:
						a = round(ranga,3)
						a = 1000 * a
					#	but_instagram = types.InlineKeyboardButton(text="instagram", url=name['instagram'] )
					#	instagram.add(but_instagram)
						
						bot.send_message(c.message.chat.id, (("%s.%s,%s \n %s \n Номер: %s \n Оценка: %s из 5 баллов \n адрес:%s \n Instagram:%s \n от вас %s метрах,")%(count,name['name'],name['vid'],name['worktime'],name['phone'],name['оценка'],name['adress'],name['instagram'],a)))
					else:
					#	but_instagram = types.InlineKeyboardButton(text="instagram", url=name['instagram'] )
					#	instagram.add(but_instagram)
						bot.send_message(c.message.chat.id, (("%s.%s,%s \n %s \n Номер: %s \n Оценка: %s из 5 баллов \n адрес:%s \n Instagram:%s \n от вас %s км")%(count,name['name'],name['vid'],name['worktime'],name['phone'],name['оценка'],name['adress'],name['instagram'],round(ranga,2))))
				
		#	count += 1

		bron = types.InlineKeyboardMarkup()
		but_bron_1 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		newrange = 0
		for ranga in range(0,len(vozrostanieNum)-1):
			for name in info['restoran']:
				if ranga == name['range']:
					if ranga < 1:
						print(vozrostanieNum[x],'')

			
		but_bron_2 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_3 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_4 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_5 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_6 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_7 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_8 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_9 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_10 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		bron.add(but_bron_1,but_bron_2,but_bron_3,but_bron_4,but_bron_5,but_bron_6,but_bron_7,but_bron_8,but_bron_9,but_bron_10)
				
		bot.send_message(c.message.chat.id, "Хотите забронировать место в одном из этих ресторанов?", reply_markup=bron)
		#bot.send_message(c.message.chat.id, '')
		
		#but_3 = types.InlineKeyboardButton(text="да", callback_data="да")
		#but_4 = types.InlineKeyboardButton(text="нет", callback_data="нет")
		#bron.add(but_3,but_4)
		#bot.send_message(c.message.chat.id, "хотите встать в очередь?")#, reply_markup=bron)
		#ожидамое количество людей в очереди
	print (vozrostanieNum)

# We want to keep checking for updates. So this must be a never ending loop





	#------------------------



		'''
		for ranga in range(0,len(vozrostanieNum)-1):
			for name in info['restoran']:
				if ranga == name['range']:
					if ranga < 1:
						print(vozrostanieNum[x],'')
		for ranga,count in zip((vozrostanieNum),range(0,1)):
			
			#instagram = list1
			#instagram = types.InlineKeyboardMarkup()
			for name in info['restoran']:
				if ranga == name['range']:
					if ranga < 1:
						a = round(ranga,3)
						a = 1000 * a
					#	but_instagram = types.InlineKeyboardButton(text="instagram", url=name['instagram'] )
					#	instagram.add(but_instagram)
						but_bron_1 = types.InlineKeyboardButton(text="забронировать", callback_data="брон1")
						bot.send_message(c.message.chat.id, (("%s.%s,%s \n %s \n Номер: %s \n Оценка: %s из 5 баллов \n адрес:%s \n Instagram:%s \n от вас %s метрах,")%(count,name['name'],name['vid'],name['worktime'],name['phone'],name['оценка'],name['adress'],name['instagram'],a)), replay_markup=bron)
					else:
					#	but_instagram = types.InlineKeyboardButton(text="instagram", url=name['instagram'] )
					#	instagram.add(but_instagram)
						bot.send_message(c.message.chat.id, (("%s.%s,%s \n %s \n Номер: %s \n Оценка: %s из 5 баллов \n адрес:%s \n Instagram:%s \n от вас %s км")%(count,name['name'],name['vid'],name['worktime'],name['phone'],name['оценка'],name['adress'],name['instagram'],round(ranga,2))))
'''
			"""
		but_bron_2 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_3 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_4 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_5 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_6 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_7 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_8 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_9 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		but_bron_10 = types.InlineKeyboardButton(text="№1", callback_data="брон")
		bron.add(but_bron_1,but_bron_2,but_bron_3,but_bron_4,but_bron_5,but_bron_6,but_bron_7,but_bron_8,but_bron_9,but_bron_10)
				"""
		bot.send_message(c.message.chat.id, "Хотите забронировать место в одном из этих ресторанов?", reply_markup=bron)
		#bot.send_message(c.message.chat.id, '')
		
		#but_3 = types.InlineKeyboardButton(text="да", callback_data="да")
		#but_4 = types.InlineKeyboardButton(text="нет", callback_data="нет")
		#bron.add(but_3,but_4)
		#bot.send_message(c.message.chat.id, "хотите встать в очередь?")#, reply_markup=bron)
		#ожидамое количество людей в очереди
	print (vozrostanieNum)

# We want to keep checking for updates. So this must be a never ending loop





	#------------------------





bot.polling(none_stop=True) 

	#--------------------