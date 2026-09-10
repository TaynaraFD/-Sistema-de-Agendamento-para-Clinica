pacientes = []
profissionais = []
agendamentos = []


def cadastrar_paciente():
    print("\n--- CADASTRO DE PACIENTE ---")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")

    paciente = {
        "nome": nome,
        "telefone": telefone,
        "cpf": cpf
    }

    pacientes.append(paciente)

    print("\nPaciente cadastrado com sucesso!")


def cadastrar_profissional():
    print("\n--- CADASTRO DE PROFISSIONAL ---")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")
    area = input("Área profissional: ")

    profissional = {
        "nome": nome,
        "telefone": telefone,
        "cpf": cpf,
        "area": area
    }

    profissionais.append(profissional)

    print("\nProfissional cadastrado com sucesso!")


def mostrar_pacientes():
    print("\n--- PACIENTES CADASTRADOS ---")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    for paciente in pacientes:
        print("-------------------------")
        print("Nome:", paciente["nome"])
        print("Telefone:", paciente["telefone"])
        print("CPF:", paciente["cpf"])


def mostrar_profissionais():
    print("\n--- PROFISSIONAIS CADASTRADOS ---")

    if len(profissionais) == 0:
        print("Nenhum profissional cadastrado.")
        return

    for profissional in profissionais:
        print("-------------------------")
        print("Nome:", profissional["nome"])
        print("Telefone:", profissional["telefone"])
        print("CPF:", profissional["cpf"])
        print("Área:", profissional["area"])


def agendar_consulta():
    print("\n--- AGENDAMENTO ---")

    if len(pacientes) == 0:
        print("Não existem pacientes cadastrados.")
        return

    if len(profissionais) == 0:
        print("Não existem profissionais cadastrados.")
        return

    nome_paciente = input("Nome do paciente: ")
    nome_profissional = input("Nome do profissional: ")
    data = input("Data da consulta (DD/MM/AAAA): ")
    horario = input("Horário da consulta (HH:MM): ")

    paciente_encontrado = None
    profissional_encontrado = None

    for paciente in pacientes:
        if paciente["nome"].lower() == nome_paciente.lower():
            paciente_encontrado = paciente

    for profissional in profissionais:
        if profissional["nome"].lower() == nome_profissional.lower():
            profissional_encontrado = profissional

    if paciente_encontrado is None:
        print("\nPaciente não encontrado.")
        return

    if profissional_encontrado is None:
        print("\nProfissional não encontrado.")
        return

    # Verifica conflito de horário
    for agendamento in agendamentos:
        if (
            agendamento["profissional"]["nome"].lower()
            == profissional_encontrado["nome"].lower()
            and agendamento["data"] == data
            and agendamento["horario"] == horario
        ):
            print("\nERRO: Esse profissional já possui uma consulta nesse horário.")
            return

    novo_agendamento = {
        "paciente": paciente_encontrado,
        "profissional": profissional_encontrado,
        "data": data,
        "horario": horario
    }

    agendamentos.append(novo_agendamento)

    print("\nConsulta agendada com sucesso!")


def mostrar_agenda():
    print("\n--- AGENDA ---")

    if len(agendamentos) == 0:
        print("Nenhuma consulta agendada.")
        return

    for consulta in agendamentos:
        print("-------------------------")
        print("Paciente:", consulta["paciente"]["nome"])
        print("Profissional:", consulta["profissional"]["nome"])
        print("Área:", consulta["profissional"]["area"])
        print("Data:", consulta["data"])
        print("Horário:", consulta["horario"])


def cancelar_consulta():
    print("\n--- CANCELAMENTO DE CONSULTA ---")

    if len(agendamentos) == 0:
        print("Nenhuma consulta agendada.")
        return

    mostrar_agenda()

    nome_paciente = input("\nNome do paciente: ")
    data = input("Data da consulta: ")
    horario = input("Horário da consulta: ")

    for consulta in agendamentos:
        if (
            consulta["paciente"]["nome"].lower() == nome_paciente.lower()
            and consulta["data"] == data
            and consulta["horario"] == horario
        ):
            agendamentos.remove(consulta)
            print("\nConsulta cancelada com sucesso!")
            return

    print("\nConsulta não encontrada.")


def remarcar_consulta():
    print("\n--- REMARCAÇÃO DE CONSULTA ---")

    if len(agendamentos) == 0:
        print("Nenhuma consulta agendada.")
        return

    nome_paciente = input("Nome do paciente: ")
    data_atual = input("Data atual da consulta: ")
    horario_atual = input("Horário atual da consulta: ")

    consulta_encontrada = None

    for consulta in agendamentos:
        if (
            consulta["paciente"]["nome"].lower() == nome_paciente.lower()
            and consulta["data"] == data_atual
            and consulta["horario"] == horario_atual
        ):
            consulta_encontrada = consulta
            break

    if consulta_encontrada is None:
        print("\nConsulta não encontrada.")
        return

    nova_data = input("Nova data: ")
    novo_horario = input("Novo horário: ")

    # Verifica se o novo horário está disponível
    for consulta in agendamentos:
        if (
            consulta != consulta_encontrada
            and consulta["profissional"]["nome"].lower()
            == consulta_encontrada["profissional"]["nome"].lower()
            and consulta["data"] == nova_data
            and consulta["horario"] == novo_horario
        ):
            print("\nERRO: O profissional já possui uma consulta nesse horário.")
            return

    consulta_encontrada["data"] = nova_data
    consulta_encontrada["horario"] = novo_horario

    print("\nConsulta remarcada com sucesso!")


def menu():
    while True:
        print("\n================================")
        print("   SISTEMA DE AGENDAMENTO")
        print("================================")
        print("1 - Cadastrar paciente")
        print("2 - Cadastrar profissional")
        print("3 - Ver pacientes")
        print("4 - Ver profissionais")
        print("5 - Agendar consulta")
        print("6 - Ver agenda")
        print("7 - Cancelar consulta")
        print("8 - Remarcar consulta")
        print("9 - Sair")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()

        elif opcao == "2":
            cadastrar_profissional()

        elif opcao == "3":
            mostrar_pacientes()

        elif opcao == "4":
            mostrar_profissionais()

        elif opcao == "5":
            agendar_consulta()

        elif opcao == "6":
            mostrar_agenda()

        elif opcao == "7":
            cancelar_consulta()

        elif opcao == "8":
            remarcar_consulta()

        elif opcao == "9":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


menu()
