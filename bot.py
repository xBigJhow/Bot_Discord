import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('TOKEN')
print("Token carregado:", TOKEN)  # Isso deve imprimir o valor do token, se estiver correto
if TOKEN is None:
    print("Erro: O token não foi carregado corretamente. Verifique o arquivo .env.")

# Cria a instância do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

# Evento que é chamado quando o bot está pronto
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# Comando 'rollover'
@bot.command()
async def rollover(ctx):
    mensagem = (
        "🎰 **Rollover** é um requisito comum em cassinos online relacionado a bônus.\n\n"
        "ℹ️ Ele determina quantas vezes o valor do bônus (ou bônus + depósito) precisa ser apostado.\n\n"
        "📌 **Dicas para rollover em casas comuns (não chinesas):**\n\n"
        "1️⃣ **Bac Bo (Cassino ao Vivo)**:\n"
        "   - Aposte metade do valor no 🔵 **azul** e a outra metade no 🔴 **vermelho**.\n"
        "   - 🔄 **Resultado:**\n"
        "     - Se não der TIE, você **não perde nada**. ✅\n"
        "     - Se der TIE, você perde **10%** do valor apostado. ❌\n\n"
        "2️⃣ **Baccarat 777 (Slot):**\n"
        "   - Aposte no **Player** e **Banker**.\n"
        "   - 🔄 **Resultado:**\n"
        "     - Se der Player, você **não perde nada**. ✅\n"
        "     - Se der Banker, você perde apenas **2.5%** do valor apostado. ❌\n\n"
        "3️⃣ **Mini Roulette (Spribe):**\n"
        "   - Aposte metade no ⚫ **preto** e metade no 🔴 **vermelho**.\n"
        "   - 🔄 **Resultado:**\n"
        "     - Perda garantida de **3%** do total da aposta. ❌\n\n"
        "🎲 Escolha a melhor estratégia e boa sorte! 🍀"
    )
    await ctx.send(mensagem)

# Comando 'tada'
@bot.command()
async def tada(ctx):
    mensagem = (
        "🎮 **Códigos TADA** são resgatados no jogo *Fortune Gems*, da provedora **Tada Gaming**.\n\n"
        "🔑 **Códigos de resgate disponíveis e suas plataformas:**\n\n"
        "• 🔹 **Código de resgate:** `9F` - Resgate em: [9F.com](https://9f.com)\n"
        "• 🔹 **Código de resgate:** `9D` - Resgate em: [9D.com](https://9d.com)\n"
        "• 🔹 **Código de resgate:** `claze` - Resgate em: [Claze.com](https://claze.com)\n"
        "• 🔹 **Código de resgate:** `ijogo` - Resgate em: [Ijogo.com](https://ijogo.com)\n\n"
        "🏷️ **Códigos relacionados ao BRABET:**\n"
        "Esses códigos podem ser usados em várias casas que estão fixadas no chat **#tada**, como:\n"
        "• ✨ **SEXWIN**\n"
        "• ✨ **ACCWIN**\n"
        "• ✨ **BRAQQQ**\n"
        "• ✨ **PLAYPP**\n"
        "• ✨ **PPYBET**\n"
        "• ✨ **IPIWIN**\n\n"
        "📌 Certifique-se de verificar as casas disponíveis antes de resgatar. Boa sorte! 🍀"
    )
    await ctx.send(mensagem)


# Comando 'surebet'
@bot.command()
async def surebet(ctx):
    mensagem = (
        "🎯 **Surebet (Aposta Certa)**\n"
        "É uma estratégia utilizada em apostas esportivas  para ter um **lucro garantido**, "
        "independentemente do resultado. Essa técnica aproveita as diferenças nas odds (cotações) "
        "oferecidas por diferentes casas de apostas para o mesmo evento.\n\n"
        
        "🛠️ **Como funciona?**\n"
        "A ideia é distribuir o dinheiro em apostas em todos os possíveis resultados de um evento "
        "(como vitória, empate ou derrota), de forma que o retorno total seja maior que o valor apostado, "
        "independentemente do desfecho.\n\n"

        "📊 **Exemplo Prático**\n"
        "Suponha que há um jogo de futebol entre **Time A** e **Time B**, com as seguintes odds:\n\n"
        "🏠 **Casa 1**: Vitória do Time A → **2.70**\n"
        "🏠 **Casa 2**: Vitória do Time B → **1.80**\n\n"

        "💡 **Apostas Estratégicas - Valor de R$100,00:**\n"
        "1️⃣ Aposte **R$40** na vitória do **Time A** (Casa 1).\n"
        "2️⃣ Aposte **R$60** na vitória do **Time B** (Casa 2).\n\n"

        "🔄 **Resultados Possíveis:**\n"
        "✔️ **Se o Time A vencer:**\n"
        "   - Você recebe **R$108,00** (R$40 × 2.70).\n"
        "   - **Lucro líquido:** **R$8,00** ✅\n\n"
        "✔️ **Se o Time B vencer:**\n"
        "   - Você recebe **R$108,00** (R$600 × 1,80).\n"
        "   - **Lucro líquido:** **R$8,00** ✅\n\n"

        "💰 **Vantagem:** Lucro garantido de 8% no valor apostado! 🍀\n\n"
        
        "🧮[Calculadora de Surebet](https://pt.surebet.com/calculator) ⚖"
    )
    await ctx.send(mensagem)

