<head>
<h3> Desafio Otimizando o Sistema Bancário com Funções Python</h3>
<p>Desafio elaborado por Guilherme Arthur de Carvalho</p>
</head>
<body>
<h4>Narrativa</h4>
<p>Precisamos deixar nosso código mais modularizado, para isso, vamos criar funções para as opções existentes: sacar, depositar e visualizar histórico.</p>
<p>Além disso, para a versão 2 do nosso sistema, precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário)</p>
<p>Devemos criar funções para todas as operações do sistema</p>
<p>Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos.</p>
<p>O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor </p>
<p>Precisamos criar duas novas funções: criar usuário e criar conta corrente</p>
<p>Fique a vontade para adicionar mais funções, exemplo: listar contas</p>

<h4>Objetivo Geral</h4>
<p>Separar as funções existentes de saque, depósito e extrato em funções </p>
<p>Criar duas novas funções:
	<ol>
		<li>Cadastrar usuário (cliente)</li>
		<li>Cadastrar conta bancária</li>
	</ol>
</p>

<h4>Objetivos Específicos</h4>

<h6>Função de Depósito</h6>
<p>A função de depósito deve receber os argumentos apenas por posição (positional only)</p>
<p>Sugestão de argumentos: saldo, valor, extrato</p>
<p>Sugestão de retorno: saldo e extrato </p>

<h6>Função de Saque</h6>
<p>A função saque deve receber os argumentos apenas por nome (keyword only)</p>
<p>Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limites_saques</p>
<p>Sugestão de retorno: saldo e extrato</p>

<h6>Operação de Extrato</h6>
<p>A função extrato deve receber os argumentos por posição e nome (positional only e keyword only)</p>
<p>Argumentos posicionais: saldo, argumentos nomeados: extrato</p>

<h6>Criar usuário (cliente)</h6>
<p>O programa deve aramzenar os usuários em lista, um usuário é composto por: nome, data de nascimento, cpf e endereço</p>
<p>O endereço é uma string com formato: logradouro, número, bairro, cidade/ sigla de estado</p>
<p>Deve ser armazenado somente os números do CPF</p>
<p>Não podemos cadastrar dois usuários com o mesmo CPF</p>

<h6>Criar conta corrente</h6>
<p>O programa deve aramzenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário</p>
<p>O número da conta é sequencial, iniciando em 1</p>
<p>O número da agência é fixo: "0001"</p>
<p>O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário</p>

<h6>Dica</h6>
<p>Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista</p>
</body>