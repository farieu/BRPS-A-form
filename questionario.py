import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def obternome(self):
        return self.nome

    def obteridade(self):
        return self.idade
    
#"Aqui teria que ter um input, e processar esse input pra botar numa váriavel."    
#pessoa = Pessoa("Caio", 37)
#print (pessoa.obteridade())
#print (pessoa.obternome())

class PreocupaçãoSomática:
    def __init__(self, resp1, resp2, resp3, resp4):
        self.pergunta1 = "Como costuma ser sua saúde física (do corpo)?"
        self.pergunta2 = "Como esteve sua saúde no último ano?"
        self.pergunta3 = "Você está preocupado com algum problema de saúde agora?"
        self.pergunta4 = "Você sente que tem alguma coisa incomum acontecendo com seu corpo ou cabeça?"
        self.resp1 = resp1
        self.resp2 = resp2
        self.resp3 = resp3
        self.resp4 = resp4

    def SaudeFisica(self):
        return self.resp1
    
    def SaudeUltimoAno(self):
        return self.resp2
    
    def SaudeAgora(self):
        return self.resp3
    
    def SaudeIncomum(self):
        return self.resp4
    
#As perguntas 7, 8 e 9 dependem da resposta da 6a.
class Ansiedade:
    def __init__(self, resp5, resp6, resp7, resp8, resp9):
        self.pergunta5 = "Você está preocupado com alguma coisa?"
        self.pergunta6 = "Você tem se sentido tenso ou ansioso a maior parte do tempo?"
        self.pergunta7 = "Quando se sente assim, você consegue saber o porquê?"
        self.pergunta8 = "De que forma suas ansiedades ou preocupações afetam o seu dia a dia?"
        self.pergunta9 = "Existe algo que ajuda a melhorar essa sensação?"
        self.resp5 = resp5
        self.resp6 = resp6
        self.resp7 = resp7
        self.resp8 = resp8
        self.resp9 = resp9

    def AnsiedadePreocupacao(self):
        return self.resp5
    
    def AnsiedadeTenso(self):
        return self.resp6
    
    def AnsiedadeMotivo(self):
        return self.resp7
    
    def AnsiedadeRotina(self):
        return self.resp8
    
    def AnsiedadeMelhora(self):
        return self.resp9
    
"As seções RETRAIMENTO AFETIVO (3) e DESORGANIZAÇÃO CONCEITUAL (4) são pontuadas a partir de observações do entrevistador ao usuário."
class SentimentosDeCulpa:
    def __init__(self, resp10, resp11, resp12, resp13):
        self.pergunta10 = "Nos últimos dias você tem se sentido um peso para sua família ou colegas?"
        self.pergunta11 = "Você tem se sentido culpado por alguma coisa feita no passado?"
        self.pergunta12 = "Você acha que o que está passando agora é um tipo de castigo?"
        self.pergunta13 = "Por que você acha isso?"
        self.resp10 = resp10
        self.resp11 = resp11
        self.resp12 = resp12
        self.resp13= resp13

    def SentimentosPeso(self):
        return self.resp10
    
    def SentimentosCulpa(self):
        return self.resp11
    
    def SentimentosCastigo(self):
        return self.resp12
    
    def SentimentosMotivo(self):
        return self.resp13
    
"As seções TENSÃO (6) e MANEIRISMOS E POSTURA (7) são pontuadas a partir de observações do entrevistador ao usuário."
class IdeiasDeGrandeza:
    def __init__(self, resp14, resp15, resp16, resp17):
        self.pergunta14 = "Nos últimos dias você tem se sentido com algum talento ou habilidade que a maioria das pessoas não tem?"
        self.pergunta15 = "Como você sabe disso?"
        self.pergunta16 = "Você acha que as pessoas têm tido inveja de você?"
        self.pergunta17 = "Você tem acreditado que tenha alguma coisa importante para fazer no mundo?"
        self.resp14 = resp14
        self.resp15 = resp15
        self.resp16 = resp16
        self.resp17 = resp17

    def IdeiasTalento(self):
        return self.resp14
    
    def IdeiasConhecimento(self):
        return self.resp15
    
    def IdeiasInveja(self):
        return self.resp16
    
    def IdeiasImportante(self):
        return self.resp17
    
class HumorDepressivo:
    def __init__(self, resp18, resp19, resp20):
        self.pergunta18 = "Como tem estado seu humor (alegre, triste, irritável)?"
        self.pergunta19 = "Você acredita que pode melhorar?"
        self.pergunta20 = "Como esse sentimento tem afetado seu dia a dia?"
        self.resp18 = resp18
        self.resp19 = resp19
        self.resp20 = resp20

    def HumorEstado(self):
        return self.resp18
    
    def HumorMelhoria(self):
        return self.resp19
    
    def HumorInfluencia(self):
        return self.resp20
    
