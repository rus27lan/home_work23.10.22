# 1) Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = "абв1 2абв 3а2б1в "
# print(f'Исходный текст: {text}')
# text2 = text.replace('абв', '')
# print(f'Удалили слова абв: {text2}')
# text3 = text.replace('а', "").replace("б", "").replace("в", "")
# print(f'Удалили все буквы "абв": {text3}')





# 2) Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import randint

# candy = 50
# name_one = input("Введите имя первого игрока: ")
# name_two = input("Введите имя второго игрока: ")
# lst_name = []
# if randint(0,1) == 0: lst_name.append(name_one), lst_name.append(name_two)
# else: lst_name.append(name_two), lst_name.append(name_one)
# print(f'\nПервый ход делает игрок : {lst_name[0]}')
# print(f'Далее ход переходит игроку : {lst_name[1]} \n')
# point_first = 0
# point_second = 0
# if candy >= 0:
#     while candy >= 0:
#         print(f'{lst_name[0]} ваш ход')
#         select_point = int(input())
#         if select_point <= 28 and select_point <= candy: 
#             point_first += select_point
#         elif select_point > candy: print('На столе конфет меньше , чем вы хотите взять! \nВы пропускаете ход!\n');select_point = 0
#         elif select_point > 28: print("За 1 ход , можно взять не более 28 конфет.\nВы пропускаете ход! \n");select_point = 0
#         candy -= select_point
#         if candy == 0: break
#         print(f'На столе осталось: {candy} конфет\n{lst_name[0]} у вас {point_first} очков \n{lst_name[1]} у вас {point_second} очков\n')
#         if candy >=0:
#             print(f'{lst_name[1]} ваш ход')
#             select_point = int(input())
#             if select_point <= 28 and select_point <= candy:
#                 point_second += select_point
#             elif select_point > candy: print('На столе конфет меньше , чем вы хотите взять! \nВы пропускаете ход!\n'); select_point = 0
#             elif select_point > 28: print("За 1 ход , можно взять не более 28 конфет.\nВы пропускаете ход! \n");select_point = 0
#             candy -= select_point
#             print(f'На столе осталось: {candy} конфет\n{lst_name[0]} у вас {point_first} очков \n{lst_name[1]} у вас {point_second} очков\n')
#         if candy == 0: break
# print(f'На столе осталось: {candy} конфет\n{lst_name[0]} у вас {point_first} очков \n{lst_name[1]} у вас {point_second} очков\n')
# if point_first > point_second: print(f'Выйграл игрок {lst_name[0]}')
# elif point_first == point_second: print("Ничья!")
# else: print(f'Выйграл игрок {lst_name[1]}')

# а) Игра против бота

# from random import randint

