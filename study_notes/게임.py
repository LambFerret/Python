class GameCharacter:
    # 게임 캐릭터 클래스
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
        # 게임 캐릭터는 속성으로 이름, hp, 공격력을 갖는다

    def is_alive(self):
        return self.hp > 0
        # 게임 캐릭터가 살아있는지(체력이 0이 넘는지) 확인하는 메소드

    def get_attacked(self, damage):
        if self.is_alive():
            self.hp = self.hp - damage if self.hp >= damage else 0
        else:
            print(f'{self.name} 싸늘한 온기만 남았습니다..')


    def attack(self, other_character):
        if self.is_alive():
            other_character.get_attacked(self.power)
        # 게임 캐릭터가 살아있으면 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다.

    def __str__(self):
        return self.name +"  " + str(self.hp)
        # 게임 캐릭터의 의미있는 정보를 포함한 문자열을 리턴한다.

# 게임 캐릭터 인스턴스 생성                        
character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

# 게임 캐릭터 인스턴스들 서로 공격
character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

# 게임 캐릭터 인스턴스 출력
print(character_1)
print(character_2)