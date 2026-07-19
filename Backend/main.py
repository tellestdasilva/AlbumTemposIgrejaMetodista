import os
import glob
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
#from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Cria a instancia da aplicação FastAPI
app = FastAPI()

# Libera o acesso para o frontend (qualquer origem pode chamar a API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Caminhos absolutos: o servidor acha a pasta de imagens
# independente de onde o comando for executado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

#app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

figurinhas = [
            {   "id": 1,
                "nome": "Igreja Metodista Jardinópolis",
                "address": "Rua Três Ilhas, 96. Santa Luzia",
                "CEP": "36030-020",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/1/imagem"
            },
            {
                "id": 2,
                "nome": "Congregação Jardim de Alá",
                "address": "Rua Elvira Bellei, 455. Jardim de Alá",
                "CEP": "36030-560",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/2/imagem"
            },
            {   "id": 3,
                "nome": "Igreja Metodista Bela Aurora",
                "address": "Rua Doutor Costa Reis, 380. Bela Aurora",
                "CEP": "36032-580",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/3/imagem"
            },
            {
                "id": 6,
                "nome": "Igreja Metodista Peniel",
                "address": "Rua Cruzador Bahia, 269. Dom Bosco",
                "CEP": "36025-430",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/6/imagem"
            },
            {
                "id": 7,
                "nome": "Igreja Metodista Itatiaia",
                "address": "Rua Antônio Rufino, 85. São Pedro",
                "CEP": "36037-130",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/7/imagem"
            },
            {
                "id": 8,
                "nome": "Congregação Metodista Borboleta",
                "address": "Rua São Cosme, 245. Borboleta",
                "CEP": "36036-230",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/8/imagem"
            },
            {
                "id": 11,
                "nome": "Igreja Metodista São Mateus",
                "address": "Avenida Independência (atualmente Presidente Itamar Franco), 1757. São Mateus",
                "CEP": "36016-321",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/11/imagem"
            },
            {
                "id": 12,
                "nome": "Campo Missionário Distrital Granbery",
                "address": "Rua Barão de Santa Helena, 300. Centro",
                "CEP": "36010-520",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/12/imagem"
            },
            {
                "id": 13,
                "nome": "Igreja Metodista Central",
                "address": "Rua Marechal Deodoro, 700. Centro",
                "CEP": "36015-460",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/13/imagem"
            },
            {
                "id": 14,
                "nome": "Igreja Metodista Monte Castelo",
                "address": "Rua dos Palmares, 78. Monte Castelo",
                "CEP": "36081-030",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/14/imagem"
            },
            {
                "id": 16,
                "nome": "Igreja Metodista Vitória dos Fiéis",
                "address": "Rua Inácio da Gama, 667. Lourdes",
                "CEP": "36070-420",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/16/imagem"
            },
            {
                "id": 17,
                "nome": "Congregação Vitorino Braga",
                "address": "Rua Henrique Vaz, 569. Ladeira",
                "CEP": "36052-590",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/17/imagem"
            },
            {
                "id": 18,
                "nome": "Igreja Metodista São Benedito",
                "address": "Avenida Gilberto Costa, 760. São Benedito",
                "CEP": "36061-140",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/18/imagem"
            },
            {
                "id": 19,
                "nome": "Congregação Metodista de Linhares",
                "address": "Rua Diva Garcia, 1715. Linhares",
                "CEP": "36060-300",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/19/imagem"
            },
            {
                "id": 20,
                "nome": "Igreja Metodista Betel",
                "address": "Rua Carmela Dutra, 1715. Nossa Sra. Aparecida",
                "CEP": "36052-`470",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/20/imagem"
            },
            {
                "id": 21,
                "nome": "Igreja Metodista Eldorado",
                "address": "Rua Luiz Rocha, 651. Eldorado",
                "CEP": "36046-205",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/21/imagem"
            },
            {
                "id": 22,
                "nome": "Igreja Metodista Benfica",
                "address": "Avenida Juscelino Kubitschek, 6229. Benfica",
                "CEP": "36090-280",
                "Cidade": "Juiz de Fora",
                "imagem_url": "/figurinhas/22/imagem"
            },
            {
                "id": 26,
                "nome": "Igreja Metodista Goianá",
                "address": "Rua 21 de Dezembro, 872. Centro",
                "CEP": "36152-000",
                "Cidade": "Goianá",
                "imagem_url": "/figurinhas/26/imagem"
            },
            {
                "id": 27,
                "nome": "Congregação Metodista Piraúba",
                "address": "Rua Projetada, s/n. Boa Vista",
                "CEP": "36170-000",
                "Cidade": "Piraúba",
                "imagem_url": "/figurinhas/27/imagem"
            },
            {
                "id": 28,
                "nome": "Igreja Metodista Central",
                "address": "Rua Manoel Lobato, 88. Centro",
                "CEP": "36700-000",
                "Cidade": "Leopoldina",
                "imagem_url": "/figurinhas/28/imagem"
            },
            {
                "id": 29,
                "nome": "Igreja Metodista Central",
                "address": "Rua Pedro de Oliveira, 381. Centro",
                "CEP": "36800-000",
                "Cidade": "Carangola",
                "imagem_url": "/figurinhas/29/imagem"
            },
            {
                "id": 30,
                "nome": "Igreja Metodista Barbacena",
                "address": "Avenida Bias Fortes, 575. Centro",
                "CEP": "36200-000",
                "Cidade": "Barbacena",
                "imagem_url": "/figurinhas/30/imagem"
            },
            {
                "id": 31,
                "nome": "Igreja Metodista em Ouro Branco",
                "address": "Rua Dedine, 481. Siderurgia",
                "CEP": "36420-000",
                "Cidade": "Ouro Branco",
                "imagem_url": "/figurinhas/31/imagem"
            },
            {
                "id": 32,
                "nome": "Igreja Metodista Conselheiro Lafaiete",
                "address": "Rua Cel. Albino, 125. Centro",
                "CEP": "36400-000",
                "Cidade": "Conselheiro Lafaiete",
                "imagem_url": "/figurinhas/32/imagem"
            },
            {
                "id": 33,
                "nome": "Igreja Metodista Central de Belo Horizonte",
                "address": "Rua Tupis, 51. Centro",
                "CEP": "30190-060",
                "Cidade": "Belo Horizonte",
               "imagem_url": "/figurinhas/33/imagem"
            },
            {
                "id": 34,
                "nome": "Igreja Metodista do Barreiro",
                "address": "Rua Gilmar Pereira Rosa, 12. Cardoso",
                "CEP": "30626-370",
                "Cidade": "Belo Horizonte",
               "imagem_url": "/figurinhas/34/imagem"
            },
            {
                "id": 36,
                #Região 1
                "nome": "Igreja Metodista em Tijuca",
                "address": "Rua Engenheiro Adel, 25. Tijuca",
                "CEP": "20260-210",
                "Cidade": "Rio de Janeiro",
                "imagem_url": "/figurinhas/36/imagem"
            },
            {
                "id": 37,
                #Região 1
                "nome": "Catedral Metodista do Rio de Janeiro",
                "address": "Praça José de Alencar, 4. Flamengo",
                "CEP": "22230-020",
                "Cidade": "Rio de Janeiro",
                "imagem_url": "/figurinhas/37/imagem"
            },
            {
                "id": 38,
                #Região 1
                "nome": "Catedral Metodista de Petrópolis",
                "address": "Rua Marechal Deodoro, 80. Centro",
                "CEP": "25620-150",
                "Cidade": "Petrópolis",
                "imagem_url": "/figurinhas/38/imagem"
            },
            {
                "id": 39,
                #Região 3
                "nome": "Igreja Metodista em Morro Grande",
                "address": "Rua Joaquim Ribeiro, 349. Sítio Morro Grande",
                "CEP": "02809-000",
                "Cidade": "São Paulo",
                "imagem_url": "/figurinhas/39/imagem"
            }
          ]

# Define a rota para o metodo GET em ("/templos/")
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna o dicionario que sera convertido automaticamente para JSON
    return figurinhas

@app.get("/figurinhas/{id}/imagem")
def imagem_da_figurinha(id: int):
    # Procura o arquivo que começa com o número da figurinha (ex: "07-Tim.jpeg").
    # O [!0-9] logo depois do número evita que o id 1 case com "10-Wes.jpg".
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)

    # Nenhum arquivo encontrado para esse id
    if not arquivos:
        raise HTTPException(status_code=404, detail="Foto do Templo não encontrada")

    # Entrega os bytes da imagem (o FastAPI descobre o Content-Type pela extensão)
    return FileResponse(arquivos[0])
