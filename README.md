<h1>Инвариантное задание</h1>
2.1 Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).

2.2. Создание геттеров и сеттеров для классов «запись», «комментарий» приложения «Гостевая книга». Создание функций для вывода на печать информации, хранящийся в объектах.

```python
class zapis:
    def __init__(self, author, comment):
        self.author = author
        self._comment = comment #позволяет сделать их полускрытыми(если одно подчёркивание, если два,то полностью скрытыми)Так как они скрытые, мы создаём геттеры, чтобы мы могли к ним обратиться. Сеттеры позволяют изменить то, что написано в переменной.
        self.comments = list()

    def stroka (self): #возвращаем автора и его комментарий
        return ("Автор: " + str(self.author) + "\n" + "Комментарий: " + str(self._comment) + "\n")

    def show_comments(self):
        comments_string = ""
        for comment in self.comments:
            comments_string = comment.stroka() + comments_string
        return comments_string

    @property #специальное свойство, которое позволяет как раз таки создать эти геттеры, сеттеры
    def comment(self):
        return self._comment

    def add_comment(self, comment):
        self.comments.append(comment)

    @comment.setter
    def comment(self, comment):
        self._comment = comment

    @comment.getter
    def comment(self):
        return self._comment

      
class Comments(zapis):
    def __init__(self, author, comment):
        super(Comments, self).__init__(author=author, comment=comment)


if __name__ == "__main__":
    post = zapis("IVT", "Завтра пары отменяются")

    post.add_comment(Comments("Ксения", "Всё понятно"))
    post.add_comment(Comments("Антон", "Так точно:)"))

    with open('Record.txt', 'a') as f:
        f.write("Запись")
        f.write(str(post.stroka()))
        f.write("Комментарии")
        f.write(str(post.show_comments()))
```
![alt](https://github.com/python-advance/sem5-oop-KsushaSeliv/blob/master/invar/15.JPG)

<h1>Вариативное задание</h1>
3.1 Разработка прототипа приложения “Регистрация на конференцию” на основе фрагмента технического задания с использованием ООП.

```python
import re 

class guest():

  log = []

  def __init__(self, dictsinfo): #здесь у нас будет словарик, в который будут входить name,sname,email,age
    self.name = dictsinfo["name"] 
    self.sname = dictsinfo["sname"]
    self.email = dictsinfo["email"]
    self.age = dictsinfo["age"]

  @property
  def email(self):
      return self._email
    
  @email.setter #создаём сеттер для email
  def email(self, value):
    pattern = r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}"
    reobj = re.compile(pattern)    

    if (not (reobj.findall(str(value)))): #если не нашлось никаких сопадений с заданным паттерном, поднимаем ошибочку
      raise ValueError('Ошибка')
    else: #иначе записываем, что email был создан
      self.log.append ("Всё хорошо")
      self._email = value

  def otvetinfo(self): #записываем все наши данные
     self.information = {"name": self.name,"sname": self.sname,"email": self.email,"age": self.age,}
     return self.information

  def __str__(self):
    return (self.f_name + " " + self.s_name)   

name = input("Имя:")
sname = input("Фамилия:")
email = input("Почта:")
age = input("Возраст:")

info={"name":name,"sname":sname,"email":email, "age":age}

stringinfo=guest(info)
print(stringinfo.otvetinfo())

with open('otvet.txt', 'a') as f:
  f.write(str(stringinfo.log))
```
![alt](https://github.com/python-advance/sem5-oop-KsushaSeliv/blob/master/var/16.JPG)