# candy = 50
# name_one = input("Введите имя игрока: ")
# name_two = 'Компьютер'
# lst_name = []
# if randint(0,1) == 0: lst_name.append(name_one), lst_name.append(name_two)
# else: lst_name.append(name_two), lst_name.append(name_one)
# print(f'\nПервый ход делает игрок : {lst_name[0]}')
# print(f'Далее ход переходит игроку : {lst_name[1]} \n')
# point_first = 0
# point_second = 0
# select_point = 0
# if candy >= 0:
#     while candy >= 0:
#         if lst_name[0] == 'Компьютер':
#             select_point = randint(1,28)
#             if select_point <= 28 and select_point <= candy: 
#                 point_first += select_point
#             elif select_point > candy: print('На столе конфет меньше , чем вы хотите взять! \nВы пропускаете ход!\n');select_point = 0
#             elif select_point > 28: print("За 1 ход , можно взять не более 28 конфет.\nВы пропускаете ход! \n");select_point = 0
#             candy -= select_point
#             if candy == 0: break
#             print(f'На столе осталось: {candy} конфет\n{lst_name[0]} у вас {point_first} очков \n{lst_name[1]} у вас {point_second} очков\n')
#             if candy >=0:
#                 print(f'{lst_name[1]} ваш ход')
#                 select_point = int(input())
#                 if select_point <= 28 and select_point <= candy:
#                     point_second += select_point
#                 elif select_point > candy: print('На столе конфет меньше , чем вы хотите взять! \nВы пропускаете ход!\n'); select_point = 0
#                 elif select_point > 28: print("За 1 ход , можно взять не более 28 конфет.\nВы пропускаете ход! \n");select_point = 0
#                 candy -= select_point
#                 print(f'На столе осталось: {candy} конфет\n{lst_name[0]} у вас {point_first} очков \n{lst_name[1]} у вас {point_second} очков\n')
#             if candy == 0: break
#         else:
#             if lst_name[0] == name_one:
#                 print(f'{lst_name[0]} ваш ход')
#                 select_point = int(input())
#             if select_point <= 28 and select_point <= candy: 
#                 point_first += select_point
#             elif select_point > candy: print('На столе конфет меньше , чем вы хотите взять! \nВы пропускаете ход!\n');select_point = 0
#             elif select_point > 28: print("За 1 ход , можно взять не более 28 конфет.\nВы пропускаете ход! \n");select_point = 0
#             candy -= select_point
#             if candy == 0: break
#             print(f'На столе осталось: {candy} конфет\n{lst_name[0]} у вас {point_first} очков \n{lst_name[1]} у вас {point_second} очков\n')
#             if candy >=0:
#                 print(f'{lst_name[1]} ваш ход')
#                 select_point = randint(1,28)
#                 if select_point <= 28 and select_point <= candy:
#                     point_second += select_point
#                 elif select_point > candy: print('На столе конфет меньше , чем вы хотите взять! \nВы пропускаете ход!\n'); select_point = 0
#                 elif select_point > 28: print("За 1 ход , можно взять не более 28 конфет.\nВы пропускаете ход! \n");select_point = 0
#                 candy -= select_point
#                 print(f'На столе осталось: {candy} конфет\n{lst_name[0]} у вас {point_first} очков \n{lst_name[1]} у вас {point_second} очков\n')
#             if candy == 0: break
# print(f'На столе осталось: {candy} конфет\n{lst_name[0]} у вас {point_first} очков \n{lst_name[1]} у вас {point_second} очков\n')
# if point_first > point_second: print(f'Выйграл игрок {lst_name[0]}')
# elif point_first == point_second: print("Ничья!")
# else: print(f'Выйграл игрок {lst_name[1]}')



# 3) Создайте программу для игры в ""Крестики-нолики"".

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")


# 4) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# ABCABCABCDDDFFFFFF

# from curses.ascii import isdigit
# from unicodedata import digit

# RLE = "ABCABCABCDDDFFFFFF"
# with open("RLE.txt", "w") as file:
#     file.write(RLE)
#     file.close()

# def RLE_encode(RLE):
#     encode = ''
#     count = 0
#     while count < len(RLE):
#         i = 1
#         while RLE[count] == RLE[count+1]:
#             i += 1
#             count += 1
#             if count + 1 >= len(RLE): break
#         encode += f'{i}{RLE[count]}'
#         count += 1
#         if count + 1 >= len(RLE): break
#     return encode
# print(f'Исходный: {RLE} \nВ сжатом виде: {RLE_encode(RLE)}')
# with open("RLE_encode.txt", "w") as file:
#     file.write(RLE_encode(RLE))
#     file.close()

# def RLE_decode(encode):
#     decode = ''
#     count = ''
#     for char in encode:
#         if char.isdigit(): count += char
#         else: 
#             decode += char * int(count)
#             count = ''
#     return decode
# print(f'Востановленный: {RLE_decode(RLE_encode(RLE))}')
# with open("RLE_decode.txt", "w") as file:
#     file.write(RLE_decode(RLE_encode(RLE)))
#     file.close()












# код из лекции

# # list = [(i, i**3) for i in range(1, 21) if i%2 ==0]
# # print (list)

# numbers = '1 2 3 5 8 15 23 38'.split()
# numbers_list = []
# # for i in numbers:
# #     numbers_list.append(int(i))
# # print(numbers_list)                <-- тоже саоме что numbers_list = select(int, numbers)
# #                                        функция select преобразует список(str) в (int)

# list = [(i, i**3) for i in numbers_list if i%2 ==0]
# print (list)