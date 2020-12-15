import re


def parser(text):
    # Padrão de range: AA000-AB000
    pattern = r'([a-zA-Z][a-zA-Z][0-9][0-9][0-9][\s]*[\-][\s]*[a-zA-Z][a-zA-Z][0-9][0-9][0-9])'
    # Padrão normal: AA000
    pattern2 = r'([a-zA-Z][a-zA-Z][0-9][0-9][0-9])'

    # Primeira leitura do texto
    lista = re.findall(pattern, text)
    # Segunda leitura do texto
    lista2 = re.findall(pattern2, text)
    
    flights = []

    for r in lista:
        i = 0
        number = 1
        trimmed = r.replace(' ', '')
        inicio = trimmed.split('-')[0].upper()
        fim = trimmed.split('-')[1].upper()
        range_inferior = int(re.search(r'\d+', inicio).group())
        range_superior = int(re.search(r'\d+', fim).group())

        if inicio[1] == fim[1]:
            while  range_inferior <= range_superior:
                serial = inicio[0]+inicio[1]+str(range_inferior).zfill(3)
                range_inferior += 1
                flights.append(serial)
        else:
            char = inicio[1]
            
            char_end = fim[1]
            
            while char <= char_end:            
                if i == 0:
                    while  range_inferior <= 999:
                        serial = inicio[0]+char+str(range_inferior).zfill(3)
                        flights.append(serial)
                        if range_inferior == 999:
                            char = chr(ord(char) + 1)
                        range_inferior += 1
                    i += 1                        
                if char == char_end:
                    while  number <= range_superior:
                        serial = inicio[0]+char+str(number).zfill(3)
                        flights.append(serial)
                        number += 1
                else:
                    while  number <= 999:
                        serial = inicio[0]+char+str(number).zfill(3)
                        flights.append(serial)
                        number += 1
                number = 1
                char = chr(ord(char) + 1)
    
    for r in lista2:
        flights.append(r.upper())
    final_list = list(dict.fromkeys(flights))
    return final_list

#print(flights)

if __name__ == "__main__":
    text = 'ya900 yb190-yb200 yc999 - yd020 Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.  yo875'
    lista = parser(text)
    print(lista)