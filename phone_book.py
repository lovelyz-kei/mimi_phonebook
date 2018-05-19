class phoneBookItem:
	def __init__(self, name, number, email, group):
		self.name = name
		self.number = number
		self.email = email
		self.group = group

	def printDetail(self):
		print("이름 : " + self.name)
		print("번호 : " + self.number)
		print("이메일 : " + self.email)
		print("그룹 : " + self.group)

class phoneBook:
	def __init__(self):
		self.itemList = []

	def __init__(self, itemList):
		self.itemList = itemList

	def selectMenu(self):
		print("1. 연락처 등록")
		print("2. 연락처 수정")
		print("3. 연락처 삭제")
		print("4. 연락처 검색")
		print("5. 연락처 전체, 그룹 보기")
		print("0. 프로그램 종료")
		print("메뉴 선택 : ")
		return input()

	def selectGroupNum(self):
		print("1. 가족")
		print("2. 친구")
		print("3. 직장")
		print("4. 기타")
		print("그룹 선택 : ")
		return input()

	def groupNumToGroup(self, groupNum):
		if groupNum == 1:
			return "가족"
		elif groupNum == 2:
			return "친구"
		elif groupNum == 3:
			return "직장"
		elif groupNum == 4:
			return "기타"

	def findIdx(self, number):
		for idx, val in enumerate(self.itemList):
			if val.number == number:
				return idx
		return None


	def addItem(self):
		print("저장할 이름을 등록해주세요.")
		name = input()
		
		while True:
			print(name + "의 번호는 무엇입니까? '-' 없이 등록바랍니다.")
			number = input()
			if self.findIdx(number) is not None:
				print("이미 등록되어 있는 번호입니다.")
				continue
			if number.count("-") != 0:
				print("-을 넣지 말고 입력해주세요.")
			else:
				break

		while True:
			print(name + "의 이메일은 무엇입니까?")
			email = input()
			if email.count("@") != 1:
				print("이메일 형식을 지켜주세요")
			else:
				break

		while True:
			groupNum = int(self.selectGroupNum())

			if groupNum >= 1 and groupNum <= 4:
				group = self.groupNumToGroup(groupNum)
				break
			else:
				print("1~4의 값을 입력해주세요.")

		newItem = phoneBookItem(name, number, email, group)
		self.itemList.append(newItem)
		newItem.printDetail()

	def modifyItem(self):
		print("수정할 항목의 전화번호를 입력해주세요.")
		number = input()

		targetIdx = self.findIdx(number)
		
		if targetIdx is None:
			print("입력하신 전화번호에 해당하는 항목이 없습니다.")
			return
		else:
			targetItem = self.itemList[targetIdx]
			while True:
				targetItem.printDetail()
				print("수정하실 항목을 선택하세요.")
				print("1. 이름")
				print("2. 번호")
				print("3. 이메일")
				print("4. 그룹")
				print("항목 선택 : ")
				selectNum = input()

				if selectNum == "1":
					print("수정할 이름을 입력하세요 : ")
					newName = input()
					targetItem.name = newName
				elif selectNum == "2":
					while True:
						print("수정할 번호를 입력하세요 : ")
						newNumber = input()

						if newNumber.count("-") != 0:
							print("'-'을 넣지 말고 입력해주세요.")
						else:
							break
						targetItem.number = newNumber
				elif selectNum == "3":
					while True:
						print("수정할 이메일을 입력하세요 : ")
						newEmail = input()

						if newEmail.count("@") != 1:
							print("이메일 형식에 맞게 입력해주세요.")
						else:
							targetItem.email = newEmail
							break
				elif selectNum == "4":
					while True:
						print("수정할 그룹 번호를 입력하세요.")
						groupNum = self.selectGroupNum()

						if groupNum >= 1 and groupNum <= 4:
							group = self.groupNumToGroup(groupNum)
							targetItem.group = group
							break
						else:
							print("1~4의 값을 입력해주세요.")
				else:
					print("1~4의 값을 입력해주세요.")
					continue

				break

	def deleteItem(self):
		if len(self.itemList) == 0:
			print("저장된 전화번호가 없습니다.")
			return

		print("삭제할 항목의 전화번호를 입력해주세요. : ")
		targetNum = input()

		targetIdx = findIdx(targetNum)
		if targetIdx is None:
			print("입력하신 전화번호에 해당하는 항목이 없습니다.")
			return

		targetItem = self.itemList[targetIdx]
		targetItem.printDetail()
		print("위의 정보가 삭제됩니다.")
		del targetItem

	def searchItem(self):
		if len(self.itemList) == 0:
			print("저장된 전화번호가 없습니다.")
			return

		while True:
			print("이름과 전화번호 중 어느 것으로 검색하시겠습니까?")
			print("1. 이름으로 검색")
			print("2. 번호로 검색")

			searchType = input()
			hasFound = False

			if searchType == "1":
				print("누구를 검색하시겠습니까?")
				searchName = input()

				for item in self.itemList:
					if item.name == searchName:
						hasFound = True
						item.printDetail()

				if not hasFound:
					print("해당 이름으로 등록된 번호가 없습니다.")

			elif searchType == "2":
				print("어떤 번호를 검색하시겠습니까?")
				searchNum = input()

				targetIdx = findIdx(searchNum)

				if targetIdx is None:
					print("해당 전화번호는 등록되어 있지 않습니다.")
				else:
					self.itemList[targetIdx].printDetail()
			else:
				print("1~2의 값을 입력해주세요.")
				continue
			break

	def showList(self):
		if len(self.itemList) == 0:
			print("저장된 전화번호가 없습니다.")
			return

		while True:
			print("전체보기 그룹보기 중 선택하세요.")
			print("1. 전체보기")
			print("2. 그룹보기")
			print("보기 방식 선택 : ")
			searchType = input()

			if searchType == "1":
				for item in self.itemList:
					item.printDetail()
					print("\n")
			elif searchType == "2":
				print("어떤 그룹을 검색하시겠습니까?")
				searchGroup = input()
				hasFound = False

				for item in self.itemList:
					if item.group == searchGroup:
						item.printDetail()
						print("\n")
						hasFound = True

				if not hasFound:
					print("입력하신 그룹에 속한 전화번호가 없습니다.")
			else:
				print("1~2의 값을 입력해주세요.")
				continue
			break


























