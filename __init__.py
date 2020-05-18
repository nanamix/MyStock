from kiwoom.kiwoom import *
import sys
from PyQt5.QtWidgets import *

class Main():
    def __init__(self):
        print("Main() Start")
        self.app = QApplication(sys.argv) # PyQt5로 실행할 파일 명을 자동 설정
        ##Kiwoom()
        self.kiwoom = Kiwoom() # 키움 클래스 객체화
        self.app.exec_() # 이벤트 루프 실행

if __name__ == "__main__":
    Main()