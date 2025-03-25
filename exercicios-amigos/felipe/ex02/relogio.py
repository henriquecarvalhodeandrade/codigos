import time

for i in range(15):

    for j in range(60):

        for k in range(60):

            print(f'{i} h: {j} min: {k} seg')

            if k == 59:
                print(f'passaram-se {i+1} horas')
            
            if j == 59:
                print(f'passaram-se {i+1} horas')

            time.sleep(1)
