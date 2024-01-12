# Frontend -> usuário vê/interage
# Backend -> lógica por trás do site

# Frameworks
    # Django
    # Flask
    # Flet
        # Sites
        # programas de computador
        # aplicativos de celular
        
# Título hashzap
# Botão de Iniciar o chat
    # Popup
        # Bem vindo ao Hashzap
        # Escreva seu nome
        # Entrar no chat
# Chat
    # Usuário entrou no chat
    # Mensagems do usuário
#  Campo para enviar mensagem
# Botão de enviar

import flet as ft

def main(pagina):
    titulo = ft.Text("Hashzap")
    
    nome_usuario = ft.TextField(label="Escreva seu nome")   
    
    chat = ft.Column() 
    
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    # Evento de clique Botão enviar
    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        
        pagina.pubsub.send_all(texto_campo_mensagem)
        
        campo_mensagem.value = ""
        
        pagina.update()
        
    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    # Evento de clique Botão entrar chat
    def entrar_chat(evento):
        # Feche o popup
        popup.open = False
        
        # Tirei o botão "iniciar chat" da tela
        pagina.remove(botao_iniciar)
        
        # adicionar o nosso chat
        pagina.add(chat)
        
        # criar o Campo de enviar mensagem
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)
        
        # Usuário entrou no chat
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        
        pagina.update()
    
    # popup
    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )
    
    # Evento de clique Botão iniciar chat
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
    
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    
    
# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)