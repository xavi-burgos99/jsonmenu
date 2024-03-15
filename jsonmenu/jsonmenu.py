import os

class JsonMenu:
  
	default_translations = {
		"ar": { "back": "عودة", "exit": "خروج", "invalid_option": "خيار غير صالح", "select_option": "اختر خيارًا", "press_enter": "اضغط على \"Enter\" للمتابعة..." },
		"ca": { "back": "Enrere", "exit": "Sortir", "invalid_option": "Opció no vàlida", "select_option": "Selecciona una opció", "press_enter": "Prem \"Enter\" per continuar..." },
		"de": { "back": "Zurück", "exit": "Beenden", "invalid_option": "Ungültige Option", "select_option": "Wählen Sie eine Option", "press_enter": "Drücken Sie \"Enter\", um fortzufahren..." },
		"en": { "back": "Back", "exit": "Exit", "invalid_option": "Invalid option", "select_option": "Select an option", "press_enter": "Press \"Enter\" to continue..." },
		"es": { "back": "Atrás", "exit": "Salir", "invalid_option": "Opción inválida", "select_option": "Selecciona una opción", "press_enter": "Presiona \"Enter\" para continuar..." },
		"fr": { "back": "Retour", "exit": "Sortie", "invalid_option": "Option invalide", "select_option": "Sélectionnez une option", "press_enter": "Appuyez sur \"Entrée\" pour continuer..." },
		"hi": { "back": "वापस", "exit": "निकास", "invalid_option": "अमान्य विकल्प", "select_option": "एक विकल्प चुनें", "press_enter": "जारी रखने के लिए \"Enter\" दबाएं..." },
		"it": { "back": "Indietro", "exit": "Uscita", "invalid_option": "Opzione non valida", "select_option": "Seleziona un'opzione", "press_enter": "Premi \"Invio\" per continuare..." },
		"ja": { "back": "戻る", "exit": "出口", "invalid_option": "無効なオプション", "select_option": "オプションを選択", "press_enter": "続行するには \"Enter\" キーを押してください..." },
		"ko": { "back": "뒤로", "exit": "출구", "invalid_option": "잘못된 옵션", "select_option": "옵션을 선택", "press_enter": "\"Enter\"를 눌러 계속하십시오..." },
		"nl": { "back": "Terug", "exit": "Afsluiten", "invalid_option": "Ongeldige optie", "select_option": "Selecteer een optie", "press_enter": "Druk op \"Enter\" om door te gaan..." },
		"pt": { "back": "Voltar", "exit": "Sair", "invalid_option": "Opção inválida", "select_option": "Selecione uma opção", "press_enter": "Pressione \"Enter\" para continuar..." },
		"ru": { "back": "Назад", "exit": "Выход", "invalid_option": "Неверный вариант", "select_option": "Выберите вариант", "press_enter": "Нажмите \"Enter\", чтобы продолжить..." },
		"sv": { "back": "Tillbaka", "exit": "Avsluta", "invalid_option": "Ogiltigt alternativ", "select_option": "Välj ett alternativ", "press_enter": "Tryck på \"Enter\" för att fortsätta..." },
		"tr": { "back": "Geri", "exit": "Çıkış", "invalid_option": "Geçersiz seçenek", "select_option": "Bir seçenek seçin", "press_enter": "Devam etmek için \"Enter\" tuşuna basın..." },
		"zh": { "back": "返回", "exit": "退出", "invalid_option": "无效选项", "select_option": "选择一个选项", "press_enter": "按 \"Enter\" 继续..." }
	}
 
	default_themes = {
		"ascii": { "tl": "+", "tr": "+", "cl": "+", "cr": "+", "bl": "+", "br": "+", "h": "-", "v": "|" },
		"unicode": { "tl": "┌", "tr": "┐", "cl": "├", "cr": "┤", "bl": "└", "br": "┘", "h": "─", "v": "│" },
		"bold": { "tl": "┏", "tr": "┓", "cl": "┣", "cr": "┫", "bl": "┗", "br": "┛", "h": "━", "v": "┃" },
		"double": { "tl": "╔", "tr": "╗", "cl": "╠", "cr": "╣", "bl": "╚", "br": "╝", "h": "═", "v": "║" },
		"rounded": { "tl": "╭", "tr": "╮", "cl": "├", "cr": "┤", "bl": "╰", "br": "╯", "h": "─", "v": "│" },
		"dotted": { "tl": "·", "tr": "·", "cl": "·", "cr": "·", "bl": "·", "br": "·", "h": "·", "v": ":" },
		"striped": { "tl": "─", "tr": "─", "cl": "─", "cr": "─", "bl": "─", "br": "─", "h": "─", "v": "│" }
	}

	def __init__(self, title: str, menu: list, options: dict = {}):
		self.options = options
		self.title = title
		if "back_menu" not in self.options:
			self.options["back_menu"] = None
		elif type(self.options["back_menu"]) is not JsonMenu:
			raise Exception("Back menu option must be a JsonMenu object")
		if "debug" not in self.options:
			self.options["debug"] = False
		elif type(self.options["debug"]) is not bool:
			raise Exception("Debug option must be a boolean")
		if "clear" not in self.options:
			self.options["clear"] = True
		elif type(self.options["clear"]) is not bool:
			raise Exception("Clear option must be a boolean")
		if "width" not in self.options:
			self.options["width"] = 31
		elif type(self.options["width"]) is not int:
			raise Exception("Width option must be an integer")
		if "language" not in self.options:
			self.options["language"] = "en"
		elif type(self.options["language"]) is not dict and type(self.options["language"]) is not str:
			raise Exception("Language option must be a dictionary or a string")
		if type(self.options["language"]) is str:
			if self.options["language"] not in self.default_translations:
				supported_languages = ", ".join(self.default_translations.keys())
				raise Exception(f"Language not supported. (The supported languages are: {supported_languages})")
			self.translations = self.default_translations[self.options["language"]]
		else:
			for key in self.options["language"]:
				if key not in self.default_translations["en"]:
					raise Exception("Invalid translation")
			for key in self.default_translations["en"]:
				if key not in self.options["language"]:
					if self.options["debug"]:
						print(f"\033[93mWarning: \033[90mThe translations are incomplete. Some messages will be displayed in English.\033[0m")
					break
			self.translations = self.options["language"]
		if "theme" not in self.options:
			self.options["theme"] = "unicode"
		elif type(self.options["theme"]) is not dict and type(self.options["theme"]) is not str:
			raise Exception("Theme option must be a dictionary or a string")
		if type(self.options["theme"]) is str:
			if self.options["theme"] not in self.default_themes:
				supported_themes = ", ".join(self.default_themes.keys())
				raise Exception(f"Theme not supported. (The supported themes are: {supported_themes})")
			self.theme = self.default_themes[self.options["theme"]]
		else:
			for key in self.options["theme"]:
				if key not in self.default_themes["ascii"]:
					raise Exception("Invalid theme")
			for key in self.default_themes["ascii"]:
				if key not in self.options["theme"]:
					if self.options["debug"]:
						print(f"\033[93mWarning: \033[90mThe theme is incomplete. Some characters will be displayed in ASCII.\033[0m")
					break
			self.theme = self.options["theme"]
		self.submenu_options = self.options.copy()
		self.submenu_options["back_menu"] = self
		self.load_menu(menu)

	def load_menu(self, menu: list):
		for i in range(len(menu)):
			if type(menu[i]) is not dict:
				raise Exception("Menu option must be a dictionary")
			if "label" not in menu[i]:
				raise Exception("Menu option must have a label")
			if "action" not in menu[i] and "submenu" not in menu[i]:
				raise Exception("Menu option must have an action or a submenu")
			if "submenu" in menu[i]:
				if type(menu[i]["submenu"]) is not list:
					raise Exception("Submenu must be a list")
				menu[i]["submenu"] = JsonMenu(menu[i]["label"], menu[i]["submenu"], self.submenu_options)
			if "action" in menu[i]:
				if not callable(menu[i]["action"]):
					raise Exception("Action must be a function")
		self.menu = menu
	
	def show(self, message: str = None):
		if self.options["clear"]:
			os.system('cls' if os.name == 'nt' else 'clear')
		print(f"\033[90m{self.theme['tl'] + self.theme['h'] * (self.options['width'] - 2) + self.theme['tr']}\033[0m")
		title = self.__fixStringWidth(self.title, self.options["width"] - 4, "center")
		print(f"\033[90m{self.theme['v']}\033[0m {title} \033[90m{self.theme['v']}\033[0m")
		print(f"\033[90m{self.theme['cl'] + self.theme['h'] * (self.options['width'] - 2) + self.theme['cr']}\033[0m")
		for i in range(len(self.menu)):
			label = self.__fixStringWidth(self.menu[i]["label"], self.options["width"] - 7)
			print(f"\033[90m{self.theme['v']}\033[0m \033[93m{i + 1}.\033[0m {label} \033[90m{self.theme['v']}\033[0m")
		if self.options["back_menu"] is not None:
			label = self.__fixStringWidth(self.__l('back'), self.options["width"] - 7)
			print(f"\033[90m{self.theme['v']}\033[0m \033[93m0.\033[0m {label} \033[90m{self.theme['v']}\033[0m")
		else:
			label = self.__fixStringWidth(self.__l('exit'), self.options["width"] - 7)
			print(f"\033[90m{self.theme['v']}\033[0m \033[93m0.\033[0m {label} \033[90m{self.theme['v']}\033[0m")
		print(f"\033[90m{self.theme['bl'] + self.theme['h'] * (self.options['width'] - 2) + self.theme['br']}\033[0m")
		print("")
		if message is not None:
			print(message + ". ", end="")
		selection = input(f"{self.__l('select_option')}: ")
		if not selection.isdigit():
			self.show(self.__l("invalid_option"))
			return
		if int(selection) < 0 or int(selection) > len(self.menu):
			self.show(self.__l("invalid_option"))
			return
		if int(selection) == 0:
			if self.options["back_menu"] is not None:
				self.options["back_menu"].show()
				return
			print("")
			exit()
		print("")
		print("")
		selection = int(selection) - 1
		if "action" in self.menu[selection]:
			self.menu[selection]["action"]()
		if "submenu" in self.menu[selection]:
			self.menu[selection]["submenu"].show()
		print("")
		input(self.__l("press_enter"))
		self.show()
  
	def __calcStringWidth(self, string: str) -> int:
		width = 0
		for c in string:
			if ord(c) < 128:
				width += 1
			else:
				width += 2
		return width

	def __calcLastCharWidth(self, string: str) -> int:
		c = string[::-1][0]
		if ord(c) < 128:
			return 1
		return 2

	def __cutString(self, string: str, width: int) -> str:
		cutString = ""
		cutWidth = 0
		for c in string:
			if ord(c) < 128:
				cutWidth += 1
			else:
				cutWidth += 2
			if cutWidth > width:
				break
			cutString += c
		return cutString

	def __fixStringWidth(self, string: str, width: int, align: str = "left") -> str:
		stringWidth = self.__calcStringWidth(string)
		offsetWidth = stringWidth - len(string)
		if stringWidth > width:
			if self.__calcLastCharWidth(string) == 2:
				string = self.__cutString(string, width - 2) + "… "
			else:
				string = self.__cutString(string, width - 1) + "…"
			stringWidth = self.__calcStringWidth(string)
			offsetWidth = stringWidth - len(string)
		if align == "left":
			return string.ljust(width - offsetWidth)
		if align == "right":
			return string.rjust(width - offsetWidth)
		if align == "center":
			return string.center(width - offsetWidth)

	def __l(self, key: str) -> str:
		if key not in self.translations:
			return self.default_translations["en"][key]
		return self.translations[key]