"A seção HOSTILIDADE (10) é pontuada a partir de uma análise do relato verbal e das suas respostas."
class Hostilidade:
    def __init__(self, resp21, resp22, resp23, resp24):
        self.pergunta21 = "Nos últimos dias você tem estado impaciente ou irritávelcom as outras pessoas?"
        self.pergunta22 = "Conseguiu manter o controle?"
        self.pergunta23 = "Tolerou as provocações?"
        self.pergunta24 = "Chegou a agredir alguém ou quebrar objetos?"
        self.resp21 = resp21
        self.resp22 = resp22
        self.resp23 = resp23
        self.resp24 = resp24

    def HostilidadeImpaciencia(self):
        return self.resp21
    
    def HostilidadeControle(self):
        return self.resp22
    
    def HostilidadeProvocações(self):
        return self.resp23
    
    def HostilidadeAgressividade(self):
        return self.resp24

"A seção DESCONFIANÇA (11) é pontuada mediante informação subjetiva, mas ainda sim, tem perguntas."
class Desconfiança:
    def __init__(self, resp25, resp26, resp27, resp28, resp29):
        self.pergunta25 = "Você tem tido a impressão de que as outras pessoas estão falando ou rindo de você?"
        self.pergunta26 = "De que forma você percebe isso?"
        self.pergunta27 = "Você tem achado que tem alguém com más intenções contra você ou se esforçado para lhe causar problemas?"
        self.pergunta28 = "Quem? Por quê?"
        self.pergunta29 = "Como você sabe disso?"
        self.resp25 = resp25
        self.resp26 = resp26
        self.resp27 = resp27
        self.resp28 = resp28
        self.resp29 = resp29

    def DesconfiancaImpressao(self):
        return self.resp25
    
    def DesconfiancaPerceber(self):
        return self.resp26
    
    def DesconfiancaIntencoes(self):
        return self.resp27
    
    def DesconfiancaQuem(self):
        return self.resp28
    
    def DesconfiancaConhecimento(self):
        return self.resp29
    
#As respostas do conjunto de perguntas (32 a 35) e (37 a 40) dependem das respostas da 31 e da 36, respectivamente.
class ComportamentoAlucinatório:
    def __init__(self, resp30, resp31, resp32, resp33, resp34, resp35, resp36, resp37, resp38, resp39, resp40):
        self.pergunta30 = "Você tem tido experiências incomuns que a maioria das pessoas não tem?"
        self.pergunta31 = "Você tem escutado coisas que as outras pessoas não podem ouvir?"
        self.pergunta32 = "Você estava acordado nesse momento?"
        self.pergunta33 = "O que você ouvia - barulhos, cochichos, vozes conversando com você ou conversando entre si?"
        self.pergunta34 = "Com que frequência?"
        self.pergunta35 = "Interferem no seu dia a dia?"
        self.pergunta36 = "Você tem visto coisas que a maioria das pessoas não pode ver?"
        self.pergunta37 = "Você estava acordado nesse momento?"
        self.pergunta38 = "O que você via - luzes, formas, imagens?"
        self.pergunta39 = "Com que frequência?"
        self.pergunta40 = "Interferem no seu dia a dia?"
        self.resp30 = resp30
        self.resp31 = resp31
        self.resp32 = resp32
        self.resp33 = resp33
        self.resp34 = resp34
        self.resp35 = resp35
        self.resp36 = resp36
        self.resp37 = resp37
        self.resp38 = resp38
        self.resp39 = resp39
        self.resp40 = resp40

    def AlucinacaoExperiencia(self):
        return self.resp30
    
    def AlucinacaoEscutado(self):
        return self.resp31
    
    def AlucinacaoAcordado1(self):
        return self.resp32
    
    def AlucinacaoOuvia(self):
        return self.resp33
    
    def AlucinacaoFrequencia1(self):
        return self.resp34
    
    def AlucinacaoInterferem1(self):
        return self.resp35
    
    def AlucinacaoVisto(self):
        return self.resp36
    
    def AlucinacaoAcordado2(self):
        return self.resp37
    
    def AlucinacaoVia(self):
        return self.resp38
    
    def AlucinacaoFrequencia2(self):
        return self.resp39
    
    def AlucinacaoInterferem2(self):
        return self.resp40

