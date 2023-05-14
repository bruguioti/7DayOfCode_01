#include <iostream>
using namespace std;

// Defini��o da classe Paciente
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

// Defini��o da classe ListaPacientes
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
            cout << "A lista de pacientes est� vazia." << endl;
        } else {
            Paciente* atual = cabeca;
            while (atual != NULL) {
                cout << "Nome: " << atual->nome << ", Identifica��o: " << atual->identificacao << ", Estado de Sa�de: " << atual->estado_saude << endl;
                atual = atual->proximo;
            }
        }
    }
};

int main() {
    ListaPacientes listaPacientes;

    // Adicionando pacientes � lista
    listaPacientes.adicionarPaciente("Jo�o", 1, "Est�vel em tratamento intensivo");
    listaPacientes.adicionarPaciente("Maria", 2, "Em estado cr�tico");
    listaPacientes.adicionarPaciente("Pedro", 3, "Est�vel");

    // Listando os pacientes
    listaPacientes.listarPacientes();

    return 0;
}

