import streamlit as st
import string
from random import choice, randint

def gerador(size, num_special_chars):
    lower  = list(string.ascii_lowercase)
    upper  = list(string.ascii_uppercase)
    charac = list('#$%&\'()*+,-./:;<=>?@')
    number = [i for i in range(10)]
    
    # verifica se há caracteres especiais suficientes
    if num_special_chars > size - 4:
        raise ValueError('Não é possível gerar uma senha com esses requisitos.')
    
    # inicializa a senha com um caractere de cada tipo
    senha = [choice(lower), choice(upper), choice(charac), choice(number)]
    
    # adiciona um caractere especial extra para garantir que haja pelo menos um
    if num_special_chars > 0:
        pos = randint(0, len(senha))
        senha.insert(pos, choice(charac))
        num_special_chars -= 1
    
    # adiciona caracteres aleatórios até que a senha tenha o tamanho desejado
    while len(senha) < size:
        turn = choice(['low','upper','number','charac'])
        if turn == 'low':
            senha.append(choice(lower))
        elif turn == 'upper':
            senha.append(choice(upper))
        elif turn == 'number':
            senha.append(choice(number))
        else:
            pos = randint(0, len(senha))
            senha.insert(pos, choice(charac))
            num_special_chars -= 1
    
    # adiciona caracteres especiais aleatoriamente
    for i in range(num_special_chars):
        pos = randint(0, len(senha))
        senha.insert(pos, choice(charac))
    
    # verifica se a senha tem pelo menos um caractere de cada tipo
    types = {'lower': False, 'upper': False, 'charac': False, 'number': False}
    for c in senha:
        if c in lower:
            types['lower'] = True
        elif c in upper:
            types['upper'] = True
        elif c in charac:
            types['charac'] = True
        elif c in number:
            types['number'] = True
    
    senha_str = "".join([str(c) for c in senha])
    return senha_str

# Cria o aplicativo usando o Streamlit
def app():
    st.title("Gerador de senhas")
    
    # Obtém o tamanho e a quantidade de caracteres especiais do usuário
    size = st.sidebar.slider("Tamanho da senha", min_value=8, max_value=30, step=1)
    num_special_chars = st.sidebar.slider("Quantidade de caracteres especiais", min_value=0, max_value=5, step=1)
    
    # Gera a senha com base nas informações fornecidas
    if st.sidebar.button("Gerar senha"):
        senha = gerador(size, num_special_chars)
        st.success(f"Sua senha é: {senha}")

if __name__ == "__main__":
    app()