from array import array
import sys

i: int = 0
c: int = 0
memory: array = array('i', [0 for j in range(0, 30001)])
code_text = None
bracket_map = {}
stack = []


def main():
    global i, c
    global code_text
    global memory

    code_text = ''

    if len(sys.argv) > 1:  # yes, arg here
        code_file = open(sys.argv[1])
        for line in code_file.readlines():
            code_text += line
        pass
        code_text = list(code_text)
    else:
        quit(0)

    #  пробегаемся по коду и ищем пары скобок циклов
    for pos, symbol in enumerate(code_text):
        # открыли скобку - положим в вершину стека её позицию
        if symbol == '[':
            stack.append(pos)
        elif symbol == ']':
            last_open_pos = stack.pop()  # позиция последней открывающей скобки
            # создадим парные записи
            bracket_map[pos] = last_open_pos
            bracket_map[last_open_pos] = pos  # bracket_map хранит значения вида {индекс_n[:индекс_n]}, n - [1, n]
        pass

    while c < len(code_text):
        if code_text[c] == '>':
            i += 1
        if code_text[c] == '<':
            i -= 1
        if code_text[c] == '+':
            memory[i] += 1
        if code_text[c] == '-':
            memory[i] -= 1
        if code_text[c] == '.':
            print(chr(memory[i]))
        if code_text[c] == ',':
            input_text = input('>>').split(" ")[0]
            memory[i] = ord(input_text)
        if code_text[c] == '[':
            if memory[i] == 0:
                c = bracket_map[c]  # перескакиваем на соответствующую ']'
        if code_text[c] == ']':
            if memory[i] != 0:
                c = bracket_map[c]  # перескакиваем на соответствующую ']'
        c += 1
        pass
    pass  # end main


if __name__ == "__main__":
    main()