# Comando 'freebet'
@bot.command()
async def freebet(ctx):
    mensagem = (
        "🎁 **Freebet com Estratégia de Extração**\n"
        "Uma **Freebet** é uma aposta gratuita oferecida pelas casas de apostas. Com a estratégia de **extração**, podemos transformar essa aposta em **dinheiro garantido** ao usar uma *exchange* (plataforma de apostas de contra-apostas), como a **Bet-Bra** ou **Betfair**.\n\n"
        
        "Essa estratégia consiste em fazer uma aposta **\"a favor\"** com a Freebet e, ao mesmo tempo, uma aposta **\"contra\"** (lay) na exchange, garantindo lucro ou minimizando perdas.\n\n"
        
        "💡 **Aqui no Saruê's Group**, nossos Administradores estão ativos a todo momento procurando Freebets. Quando encontram casas com possibilidades de extração de Freebet, eles enviam todas as entradas necessárias para que você tenha lucro garantido, tanto diretamente quanto na hora da extração da Freebet.\n\n"

        "📋 **Instruções:**\n"
        "1️⃣ Faça a **cópia das entradas com exatidão** enviadas pelos administradores.\n"
        "2️⃣ Caso as **ODD's estejam diferentes**, solicite ajuda no chat **#duvidas**.\n"
        "3️⃣ Nossos administradores recalcularão para garantir o melhor aproveitamento da Freebet.\n\n"

        "💰 Transforme suas Freebets em lucro garantido de forma simples e segura! 🚀"
    )
    await ctx.send(mensagem)

# Comando 'multiconta'
@bot.command()
async def multiconta(ctx):
    mensagem = (
        "🔑 **Multigerenciador de Contas **\n"
        "O **Multigerenciador de Contas** é uma ferramenta essencial para gerenciar várias contas simultaneamente em plataformas de apostas ou jogos online. Com ele, você pode otimizar suas apostas, controlar múltiplas contas e maximizar seus lucros de forma mais eficiente.\n\n"
        
        "🐬 **Dolphin** é um dos mais populares multigerenciadores, permitindo que você **gerencie várias contas** em diferentes casas de apostas ao mesmo tempo, sem risco de ser banido por atividades suspeitas de múltiplas apostas. A ferramenta garante o **controle total** de suas contas e apostas, otimizando o desempenho no longo prazo.\n\n"

        "💡 **Vantagens de usar um Multigerenciador:**\n"
        "1️⃣ **Gerenciamento de múltiplas contas** em diversas plataformas de apostas. Você pode fazer apostas mais estratégicas, sem se preocupar com a limitação de uma única conta.\n"
        "2️⃣ **Automação** de processos, como entradas automáticas e cálculos de odds. Isso permite um controle mais preciso e sem erros.\n"
        "3️⃣ **Segurança** e anonimato ao utilizar o Dolphin, evitando bloqueios ou bans por atividades de múltiplas contas.\n"
        "4️⃣ **Maximize seus lucros** ao aproveitar bônus de diferentes contas e utilizar estratégias de apostas mais assertivas.\n\n"

        "🔒 **Atenção:** Para utilizar o **Dolphin** ou outro multigerenciador de contas, é importante seguir as regras das casas de apostas, já que algumas plataformas podem ter restrições sobre o uso de múltiplas contas. Certifique-se de usar o sistema de forma ética e dentro das diretrizes das casas de apostas para evitar problemas futuros.\n\n"

        "🚀 **Dica:** Utilizamos o Dolphin como exemplo pois ele libera 10 perfis gratuitos, segue o link para download:\n\n✨"
        "🔗 [LINK PARA DOWNLOAD](https://dolphin-anty.com)"
    )
    await ctx.send(mensagem)

