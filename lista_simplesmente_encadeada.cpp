#include <iostream>
using namespace std;

// Definição da classe Paciente
class Paciente {
public:
    string nome;
    int identificacao;
    string estado_saude;
    Paciente* proximo;

    Paciente(string nome, int identificacao, string estado_saude) {
        this->nome = nome;
        this->identificacao = identificacao;
        this->estado_saude = estado_saude;
        this->proximo = NULL;
    }
};

// Definição da classe ListaPacientes
class ListaPacientes {
private:
    Paciente* cabeca;
    Paciente* calda;

public:
    ListaPacientes() {
        cabeca = NULL;
        calda = NULL;
    }

    void adicionarPaciente(string nome, int identificacao, string estado_saude) {
        Paciente* novoPaciente = new Paciente(nome, identificacao, estado_saude);
        if (cabeca == NULL) {
            cabeca = novoPaciente;
            calda = novoPaciente;
        } else {
            calda->proximo = novoPaciente;
            calda = novoPaciente;
        }
    }

    void listarPacientes() {
        if (cabeca == NULL) {
            cout << "A lista de pacientes está vazia." << endl;
        } else {
            Paciente* atual = cabeca;
            while (atual != NULL) {
                cout << "Nome: " << atual->nome << ", Identificação: " << atual->identificacao << ", Estado de Saúde: " << atual->estado_saude << endl;
                atual = atual->proximo;
            }
        }
    }
};

int main() {
    ListaPacientes listaPacientes;

    // Adicionando pacientes à lista
    listaPacientes.adicionarPaciente("João", 1, "Estável em tratamento intensivo");
    listaPacientes.adicionarPaciente("Maria", 2, "Em estado crítico");
    listaPacientes.adicionarPaciente("Pedro", 3, "Estável");

    // Listando os pacientes
    listaPacientes.listarPacientes();

    return 0;
}

