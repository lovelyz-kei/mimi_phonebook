import phone_book as pb
import pickle

if __name__ == "__main__":
	phoneBookInstance = pb.phoneBook([])
	try:
		fileLoad = open("phone_book.txt", "rb")
		phoneBookInstance.itemList = pickle.load(fileLoad)
		fileLoad.close()

	except FileNotFoundError:
		fileInit = open("phone_book.txt", "wb")
		initItemList = []
		pickle.dump(initItemList, fileInit)
		fileInit.close()

	while True:
		menuNum = phoneBookInstance.selectMenu()

		if menuNum == "1":
			phoneBookInstance.addItem()
		elif menuNum == "2":
			phoneBookInstance.modifyItem()
		elif menuNum == "3":
			phoneBookInstance.deleteItem()
		elif menuNum == "4":
			phoneBookInstance.searchItem()
		elif menuNum == "5":
			phoneBookInstance.showList()
		elif menuNum == "0":
			fileSave = open("phone_book.txt", "wb")
			pickle.dump(phoneBookInstance.itemList, fileSave)
			fileSave.close()
			print("프로그램을 종료합니다.")
			break
		else:
			print("메뉴에 제시된 번호만을 입력해주세요.")