# Comando 'proxy'
@bot.command()
async def proxy(ctx):
    mensagem = (
        "🌐 **Proxies no Uso de Multigerenciador de Contas em Casas de Apostas**\n"
        "Quando se utiliza **multigerenciadores de contas**, como o **Dolphin**, o uso de **proxies** se torna essencial para **evitar bloqueios** por parte das casas de apostas, que podem detectar múltiplos acessos vindos do mesmo IP.\n\n"
        
        "🔑 **Como os Proxies ajudam no Multigerenciamento?**\n"
        "As casas de apostas muitas vezes têm **restrições sobre múltiplas contas** em um único IP. Se você usar **várias contas** sem proxies, a plataforma pode perceber e **bloquear** suas contas por **fraude ou violação de regras**. O **proxy** resolve esse problema, pois cada conta passa a parecer estar acessando a plataforma de diferentes **endereços IP**, o que ajuda a **mascarar** a origem do tráfego e a **evitar detecção**.\n\n"

        "🔒 **Por que usar Proxies em Casas de Apostas?**\n"
        "1️⃣ **Evitar bloqueios de múltiplos acessos:** Casas de apostas frequentemente bloqueiam usuários que tentam acessar várias contas do mesmo IP. Os proxies permitem que cada conta tenha seu próprio IP, evitando esses bloqueios.\n"
        "2️⃣ **Gerenciar várias contas sem restrições:** Usar proxies ajuda a gerenciar **várias contas** simultaneamente sem que a plataforma perceba que todas estão conectadas ao mesmo usuário.\n"
        "3️⃣ **Evitar limitações de geolocalização:** Se você usar contas em plataformas que restringem o acesso com base na localização geográfica, proxies permitem que você **mascare sua localização** e acesse as plataformas de qualquer região.\n\n"

        "🚀 **Dica:** Ao usar **proxies rotativos**, você pode alterar os **endereços IP** frequentemente, garantindo que suas contas permaneçam **indetectáveis** e **seguras**, além de permitir **múltiplas entradas** em várias plataformas de apostas simultaneamente.\n\n"

        "🔗[COMPRAR PROXYS NA WEBSHARE](https://dashboard.webshare.io/subscription)"
    )
    await ctx.send(mensagem)


@bot.command()
async def info(ctx):
    mensagem = (
    "🤖 **Informações sobre o Bot Saruê's Group**\n\n"
    
    "🔍 **Como chamar o bot:**\n"
    "Basta digitar os comandos no chat para interagir com o bot! Use o **prefixo** definido para enviar os comandos.\n\n"
    
    "📜 **Comandos disponíveis:**\n"
    "1️⃣ **$rollover**: Instruções sobre a estratégia de rollover em cassinos e como maximizar o bônus.\n"
    "2️⃣ **$tada**: Códigos TADA para o jogo *Fortune Gems* e as plataformas onde podem ser resgatados.\n"
    "3️⃣ **$surebet**: Explicação sobre a estratégia de Surebet e como obter lucro garantido com apostas esportivas.\n"
    "4️⃣ **$freebet**: Estratégia de extração de Freebets e como transformar uma aposta gratuita em lucro garantido.\n"
    "5️⃣ **$multiconta**: Dicas sobre o uso de multigerenciador de contas, como o Dolphin, para otimizar suas apostas.\n"
    "6️⃣ **$proxy**: Como usar proxies para evitar bloqueios ao gerenciar várias contas em casas de apostas.\n\n"
    
    )
    await ctx.send(mensagem)

    # Evento para capturar comandos não encontrados
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("❌ **Função não disponível. Tente novamente com um comando válido.**")



# Comando 'contato'
@bot.command()
async def contato(ctx):
    mensagem = (
        "📞 **Entre em contato com os responsáveis abaixo**:\n\n"
        "👨‍💼 **JEAN** - Dúvida sobre códigos TADA\n"
        "👨‍💼 **UGA e NELSIN** - Dúvida sobre FREEBET\n"
        "👨‍💼 **PEDRO** - Dúvida sobre SUREBET\n"
        "👨‍💼 **SLEIVER** - TICKETS/TESTA CPA\n"
        "👨‍💼 **CORTES** - TICKETS/TESTA CPA\n"
        "👨‍💼 **S!X / 4THEUX / SAMPZ** - TESTE DE CALLS\n"
        "👨‍💼 **SANZZ** - ENCONTRA CALLS\n"
        "👨‍💼 **SANDER** - ATENDIMENTO DE TICKETS E ORGANIZAÇÃO DO SERVIDOR\n"
        "👨‍💼 **BRYAN** - ATENDIMENTO DE TICKETS E VALIDAÇÃO DE CALL\n\n"
        "💬 **Escolha o responsável adequado e entre em contato com eles!**"
    )
    await ctx.send(mensagem)


@bot.command()
async def ping(ctx):
    mensagem = (
        "pong"
    )
    await ctx.send(mensagem)



# Inicia o bot com o token
bot.run(TOKEN)