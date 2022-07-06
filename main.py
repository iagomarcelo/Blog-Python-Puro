from classes import User, Post, Ads
from collections import Counter
from datetime import datetime, timezone, timedelta
import time

timezone_offset = -3.0
tzinfo = timezone(timedelta(hours=timezone_offset))
data = datetime.now(tzinfo)
#define data

arrayPosts = []
usuario = []
action = 99991
options = 99991
#cria listas e define variáveis a serem usadas nos while's

#Opções iniciais
while options != '0':
  print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99                 0 - Encerrar sistema\n\n                      HOME')
  print('____________________________________________________\n')
  options = (input('1 - Fazer Login\n2 - Fazer Cadastro\n'))
  
  if options == '0':
    print('Até a próxima!\nEncerrando...')
    action = '0'
    time.sleep(3)
    break
    
  if options == '1':
    print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99\n\n                      LOGIN')
    print('____________________________________________________\n')
    fakeTestLogin = input('Login: ')
    fakeTestPassword = input('Senha: ')
    print('\nERROR 404: VOCÊ AINDA NÃO POSSUI DADOS NO NOSSO SISTEMA, CADASTRE-SE!')
    options = input('\nPara retornar à página inicial, pressione ENTER\n')

  elif options == '2':
    print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99\n\n                      CADASTRE-SE')
    print('____________________________________________________\n')
    userId = 1
    userName = input('Nome de Usuário: ')
    userLogin = input('Login: ')
    userPassword = input('Senha: ')
    usuario.append(User(userId, userName, userLogin, userPassword))
    usuario1 = (vars(usuario[0]))
    print('\nSeu Nome de usuário foi salvo como: ' + usuario1['nome'])
    print('Seu Login foi salvo como: ' + usuario1['login'])
    print('Sua senha foi salva como: ' + usuario1['senha'])
    print('\nCADASTRO EFETUADO COM SUCESSO!')

    options = input('\nPara realizar login, pressione ENTER\n')
    break
  else:
    print('Insira um número válido!')
    options = input('\nPara retornar à página inicial, pressione ENTER\n')

