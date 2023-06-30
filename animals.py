import animals.ferma_class as frm
from animals.dog_class import Dog
import user_ex.user_except as uex

if __name__ == '__main__':
    farm = frm.Farm()

    # Проверка исключений для животных
    try:
        dog = farm.generate("Dog")
        fish = farm.generate("fish")
        print("Собака говорит: ", end="")
        print(dog.say())

        print("Рыба говорит: ", end="")
        print(fish.say())
    except uex.UserMainException as e:
        print(e)



