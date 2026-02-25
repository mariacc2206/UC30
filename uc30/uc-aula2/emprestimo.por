programa{
    funcao inicio() {
        real valorCasa, salario, prestacao
        inteiro anos, meses

        escreva("Qual valor da casa:")
        leia(valorCasa)

        escreva("Qual seu salário: \n")
        leia(salario)

        escreva("Em quantos anos você deseja pagar:")
        leia(anos)

        meses = anos * 12
        prestacao = valorCasa / meses

        escreva("O valor da prestação é", prestacao)

        se(prestacao <= salario * 0.30) {
            escreva("Empréstimo aprovado \n")
        } senao {
            escreva("Emprestimo não aprovado \n")
        }
        }
    }