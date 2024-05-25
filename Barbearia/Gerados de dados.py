import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Configuração inicial
faker = Faker('pt_BR')
atendentes = ['Rafael', 'João', 'Pedro', 'Gustavo']
servicos = ['Corte de cabelo', 'Corte de barba', 'Sobrancelhas', 'Coloração no cabelo']
observacao = [
    'Seu trabalho é incrível, meu cabelo nunca esteve tão bonito!',
    'Adorei o corte, ficou exatamente como eu queria.',
    'Obrigado(a) por sempre cuidar tão bem do meu cabelo.',
    'Você tem mãos de fada, o tratamento que fez no meu cabelo ficou perfeito.',
    'Sempre saio do seu salão me sentindo renovado(a) e confiante.',
    'Sua atenção aos detalhes faz toda a diferença no resultado final.',
    'Você é um(a) verdadeiro(a) artista, seu talento para cortes e colorações é impressionante.',
    'Nunca me senti tão bem com um novo visual, obrigado(a) por sua habilidade e dedicação.',
    'Seu profissionalismo e expertise são evidentes em cada serviço que você realiza.',
    'Recomendo você para todos os meus amigos, seu trabalho é impecável.',
    'Sempre uma experiência maravilhosa vir ao seu salão, obrigado(a) pela excelência do seu trabalho.',
    'Fiquei muito satisfeito(a) com o resultado, você superou minhas expectativas.',
    'Você realmente entende o que seus clientes querem e sabe como transformar isso em realidade.',
    'Admiro sua paixão pela profissão e seu comprometimento em sempre entregar um serviço de alta qualidade.',
    'Seu atendimento é excepcional, sempre me sinto bem-vindo(a) e confortável em seu salão.',
    'Obrigado(a) por cuidar tão bem do meu cabelo e sempre me deixar feliz com o resultado.',
    'Você é um(a) verdadeiro(a) mestre(a) em transformar cabelos, estou encantado(a) com o resultado.',
    'Seu talento e criatividade são admiráveis, obrigado(a) por sempre me surpreender com cortes e cores incríveis.',
    'Estou muito feliz com o serviço, você realmente sabe como valorizar a beleza natural de cada cliente.',
    'Seu trabalho é mais do que apenas cortar cabelos, é uma forma de arte que transforma vidas.',
    'Achei que o corte poderia ter sido mais preciso, algumas partes ficaram desiguais.',
    'Percebi que o tempo de espera foi um pouco longo, talvez seja interessante melhorar a gestão de horários.',
    'Notei que a limpeza do salão poderia ser melhor, especialmente na área de espera.',
    'A coloração não ficou exatamente como eu esperava, talvez fosse bom discutir mais detalhes antes de começar.',
    'Achei que o preço do serviço foi um pouco alto em comparação com outros salões na região.',
    'Tive a impressão de que você estava um pouco distraído(a) durante o serviço, isso pode afetar a qualidade do resultado.',
    'Fiquei um pouco desconfortável com a pressão para comprar produtos adicionais, talvez seja bom ser mais sutil nesse aspecto.',
    'Achei que a comunicação sobre as opções de tratamento poderia ter sido mais clara.',
    'Notei que algumas áreas do meu cabelo foram esquecidas durante o corte, talvez seja bom revisar o processo.',
    'A temperatura da água durante a lavagem estava um pouco quente demais, poderia ser mais confortável.',
    'Achei que a música ambiente estava um pouco alta, pode ser um pouco desconfortável para alguns clientes.',
    'Notei que o ambiente estava um pouco abafado, talvez fosse bom melhorar a ventilação.',
    'Fiquei um pouco surpreso(a) com a falta de opções de revistas na área de espera, poderia ter uma seleção mais atualizada.',
    'Achei que a finalização do penteado poderia ter sido mais caprichada, algumas partes ficaram desalinhadas.',
    'Notei que você estava um pouco apressado(a) durante o serviço, isso pode afetar a qualidade do resultado final.',
    'Achei que a explicação sobre os cuidados pós-tratamento foi um pouco superficial, poderia ser mais detalhada.',
    'Notei que a cadeira de espera estava um pouco desconfortável, talvez seja bom considerar opções mais confortáveis.',
    'Achei que a iluminação no salão poderia ser mais suave, para criar um ambiente mais relaxante.',
    'Notei que a toalha usada durante o serviço estava um pouco áspera, talvez seja bom investir em toalhas mais macias.',
    'Achei que a seleção de produtos disponíveis para venda era um pouco limitada, talvez fosse bom oferecer mais opções.'
]
# Gerar dados fictícios para um ano (cerca de 20.000 linhas)
dados = []
data_inicial = datetime.strptime('2023-01-01 09:00', '%Y-%m-%d %H:%M')
data_final = datetime.strptime('2024-05-08 18:00', '%Y-%m-%d %H:%M')
intervalo_minutos = 30

while data_inicial <= data_final:
    for atendente in atendentes:
        dados.append({
            'Dia e Hora': data_inicial.strftime('%Y-%m-%d %H:%M:%S'),
            'Atendente': atendente,
            'Cliente': faker.name(),
            'Tipo de Serviço': faker.random.choice(servicos),
            'Observação': faker.random.choice(observacao)
        })
    data_inicial += timedelta(minutes=intervalo_minutos)

# Criar DataFrame com os dados
df = pd.DataFrame(dados)

# Salvar os dados em um arquivo CSV
df.to_csv('dados_aleatorios.csv', index=False)