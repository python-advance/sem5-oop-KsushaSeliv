# 3.1 Разработка прототипа приложения “Регистрация на конференцию” на основе фрагмента технического задания с использованием ООП.
import re 

class Conf():
  log = []
  def __init__(self, dicts):
    self.name = dicts["name"] 
    self.sname = dicts["sname"]
    self.email = dicts["email"]
    self.city = dicts["city"]

  @property
  def email(self):
      return self._email
    
  @email.setter
  def email(self, value):
    pattern = r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}"
    number_re = re.compile(pattern)    

    if (not (number_re.findall(str(value)))):
      raise ValueError('Ошибка')
    else:
      self.log.append ("Успешно создан!")
      self._email = value

  def otvetinfo(self):
     self.participant_info = {
      "name": self.name,
      "sname": self.sname,
      "email": self.email,
      "city": self.city,
    }

     return self.participant_info


  def __str__(self):
     return (self.name + " " + self.sname)

name = input("Введите имя:")
sname = input("Введите фамилию:")
email = input("Введите почту:")
city = input("Введите город:")

info={"name":name,"sname":sname,"email":email, "city":city}

stringinfo=Conf(info)
print(stringinfo.otvetinfo())

with open('otvet.txt', 'a') as f:
  f.write(str(stringinfo.log))
