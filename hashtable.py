class HashTable:
    """Uma tabela hash genérica para armazenar strings."""

    def __init__(self):
        """Inicializa a tabela hash."""
        self.tamanho_tab = 15
        self.tabela_hash = [[] for _ in range(self.tamanho_tab)]


    def adicionar(self, chave: str) -> bool:
        """
        Adiciona uma chave à tabela hash.
        Retorna True se a chave foi adicionada, False caso contrário.
        """
        indice = self.__funcao_hash(chave)
        # Verifica se o gerente já está cadastrado
        for item in self.tabela_hash[indice]: #aqui percorre a lista item que esta na posicao do indice da tabela hash
            if item == chave:
                print(f"Email '{chave}' já cadastrado.")
                return False
        # adiciona um novo email no final dessa lista
        self.tabela_hash[indice].append(chave)
        print(f"Email '{chave}' adicionado com sucesso.")
        return True

    def remover(self, chave: str) -> bool:
        """
        Remove uma chave da tabela hash.
        Retorna True se a chave foi removida, False caso contrário.
        """
        indice = self.__funcao_hash(chave)
        for item in self.tabela_hash[indice]:  #
            if item == chave:
                self.tabela_hash[indice].remove(chave)
                print(f"Email '{chave}' removido com sucesso.")
                return True
        print("Email nao pode ser removido pois nao existe")
        return False

    def listar(self) -> list[str]:
        """Lista todas as chaves na tabela hash."""
        lista_aux = []
        for lista in self.tabela_hash:
            for elemento in lista:
                lista_aux.append(elemento)

        print (lista_aux)

        return lista_aux


    def __funcao_hash(self, chave: str) -> int:
        """Calcula o índice da tabela hash para uma chave."""
        indice = sum(ord(c) for c in chave) % self.tamanho_tab
        return indice