#Menu
while action != '0':
  loading = [0]
  for element in loading:
    print('Carregando.')
    time.sleep(0.5)
    print('Carregando..')
    time.sleep(0.5)
    print('Carregando...')
    time.sleep(0.5)

  print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99                     0 - Fazer Logout\n\n                      MENU')
  print('____________________________________________________\n')
  action = input('1 - Fazer postagem\n2 - Mostrar postagens\n3 - Alterar Publicação\n4 - Ver data e título das publicações já postadas\n5 - Excluir publicação\n6 - Pesquisar por tema\n')

  #logout
  if action == '0':
    print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99\n\n                      LOGOUT')
    print('____________________________________________________\n')
    print('Até a próxima!\nEncerrando...')
    time.sleep(3)
    break
  
  #menu de nova postagem
  elif action == '1':
    print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99\n\n                    NOVA POSTAGEM')
    print('____________________________________________________\n')
    tipoPost = input('Tipo de postagem:\n1 - Postagem pessoal\n2 - Publicar anúncio\nENTER - Nenhuma das opções\n')
    postId = 0
    if tipoPost == '1':
      print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99\n\n                      NOVO POST')
      print('____________________________________________________\n')
      postType = tipoPost
      for p in arrayPosts:
        postId = postId + 1
      postTitle = input('digite o título: ')
      postContent = input('digite o conteúdo: ')
      postTheme = input('digite o tema: ')
      arrayPosts.append(Post(postType, postId, postTitle, postContent, postTheme, data))
    adsId = postId
    if tipoPost == '2':
      print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99\n\n                    NOVO ANÚNCIO')
      print('____________________________________________________\n')
      postType = tipoPost
      for ads in arrayPosts:
        adsId = adsId + 1
      adsUrl = input('digite a url do anúncio: ')
      adsTitle = input('digite o título do anúncio: ')
      adsContent = input('digite o conteúdo do anúncio: ')
      adsTheme = input('digite o tema do anúncio: ')
      arrayPosts.append(Ads(postType, adsId, adsUrl, adsTitle, adsContent, adsTheme, data))
    action = input('\nCaso deseje retornar para o menu, pressione ENTER\n')  
  
  #feed listando tema, título e conteúdo para publicações pessoais ou url, tema, título e conteúdo para anúncio
  elif action == '2':
    print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99\n\n                        FEED')
    print('____________________________________________________')
    i = 0
    for post in arrayPosts:
      arrayPosts1 = (vars(arrayPosts[i]))
      if arrayPosts1['postType'] == '1':
        print('\n\n' + arrayPosts1['tema'] + '\n\n' + arrayPosts1['titulo'] + '\n\n' + arrayPosts1['texto'])
        print('\nData da publicação: ' + str(arrayPosts1['data']))
        print('____________________________________________________')
      elif arrayPosts1['postType'] == '2':
        print('\n\n' + 'ANÚNCIO' + '\n\n' + 'Acesse nosso site!\n' + arrayPosts1['url'] + '\n\n' + arrayPosts1['tema'] + '\n\n' + arrayPosts1['titulo'] + '\n\n' + arrayPosts1['texto'])
        print('\nData da publicação: ' + str(arrayPosts1['data']))
        print('____________________________________________________')
      i = i+1
    action = input('\nCaso deseje retornar para o menu, pressione ENTER\n')

  #lista publicações e possibilita alterações
  elif action == '3':
    jobson = 0
    print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99\n\n')
    print('                        POSTS')
    print('____________________________________________________\n')
    for post in arrayPosts:
      arrayPosts1 = (vars(arrayPosts[jobson]))
      print(str(jobson + 1) + ' - ' + arrayPosts1['titulo'])
      jobson = jobson + 1
    jobson = 0
    
    jobson = str(input('Digite o número da postagem que você deseja alterar: \n'))
    if jobson.isnumeric() == True:
      jobson = int(jobson) - 1
      if (jobson + 1) <= len(arrayPosts) and (jobson + 1) > 0:
        arrayPosts1 = (vars(arrayPosts[jobson]))
        if arrayPosts1['postType'] == '1':
          arrayPosts1['titulo'] = input('Novo título: ')
          arrayPosts1['texto'] = input('Novo conteúdo: ')
          arrayPosts1['tema'] = input('Novo tema: ')
          arrayPosts1['data'] = data
          print('____________________________________________________')
        if arrayPosts1['postType'] == '2':
          arrayPosts1['url'] = input('Nova url: ')
          arrayPosts1['titulo'] = input('Novo título: ')
          arrayPosts1['texto'] = input('Novo conteúdo: ')
          arrayPosts1['tema'] = input('Novo tema: ')
          #dataNãoAlterável :)
        jobson = jobson + 1
      else:
        print('Insira um número válido!')
    else:
      print('Insira um número válido!')
    action = input('\nCaso deseje retornar para o menu, pressione ENTER\n')
        
  #Mostra apenas data e título das publicações postadas
  elif action == '4':
    jobson = 0
    print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99\n\n')
    print('                   DATA E TÍTULO')
    print('____________________________________________________\n')
    for post in arrayPosts:
      arrayPosts1 = (vars(arrayPosts[jobson]))
      print('\n\nTítulo: ' + arrayPosts1['titulo'])
      print('\nData da publicação: ' + str(arrayPosts1['data']))
      print('____________________________________________________')
      jobson = jobson + 1
      #LEMBRANDO, JOBSON É NOSSO AMIGO ITERADOR :]
    action = input('\nCaso deseje retornar para o menu, pressione ENTER\n')
  
  #Lista publicações e possibilita exclusão delas
  elif action == '5':
    jobson = 0
    print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99\n\n')
    print('                        POSTS')
    print('____________________________________________________\n')
    for post in arrayPosts:
      arrayPosts1 = (vars(arrayPosts[jobson]))
      print(str(jobson + 1) + ' - ' + arrayPosts1['titulo'])
      jobson = jobson + 1
    jobson = 0

    jobson = str(input('Digite o número da postagem que você deseja remover:\n(Caso não haja publicação listada, pressione ENTER para seguir\n)'))
    if jobson.isnumeric() == True:
      jobson = int(jobson) - 1
      if (jobson + 1) <= len(arrayPosts) and (jobson + 1) > 0:
        arrayPosts.pop(jobson)
    else:
      print('Insira um número válido!')
    action = input('\nCaso deseje retornar para o menu, pressione ENTER\n')
  
  #search
  elif action == '6':
    i = 0
    print('\n\n\n\n\n\n\n\nFACEBROOKLYN 99\n')
    print('                      SEARCH')
    print('____________________________________________________\n')
    filtro = str(input('Pesquisar tema: '))
    a = 0
    for post in arrayPosts:
      arrayPosts1 = (vars(arrayPosts[i]))
      if arrayPosts1['tema'].lower() == filtro.lower():
        print('\n\n' + arrayPosts1['tema'] + '\n\n' + arrayPosts1['titulo'] + '\n\n' + arrayPosts1['texto'])
        a = a + 1
      i = i+1
    print('\nTotal de publicações encontradas com o tema '+filtro+': ' +str(a))
    action = input('\nCaso deseje retornar para o menu, pressione ENTER\n')

  else:
    print('Insira um número válido!\naguarde, reestabelecendo conexão...')
    time.sleep(1.5)