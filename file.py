comandos = {
    'git init': 'Inicia um repositório Git local.',
    'git clone <url>': 'Clona um repositório remoto para o local.',
    'git add <arquivo>': 'Adiciona um arquivo específico para o próximo commit.',
    'git commit -m "<mensagem>"': 'Cria um commit com uma mensagem descritiva.',
    'git push': 'Envia os commits locais para o repositório remoto.',
    'git pull': 'Atualiza o repositório local com as mudanças do repositório remoto.',
    'git status': 'Exibe o estado atual do repositório, mostrando arquivos modificados, adicionados e não rastreados.',
    'git branch': 'Lista, cria ou exclui branches.',
    'git checkout <branch>': 'Muda para a branch especificada.',
}
print('========COMANDOS GITHUB========')
for comando, descricao in comandos.items():
    print(comando, '-', descricao)
print('===============================')