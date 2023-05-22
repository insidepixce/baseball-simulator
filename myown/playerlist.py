class Playerlist:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number
    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Number: {self.number}"
        

player_dict =[
    Playerlist("허경민", "내야수", 13),
    Playerlist("안승한", "포수", 20,),
    Playerlist("장승현", "포수", 22,),
    Playerlist("양의지", "포수", 25,),
    Playerlist("박유연", "포수", 26,),
    Playerlist("윤준호", "포수", 96,),
    Playerlist("안갈비", "내야수", 3,),
    Playerlist("신성현", "내야수", 5,),
    Playerlist("이유찬", "내야수", 7,),
    Playerlist("박계범", "내야수", 14,),
    Playerlist("서예일", "내야수", 16,),
    Playerlist("김민혁", "내야수", 18,),
    Playerlist("강승호", "내야수", 23,),
    Playerlist("권민석", "내야수", 34,),
    Playerlist("전민재", "내야수", 35,),
    Playerlist("김재호", "내야수", 52,),
    Playerlist("양석환", "내야수", 53,),
    Playerlist("임서준", "내야수", 93,),
    Playerlist("송승환", "외야수", 8,),
    Playerlist("로하스", "외야수", 11,),
    Playerlist("정수빈", "외야수", 31,),
    Playerlist("김재환", "외야수", 32,),
    Playerlist("김대한", "외야수", 37,),
    Playerlist("김인태", "외야수", 39,),
    Playerlist("홍성호", "외야수", 44,),
    Playerlist("강진성", "외야수", 49,),
    Playerlist("조수행", "외야수", 51,),
    Playerlist("양찬열", "외야수", 57,)
]

