print('Это викторина на знание географии России. Ответь на вопросы и узнай, насколько хорошо ты знаешь Россию!')

question1 = 'Какая гора является наивысшей точкой Кавказких гор? '
question2 = 'Какая область является эксклавом для России? '
question3 = 'Самое глубокое озеро на планете? '
question4 = 'Столица Республики Бурятия? '
question5 = 'Самый крупная по площади республика России из четырёх букв? '
question6 = 'Город, в котором находится один из крупнейших незамерзающих арктических портов? '
question7 = 'Единственная река, вытекающая из озера Байкал? '
question8 = 'В каком городе проводились Зимние Олимпийские игры 2014? '
question9 = 'Название края, в котором находится Ключевская сопка – самый высокий активный стратовулкан на территории Евразии? '
question10 = 'Название самой длинной в России и в мире магистрали? '

true_answer1 = 'эльбрус'
true_answer2 = 'калининградская'
true_answer3 = 'байкал'
true_answer4 = 'улан-удэ'
true_answer5 = 'саха'
true_answer6 = 'мурманск'
true_answer7 = 'ангара'
true_answer8 = 'сочи'
true_answer9 = 'камчатский'
true_answer10 = 'транссибирская'

score = 0

answer1 = input(question1).lower()
if answer1 == true_answer1:
  score+=1
answer2 = input(question2).lower()
if answer2 == true_answer2:
  score+=1
answer3 = input(question3).lower()
if answer3 == true_answer3:
  score+=1
answer4 = input(question4).lower()
if answer4 == true_answer4:
  score+=1
answer5 = input(question5).lower()
if answer5 == true_answer5:
  score+=1
answer6 = input(question6).lower()
if answer6 == true_answer6:
  score+=1
answer7 = input(question7).lower()
if answer7 == true_answer7:
  score+=1
answer8 = input(question8).lower()
if answer8 == true_answer8:
  score+=1
answer9 = input(question9).lower()
if true_answer9 == true_answer9:
  score+=1
answer10 = input(question10).lower()
if answer10 == true_answer10:
  score+=1
  
if score >= 7:
  print(f'Вы набрали {score} баллов! Вас можно считать экспертом')
else:
  print(f'Вы набрали {score} баллов. Расширяйте свой кругозор, вам есть, куда стремиться')