"As seções RETARDAMENTO MOTOR (13) e FALTA DE COOPERAÇÃO COM A ENTREVISTA (14) são pontuadas a partir de observações do entrevistador ao usuário."
class Delírios:
    def __init__(self, resp41, resp42, resp43):
        self.pergunta41 = "Você tem acreditado que alguém ou alguma coisa fora de você esteja controlando seus pensamentos ou suas ações contra a sua vontade?"
        self.pergunta42 = "Você tem a impressão de que o rádio ou a televisão mandam mensagens para você?"
        self.pergunta43 = "Você sente que alguma coisa incomum esteja acontecendo ou está para acontecer?"
        self.resp41 = resp41
        self.resp42 = resp42
        self.resp43 = resp43

    def DelirioControle(self):
        return self.resp41
    
    def DelirioComunicacao(self):
        return self.resp42
    
    def DelirioIncomum(self):
        return self.resp43

"As seções AFETO EMBOTADO (16), EXCITAÇÃO (17) e  DESORIENTAÇÃO (18) são pontuadas a partir de observações do entrevistador ao usuário."
"Apesar de haver perguntas na seção de DESORIENTAÇÃO, se trata de refazer perguntas como nome, idade, etc."

def main():
    nome = input("Qual é o seu nome? ")
    idade = int(input("Qual é a sua idade? "))

    preoc_somatica = PreocupaçãoSomática("", "", "", "")
    resp1 = input("1. " + preoc_somatica.pergunta1 + " ")
    resp2 = input("2. " + preoc_somatica.pergunta2 + " ")
    resp3 = input("3. " + preoc_somatica.pergunta3 + " ")
    resp4 = input("4. " + preoc_somatica.pergunta4 + " ")

    ansiedade = Ansiedade("", "", "", "", "")
    culpa = SentimentosDeCulpa("", "", "", "")
    resp5 = input("5. " + ansiedade.pergunta5 + " ")
    resp6 = input("6. " + ansiedade.pergunta6 + " ")
    resp7 = input("7. " + ansiedade.pergunta7 + " ")
    resp8 = input("8. " + ansiedade.pergunta8 + " ")
    resp9 = input("9. " + ansiedade.pergunta9 + " ")
    
    resp10 = input("10. " + culpa.pergunta10 + " ")

    resp11 = input("11. " + culpa.pergunta11 + " ")
    resp12 = input("12. " + culpa.pergunta12 + " ")
    resp13 = input("13. " + culpa.pergunta13 + " ")

    grandeza = IdeiasDeGrandeza("", "", "", "")
    resp14 = input("14. " + grandeza.pergunta14 + " ")
    resp15 = input("15. " + grandeza.pergunta15 + " ")
    resp16 = input("16. " + grandeza.pergunta16 + " ")
    resp17 = input("17. " + grandeza.pergunta17 + " ")
    
    humor = HumorDepressivo("", "", "")
    resp18 = input("18. " + humor.pergunta18 + " ")
    resp19 = input("19. " + humor.pergunta19 + " ")
    resp20 = input("20. " + humor.pergunta20 + " ")

    hostilidade = Hostilidade("", "", "", "")
    resp21 = input("21. " + hostilidade.pergunta21 + " ")
    resp22 = input("22. " + hostilidade.pergunta22 + " ")
    resp23 = input("23. " + hostilidade.pergunta23 + " ")
    resp24 = input("24. " + hostilidade.pergunta24 + " ")

    desconfianca = Desconfiança("", "", "", "", "")
    resp25 = input("25. " + desconfianca.pergunta25 + " ")
    resp26 = input("26. " + desconfianca.pergunta26 + " ")
    resp27 = input("27. " + desconfianca.pergunta27 + " ")
    resp28 = input("28. " + desconfianca.pergunta28 + " ")
    resp29 = input("29. " + desconfianca.pergunta29 + " ")

    alucionacoes = ComportamentoAlucinatório("", "", "", "", "", "", "", "", "", "")
    resp30 = input("30. " + alucionacoes.pergunta30 + " ")
    resp31 = input("31. " + alucionacoes.pergunta31 + " ")
    resp32 = input("32. " + alucionacoes.pergunta32 + " ")
    resp33 = input("33. " + alucionacoes.pergunta33 + " ")
    resp34 = input("34. " + alucionacoes.pergunta34 + " ")
    resp35 = input("35. " + alucionacoes.pergunta35 + " ")
    resp36 = input("36. " + alucionacoes.pergunta36 + " ")
    resp37 = input("37. " + alucionacoes.pergunta37 + " ")
    resp38 = input("38. " + alucionacoes.pergunta38 + " ")
    resp39 = input("39. " + alucionacoes.pergunta39 + " ")
    resp40 = input("40. " + alucionacoes.pergunta40 + " ")

    delirios = Delírios("", "", "")
    resp41 = input("41. " + delirios.pergunta41 + " ")
    resp42 = input("42. " + delirios.pergunta42 + " ")
    resp43 = input("43. " + delirios.pergunta43 + " ")

    pessoa = Pessoa(nome, idade)
    preocupacao_somatica = PreocupaçãoSomática(resp1, resp2, resp3, resp4)
    anxiety = Ansiedade(resp5, resp6, resp7, resp8, resp9)
    guilty = SentimentosDeCulpa(resp10, resp11, resp12, resp13)
    superiority_complex = IdeiasDeGrandeza(resp14, resp15, resp16, resp17)
    depression = HumorDepressivo(resp18, resp19, resp20)
    hostility = Hostilidade(resp21, resp22, resp23, resp24)
    distrust = Desconfiança(resp25, resp26, resp27, resp28, resp29)
    hallucinations = ComportamentoAlucinatório(resp30, resp31, resp32, resp33, resp34, resp35, resp36, resp37, resp38, resp39, resp40)
    delusions = Delírios(resp41, resp42, resp43)

    # print("Nome: ", pessoa.obternome())
    # print("Idade: ", pessoa.obteridade())
    # print("Respostas do usuário por seção: ")
    # print("- Saúde física: ", preocupacao_somatica.pergunta1, preocupacao_somatica.SaudeFisica())
    # print("- ", preocupacao_somatica.pergunta2, preocupacao_somatica.SaudeUltimoAno())
    # print("- ", preocupacao_somatica.pergunta3, preocupacao_somatica.SaudeAgora())
    # print("- ", preocupacao_somatica.pergunta4, preocupacao_somatica.SaudeIncomum())

        #Parte que converte para um arquivo JSON.
    data = {
        "nome": pessoa.obternome(),
        "idade": pessoa.obteridade(),
        "respostas_sobre_saude": {
            "SaúdeFísica": preocupacao_somatica.SaudeFisica(),
            "SaúdeUltimoAno": preocupacao_somatica.SaudeUltimoAno(),
            "SaúdeAgora": preocupacao_somatica.SaudeAgora(),
            "SaúdeSintomaIncomum": preocupacao_somatica.SaudeIncomum(),
            "Preocupações": anxiety.AnsiedadePreocupacao(),
            "Tensão": anxiety.AnsiedadeTenso(),
            "Motivo": anxiety.AnsiedadeMotivo(),
            "AnsiedadeRotina": anxiety.AnsiedadeRotina(),
            "AnsiedadeMelhora": anxiety.AnsiedadeMelhora(),
            "SentimentosPeso": guilty.SentimentosPeso(),
            "Culpa": guilty.SentimentosCulpa(),
            "Castigo": guilty.SentimentosCastigo(),
            "Motivo": guilty.SentimentosMotivo(),
            "Talento": superiority_complex.IdeiasTalento(),
            "Conhecimento": superiority_complex.IdeiasConhecimento(),
            "Inveja": superiority_complex.IdeiasInveja(),
            "IdeiasImportância": superiority_complex.IdeiasImportante(),
            "HumorEstado": depression.HumorEstado(),
            "HumorMelhoria": depression.HumorMelhoria(),
            "HumorInfluencia": depression.HumorInfluencia(),
            "Impaciência": hostility.HostilidadeImpaciencia(),
            "AutoControle": hostility.HostilidadeControle(),
            "Provocações": hostility.HostilidadeProvocações(),
            "Agressividade": hostility.HostilidadeAgressividade(),
            "ImpressõesDesconfiança": distrust.DesconfiancaImpressao(),
            "PercepçãoDesconfiança": distrust.DesconfiancaPerceber(),
            "IntençãoDesconfiança": distrust.DesconfiancaIntencoes(),
            "PessoaDesconfiança": distrust.DesconfiancaQuem(),
            "ConhecimentoDesconfiança": distrust.DesconfiancaConhecimento(),
            "Alucinações": hallucinations.AlucinacaoExperiencia(),
            "SonsAlucinações": hallucinations.AlucinacaoEscutado(),
            "AlucinaçõesAcordado": hallucinations.AlucinacaoAcordado1(),
            "AlucinaçõesEscuta": hallucinations.AlucinacaoOuvia(),
            "FrequênciaAlucinações": hallucinations.AlucinacaoFrequencia1(),
            "InterferênciaAlucinações": hallucinations.AlucinacaoInterferem1(),
            "VisãoAlucinações": hallucinations.AlucinacaoVisto(),
            "AlucinaçõesAcordado2": hallucinations.AlucinacaoAcordado2(),
            "AlucinaçõesVisão": hallucinations.AlucinacaoVia(),
            "FrequênciaAlucinações2": hallucinations.AlucinacaoFrequencia2(),
            "InterferênciaAlucinações2": hallucinations.AlucinacaoInterferem2(),
            "ControleDelírio": delusions.DelirioControle(),
            "DelírioImpressão": delusions.DelirioComunicacao(),
            "DelírioIncomum": delusions.DelirioIncomum()
        }
    }

    with open("DadosUsuário.json", "w") as arquivo:
        json.dump(data, arquivo)

if __name__ == '__main__':
    main()