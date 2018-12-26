class zapis:
    def __init__(self, author, comment):
        self.author = author
        self._comment = comment
        self.comments = list()

    def stroka (self):
        return ("Автор: " + str(self.author) + "\n" + "Комментарий: " + str(self._comment) + "\n")

    def show_comments(self):
        comments_string = ""
        for comment in self.comments:
            comments_string = comment.stroka() + comments_string
        return comments_string

    @property
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
        f.write("\nЗапись\n")
        f.write(str(post.stroka()))
        f.write("\nКомментарии\n")
        f.write(str(post.show_comments()))

